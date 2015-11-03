from models import Athlete, Team, Game, Play, Collaboration, Action, Observation, db
import os
import json

PATH_TO_TEAM_CODES = 'data/team_codes.txt'

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
			Athlete.create_or_get(
				first_name = athlete["first_name"],
				last_name = athlete["last_name"],
				team = team
			)

def create_game_data_records():
	filenames = get_json_files("data/completed_games/json")
	for filename in filenames:
		file = open(filename, "r")
		contents = file.read()
		file.close()
		game = json.loads(contents)

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
	db.connect()

	#create_team_records()
	create_athlete_records()


	db.close()
