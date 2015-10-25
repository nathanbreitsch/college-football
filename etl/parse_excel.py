import openpyxl as pyxl
import os
import json

PATH_TO_COMPLETED_GAMES = 'data/completed_games/excel'
PATH_TO_TEAM_CODES = 'data/team_codes.txt'

#schema: section_name -> { column_name - > [values] }
def read_game_file_xlsx(path):
	wb = pyxl.load_workbook(filename = path, read_only = True)
	if 'Data' in wb.get_sheet_names():
		ws = wb.get_sheet_by_name('Data')
	else:
		print("the following file does not have a Data tab: " + path)
		return None
		
	game_dict = {}
	section = None
	for col in ws.columns:
		if col[0].value != '':
			section = col[0].value
			game_dict[section] = {}
		column_name = col[1].value
		print('here')
		game_dict[section][column_name] = [x.value for x in col[2:]]
		
	return game_dict
	
def read_rosters_xlsx(path):
	wb = pyxl.load_workbook(filename = path, read_only = True)
	if 'Rosters' in wb.get_sheet_names():
		ws = wb.get_sheet_by_name('Rosters')
	else:
		print("the following file does not have a Roster tab: " + path)
		return None
	athletes = []
	initial = True #idk what ws.rows is or how to skip first element
	for row in ws.rows:
		if not initial and row[1].value is not None:
			athletes.append({
				'team_code': row[1].value,
				'number': row[2].value,
				'first_name': row[3].value,
				'last_name': row[4].value,
				'position': row[5].value,
				'height': row[6].value,
				'weight': row[7].value,
				'year': row[8].value
			})
		initial = False
		
	return athletes
	
def get_game_paths():
	concat_paths = lambda x: PATH_TO_COMPLETED_GAMES + '/' + x
	file_filter = lambda x: '~lock' not in x and '.xlsx' in x
	files = os.listdir(PATH_TO_COMPLETED_GAMES)
	files = filter(file_filter, files)
	files = map(concat_paths, files)
	return files
	
def get_team_hash():
	return {}
	
def get_athlete_hash():
	return {}
	
def write_to_json(game_dict, path):
	file = open(path,'w')
	file.write(json.dumps(game_dict))
	file.close()
	
def import_games_to_json():
	for game_path in get_game_paths():
		print(game_path)
		game_dict = read_game_file_xlsx(game_path)
		if game_dict != None:
			game_path = game_path.replace('excel','json')
			game_path = game_path.replace('.xlsx','.json')
			write_to_json(game_dict, game_path)		
			
def import_athletes_to_json():
	for game_path in get_game_paths():
		athlete_dict = read_rosters_xlsx(game_path)
		if athlete_dict != None:
			game_path = game_path.replace('completed_games', 'rosters')
			game_path = game_path.replace('excel','json')
			game_path = game_path.replace('.xlsx','.json')
			write_to_json(athlete_dict, game_path)

	
if __name__ == '__main__':
	import_athletes_to_json()