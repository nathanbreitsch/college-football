from models import Athlete, Team, Game, Play, Collaboration, Action, Observation, db

PATH_TO_TEAM_CODES = 'data/team_codes.txt'

def create_team_records():
	file = open(PATH_TO_TEAM_CODES, 'r')
	with db.atomic():
		while True:
			try:
				name = file.readline()
				code = file.readline()
			except Exception:
				break
				
			team = Team.create(
				name = name,
				code = code
			)
	file.close()
	
	
if __name__ == '__main__':
	create_team_records()