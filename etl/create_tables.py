from models import db, Athlete, Team, Game, Play, Collaboration, Action, Observation

def create_tables():
	db.connect()
	db.create_tables([Athlete, Team, Game, Play, Collaboration, Action, Observation])
	
if __name__ == '__main__':
	create_tables()