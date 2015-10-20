from models import Athlete, Team, Game, Play, Collaboration, Action, Observation, db

PATH_TO_TEAM_CODES = 'data/team_codes.txt'

def create_team_records():
	file = open(PATH_TO_TEAM_CODES, 'r')
	teams = []
	while True:
		try:
			name = file.readline()
			code = file.readline()
			if code == '':
				break
			teams.append({
				'name': name,
				'code': code
			})
		except Exception:
			break
	file.close()
	print("got this far")	
	with db.atomic():
		Team.insert_many(teams)
		
	
	
	
if __name__ == '__main__':
	create_team_records()