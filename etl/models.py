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
	number = CharField()
	year = CharField(null = True)
	position = CharField(null = True)
	height = CharField(null = True)
	weight = CharField(null = True)
	
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
	down = IntegerField(null = True)
	half = CharField(null = True)
	yards_to_go = IntegerField(null = True)
	yards_line = IntegerField(null = True)
	result = CharField(null = True)

class Collaboration(BaseModel):
	play = ForeignKeyField(Play)
	index = IntegerField()
	
class Action(BaseModel):
	collaboration = ForeignKeyField(Collaboration)
	athlete = ForeignKeyField(Athlete)
	action_type = CharField()
	
class Observation(BaseModel):
	action = ForeignKeyField(Action)
	name = CharField()
	value = CharField(null = True)
	
