from models import Athlete, Team, Game, Play, Collaboration, Action, Observation, db
from transformations import transform_Y2G, transform_down
from create_tables import create_tables, drop_tables
import os
import json
import csv

PATH_TO_TEAM_CODES = 'data/team_codes.txt'
PATH_TO_GAME_LIST = 'data/game_list.csv'

def create_team_records():
	file = open(PATH_TO_TEAM_CODES, 'r')
	teams = []
	while True:
		try:
			name = sanitize_string(file.readline())
			code = sanitize_string(file.readline())
			if code == '':
				break
			teams.append({
				'name': name,
				'code': code
			})
		except Exception:
			break
	file.close()
	print(len(teams))
	with db.atomic():
		Team.insert_many(teams).execute()

#dependency: Team
def create_athlete_records():
	team_dict = get_team_dict()
	filenames = get_json_files("data/rosters/json")
	for filename in filenames:
		file = open(filename, "r")
		contents = file.read()
		file.close()
		athletes = json.loads(contents)
		for athlete in athletes:
			team_code = athlete["team_code"]
			team = team_dict[team_code]
			last_name_comp = athlete['last_name'].split(' ')
			if len(last_name_comp) == 2:
				last_name = last_name_comp[0]
				suffix = last_name_comp[1]
			elif len(last_name_comp) == 1:
				last_name = last_name_comp[0]
			else:
				print("weird name: " + athlete['last_name'])
				last_name = athlete['last_name']
			Athlete.get_or_create(
				first_name =  athlete["first_name"],
				last_name = last_name,
				team = team,
				number = athlete["number"],
				position = athlete["position"],
				height = athlete["height"],
				weight = athlete["weight"],
				year = athlete["year"]
			)




def import_games(path_to_game_list, team_dict):
	with open(PATH_TO_GAME_LIST, 'r') as game_list_file:
		game_file_reader = csv.reader(game_list_file, delimiter=',')
		for row in game_file_reader:
			#make game record
			game, created_ = Game.get_or_create(
				path = row[0],
				team_1 = team_dict[ row[1] ],
				team_2 = team_dict[ row[2] ]
			)
			#import game data
			import_game_data(game, team_dict)
			

def import_game_data(game, team_dict):
	path = game.path
	with open(path, 'r') as file:
		contents = file.read()
		game_dict = json.loads(contents)
		play_data = game_dict['Game Data']
		
		play_numbers = game_dict['Game Data']['Play#']
		num_rows = len(play_numbers)
		current_play_index = None
		current_play = None
		for i in range(0, num_rows):
			next_play_index = play_numbers[i]
			if next_play_index != current_play_index:
				
				current_play_index = next_play_index
				#make a play
				current_play, created_ = Play.get_or_create(
					game = game,
					offense = team_dict[ play_data['Off'][i] ],
					defense = team_dict[ play_data['Def'][i] ],
					index = play_data['Play#'][i],
					quarter = play_data['Q'][i],
					down = transform_down( play_data['Dwn'][i] ),
					half = play_data['Half'][i],
					yards_to_go = transform_Y2G( play_data['Y2G'][i] ),
					yards_line = transform_Y2G( play_data['Yd Ln'][i] ),
					result = play_data['Res'][i] or None
				)
			#make a collaboration
			collaboration, created_ = Collaboration.get_or_create(
				index = i,
				play = current_play
			)
			#make all the actions  
			make_quarterback_action(game_dict['Quarterback'], collaboration, i)
				
def make_quarterback_action(qb_data, collaboration, i):
	quarterback_name_number = qb_data['QB'][i]
	if quarterback_name_number == None or quarterback_name_number.strip() == '':
		return
	athlete = find_athlete(quarterback_name_number)
	action, created_ = Action.get_or_create(
		collaboration = collaboration,
		athlete = athlete,
		action_type = 'QB' 
	)
	for key in qb_data.keys():
		if key != 'QB':
			value = qb_data[key][i]
			if value not in [None, '']:
				print(qb_data[key][i])
				Observation.get_or_create(
					action = action,
					name = key,
					value = qb_data[key][i]
				)
		
				
def find_athlete(quarterback_name_number):
	args = quarterback_name_number.split(' ')
	if len(args) == 3: #first last number
		first_name, last_name, number = args
	elif len(args) == 4:
		first_name, last_name, suffix, number = args
	else:
		print("cannot parse: " + quarterback_name_number)
		return None
	athlete = Athlete.get(
		first_name = first_name,
		last_name = last_name,
		number = number
	)
	return athlete
	
	

def get_json_files(path_to_directory):
	concat_paths = lambda x: path_to_directory + '/' + x
	file_filter = lambda x: '~lock' not in x and '.json' in x
	files = os.listdir(path_to_directory)
	files = filter(file_filter, files)
	files = map(concat_paths, files)
	return files

#get dictionary for looking up team objects by team code
def get_team_dict():
	team_dict = {}
	for team in Team.select():
		team_dict[team.code] = team
	return team_dict

def sanitize_string(string):
	string = string.strip()
	return string

if __name__ == '__main__':
	drop_tables()
	create_tables()
	db.connect()
	create_team_records()
	create_athlete_records()
	team_dict = get_team_dict()
	import_games(PATH_TO_GAME_LIST, team_dict)
	db.close()
