import peewee
from playhouse.fields import ManyToManyField

db =  peewee.SqliteDatabase(None, threadlocals=True)
class BaseModel(peewee.Model):
    id = peewee.PrimaryKeyField(unique=True)
    database = db
    class Meta:
        database = db
        order_by = ('id', )
        
class FilmModel(BaseModel):
    title = peewee.CharField(128,null=False)
    release_date = peewee.CharField(128,null=False)
    episode_id = peewee.IntegerField(null=False)

class PeopleModel(BaseModel):
    name = peewee.CharField(128,null=False)
    films = ManyToManyField(rel_model=FilmModel,related_name="characters")
    
class PlanetModel(BaseModel):
    name = peewee.CharField(128,null=False)
    climate = peewee.CharField(128,null=False)
    residents = ManyToManyField(rel_model=PeopleModel,related_name="homeworld")
    films = ManyToManyField(rel_model=FilmModel,related_name="planets")

FilmPeople = PeopleModel.films.get_through_model()
FilmPlanet = PlanetModel.films.get_through_model()
PeoplePlanet = PlanetModel.residents.get_through_model()
    

