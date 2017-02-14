import peewee
import json
import threading 
import requests
from h_swapi_models import FilmModel, PeopleModel,PlanetModel,BaseModel,FilmPeople,FilmPlanet,PeoplePlanet

from playhouse.shortcuts import *
from threading import Thread

characters = set()
planets = set()
fthreads = []
cthreads = []
pthreads = []

class mThread(Thread):

    def __init__(self, modelname,url,fid=None,pid=None):
        self.pid = pid
        self.fid = fid
        self.url = url
        self.modelname = modelname
        Thread.__init__(self)
        self.__stop = threading.Event()

    def stop(self):
        self.__stop.set()
                       
    def __get_json(self,url):
        req = requests.get(self.url)
        return req.json()

    def is_json(self,myjson):
          try:
              json_object = json.loads(myjson)
          except ValueError, e:
              return False
          return True
      
    def run(self):
        global characters,planets
        data = self.__get_json(self.url)
        if self.modelname == 'film':
            model = FilmModel.create(id=self.fid,title=data['title'], release_date=data['release_date'],episode_id = int(data['episode_id']))
            characters.update(data['characters'])
            planets.update(data['planets'])
        elif self.modelname == 'people':
            model = PeopleModel.create(id=self.pid,name=data['name'])
            films = data['films']
            for film in films:
                fid = film.split("/")[-2]
                model.films.add(fid)
        elif self.modelname == 'planet':
            model = PlanetModel.create(name=data['name'],climate=data['climate'])
            films = data['films']
            people =data['residents']
            for film in films:
                fid = film.split("/")[-2]
                model.films.add(fid)
            for p in people:
                pid = p.split("/")[-2]
                model.residents.add(pid)
        model.save()
        
class SWAPI:
    
    def __init__(self, database_name):
        self.__database_name = database_name

    def stop(self):
        global fthreads,cthreads,pthreads
        for t in fthreads:
            t.stop()
        for t in cthreads:
            t.stop()
        for t in pthreads:
            t.stop()
        BaseModel.database.close()
        
    def is_done(self):
        global fthreads,cthreads,pthreads
        for t in fthreads:
            if t.isAlive():
                return False
        for t in cthreads:
            if t.isAlive():
                return False
        for t in pthreads:
            if t.isAlive():
                return False
        return True

    def __create_tables(self):
        BaseModel.database.create_tables([FilmModel, PeopleModel,PlanetModel,FilmPlanet,FilmPeople,PeoplePlanet])
        
    
    def __fetch_films(self):
        global fthreads
        for x in range(1,8):
            t = mThread("film","http://swapi.co/api/films/"+str(x),x)
            t.start()
            fthreads +=[t]
        for t in fthreads:
            t.join()
            
    def __fetch_planets(self):
        global pthreads
        for planeturl in set(planets):
            pid = planeturl.split('/')[5]
            if not PlanetModel.select().where(PlanetModel.id == pid).exists():
                t = mThread("planet",planeturl,1,planeturl.split('/')[5])
                t.start()
                pthreads += [t]
        for t in pthreads:
            t.join()
            
    def __fetch_people(self):
        global cthreads
        for peopleurl in set(characters):
            pid = peopleurl.split('/')[5]
            if not PeopleModel.select().where(PeopleModel.id==pid).exists():
                t = mThread("people",peopleurl,1,peopleurl.split('/')[5])
                t.start()
                cthreads += [t]
        for t in cthreads:
            t.join()


    def start(self):
        global fthreads,cthreads,pthreads
        BaseModel.database.init(self.__database_name)
        BaseModel.database.connect()
        self.__create_tables()
        self.__fetch_films()
        self.__fetch_people()
        self.__fetch_planets()
        BaseModel.database.close()
