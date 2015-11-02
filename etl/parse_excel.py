import openpyxl as pyxl
import os
import json

PATH_TO_COMPLETED_GAMES = 'data/completed_games/excel'
PATH_TO_TEAM_CODES = 'data/team_codes.txt'

#schema: section_name -> { column_name - > [values] }
def read_game_file_xlsx(path):
	ws = get_ws(path)
	return extract_game_dict(ws)


def get_ws(path):
	wb = pyxl.load_workbook(filename = path)
	if 'Data' in wb.get_sheet_names():
		ws = wb.get_sheet_by_name('Import')
		return ws
	else:
		print("the following file does not have an Import tab: " + path)
		return None



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

def get_table_structure(ws):
	#first make dict col_index -> section,column
	col_names = []
	for col in ws.columns:
		if col[0].value not in ["", None, " "]:
			section_name = col[0].value
		column_name = col[1].value
		if column_name in ['', ' ', None]:
			break
		col_names.append((section_name, column_name))

	return col_names

def initialize_game_dict(col_names):
	game_dict = {}
	for section_name, column_name in col_names:
		if section_name not in game_dict:
			game_dict[section_name] = {}
		if column_name not in game_dict[section_name]:
			game_dict[section_name][column_name] = []

	return game_dict


def extract_game_dict(ws):
	table_structure = get_table_structure(ws)
	game_dict = initialize_game_dict(table_structure)

	#next, loop through rows and build game_dict
	row_index = 0
	for row in ws.rows:
		row_index += 1
		if row_index > 2: #i dont know how to subset a generator :(
			play_number = row[0].value
			if play_number in ["", " ", None]: #leave when play_numbers become nonsense
				break
			col_index = 0
			for col in row:
				if col_index >= len(table_structure):
					break
				(section_name, column_name) = table_structure[col_index]
				col_index += 1
				game_dict[section_name][column_name].append(col.value)

	return game_dict

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
	file.write(json.dumps(game_dict, sort_keys=True, indent=4, separators=(',', ': ')))
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
	#game_dict = read_game_file_xlsx("data/completed_games/excel/090315 TCU Minnesota - Final.xlsx")
	#json.dumps(game_dict)
	#write_to_json(game_dict, "data/test.json")
	#import_athletes_to_json()
	import_games_to_json()
