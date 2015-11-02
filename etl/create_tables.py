from models import db, Athlete, Team, Game, Play, Collaboration, Action, Observation

def create_tables():
	db.connect()
	db.create_tables([Athlete, Team, Game, Play, Collaboration, Action, Observation])
	db.close()
	
def drop_tables():
	db.connect()
	db.drop_tables([Athlete, Team, Game, Play, Collaboration, Action, Observation]);
	db.close()
	
if __name__ == '__main__':
	drop_tables()
	create_tables()