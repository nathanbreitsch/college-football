from peewee import *
db = SqliteDatabase('cfbfilmroom.db')

class BaseModel(Model):
	class Meta:
		database = db
		
class Team(BaseModel):
	name = CharField()
	code = CharField()

class Athlete(BaseModel):
	first_name = CharField()
	last_name = CharField()
	team = ForeignKeyField(Team)
	
class Game(BaseModel):
	team_1 = ForeignKeyField(Team, related_name='is_team_1')
	team_2 = ForeignKeyField(Team, related_name='is_team_2')
	path = CharField()
	
class Play(BaseModel):
	game = ForeignKeyField(Game)
	offense = ForeignKeyField(Team, related_name='is_offense')
	defense = ForeignKeyField(Team, related_name='is_defense')
	index = IntegerField()
	quarter = IntegerField()
	down = IntegerField()
	half = CharField()
	yards_to_go = IntegerField()
	yards_line = IntegerField()
	result = CharField()

class Collaboration(BaseModel):
	play = ForeignKeyField(Play)
	
class Action(BaseModel):
	collaboration = ForeignKeyField(Collaboration)
	athlete = ForeignKeyField(Athlete)
	
class Observation(BaseModel):
	action = ForeignKeyField(Action)
	name = CharField()
	vaule = CharField()
	
