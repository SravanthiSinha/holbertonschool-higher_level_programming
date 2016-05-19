import datetime
import json
import os.path

''' defines a Class Person and its attributes and methods'''
class Person():
    
    EYES_COLORS = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male"]

    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        
        if type(id) is not int:
            raise Exception("id is not an integer")
        if type(first_name) is not str:
            raise Exception("string is not a string")
        if (all(isinstance(item, int) for item in date_of_birth)) and (1<= date_of_birth[0] <= 12) and (1<= date_of_birth[1] <= 31) and (date_of_birth[2]>0) :
            pass
        else:
            raise Exception("date_of_birth is not a valid date")
        if (type(genre) is not str) or (genre not in self.GENRES):
            raise Exception("genre is not valid")
        if (type(eyes_color) is not str) or (eyes_color not in self.EYES_COLORS):
            raise Exception("eyes_color is not valid")
        
        self.__id = id
        self.__first_name = first_name
        self.__date_of_birth = date_of_birth
        self.__genre = genre;
        self.__eyes_color = eyes_color         

    def __str__(self):
        '''base class description) => return a string with first_name and last_name attached by a space '''
        return self.__first_name+" "+self.last_name

    def is_male(self):
        ''' return True if the person is a Male'''
        return True if self.__genre == "Male" else False

    def age(self):
        ''' return the current age (in year) based on date_of_birth and the date 05/20/2016 '''
        currentdate = datetime.date(2016,05,20)
        dobdate = datetime.date(self.__date_of_birth[2],self.__date_of_birth[0],self.__date_of_birth[1])
        return (currentdate-dobdate).days/365

    def __gt__(self,other):
        return self.age() > other.age()

    def __lt__(self, other):
        return self.age() < other.age()

    def __ge__(self, other):
        return self.age() >= other.age()
         
    def __le__(self, other):
        return self.age() <= other.age()

    def __eq__(self, other):
        return self.age() == other.age()
        
    def get_id(self):
        ''' Returns the id of the Person '''
        return self.__id
        
    def get_eyes_color(self):
        ''' Returns the eyes color of the Person '''
        return self.__eyes_color
    
    def get_genre(self):
        ''' Returns the genre of the Person '''
        return self.__genre

    def get_date_of_birth(self):
        ''' Returns the dob of the Person '''
        return self.__date_of_birth
        
    def get_first_name(self):
        ''' Returns the dob of the Person '''
        return self.__first_name

    def getname(self):
        return self.__class__.__name__


    def json(self):
        dict ={
            'first_name': self.__first_name,
            'last_name' :self.last_name,
            'id' : self.__id,
            'date_of_birth' : self.__date_of_birth,
            'genre' : self.__genre,
            'eyes_color' : self.__eyes_color,
            'is_married_to' :self.is_married_to
        }
        return dict

    def load_from_json(self,json):
        if type(json) is not dict:
            raise Exception("json is not valid")
        self.__first_name = json['first_name']
        self.last_name = json['lastname']
        self.__id = json['id']
        self.__date_of_birth = json['date_of_birth']
        self.__genre = json['genre']
        self.__eyes_color = json['eyes_color']
        self.is_married_to=json['is_married_to']
    
    ''' return True if the Class is Adult or Senior '''
    def can_be_married(self):
         return True if (self.getname()== 'Adult') or (self.getname()== 'Senior') else False 

    '''return True if is_married_to is different of 0'''
    def is_married(self):
        return True if self.is_married_to != 0 else False

    ''' will unlink 2 persons => assign is_married_to of each person to 0. Don't change the last_name, it's too late!'''
    def divorce(self, p):
        self.is_married_to == 0
        p.is_married_to == 0

    '''assign is_married_to with the id of the other person (assign both person by crossing id) and change the last_name of the '''
    def just_married_with(self, p):
        self.is_married_to = p.get_id()
        p.is_married_to=self.get_id()
        if(self.get_genre == 'Female'):
            self.last_name = p.last_name
        else:
            p.last_name = self.last_name

class Baby(Person):

    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        Person.__init__(self, id, first_name, date_of_birth, genre, eyes_color)
        self.is_married_to = 0

    '''return True if the Class is Teenager or Adult'''
    def can_run(self):
        return True if (self.getname()== 'Teenager') or (self.getname()== 'Adult') else False 

    '''return True if the Class is Baby or Senior'''
    def need_help(self):
         return True if (self.getname()== 'Baby') or (self.getname()== 'Senior') else False 


    '''return True if the Class is Baby or Teenager'''
    def is_young(self):
         return True if (self.getname()== 'Baby') or (self.getname()== 'Teenager') else False 


    '''return True if the Class is Adult or Senior'''
    def can_vote(self):
         return True if (self.getname()== 'Adult') or (self.getname()== 'Senior') else False 

    ''' return True if the Class is Adult or Senior '''
    def can_be_married(self):
         return True if (self.getname()== 'Adult') or (self.getname()== 'Senior') else False 

    '''return True if is_married_to is different of 0'''
    def is_married(self):
        return True if self.is_married_to != 0 else False

    ''' will unlink 2 persons => assign is_married_to of each person to 0. Don't change the last_name, it's too late!'''
    def divorce(self, p):
        self.is_married_to == 0
        p.is_married_to == 0

    '''assign is_married_to with the id of the other person (assign both person by crossing id) and change the last_name of the '''
    def just_married_with(self, p):
        self.is_married_to == p._id
        p.is_married_to=self.__id
        if(self.get_genre == 'Female'):
            self.last_name = p.last_name
        else:
            p.last_name = self.last_name



class Adult(Person):
    
    '''return True if the Class is Teenager or Adult'''
    def can_run(self):
        return True if (self.getname()== 'Teenager') or (self.getname()== 'Adult') else False 

    '''return True if the Class is Baby or Senior'''
    def need_help(self):
         return True if (self.getname()== 'Baby') or (self.getname()== 'Senior') else False 


    '''return True if the Class is Baby or Teenager'''
    def is_young(self):
         return True if (self.getname()== 'Baby') or (self.getname()== 'Teenager') else False 


    '''return True if the Class is Adult or Senior'''
    def can_vote(self):
         return True if (self.getname()== 'Adult') or (self.getname()== 'Senior') else False 


    ''' return True if the Class is Adult or Senior '''
    def can_be_married(self):
         return True if (self.getname()== 'Adult') or (self.getname()== 'Senior') else False 

    '''return True if is_married_to is different of 0'''
    def is_married(self):
        return True if self.is_married_to != 0 else False

    ''' will unlink 2 persons => assign is_married_to of each person to 0. Don't change the last_name, it's too late!'''
    def divorce(self, p):
        self.is_married_to == 0
        p.is_married_to == 0

    '''assign is_married_to with the id of the other person (assign both person by crossing id) and change the last_name of the '''
    def just_married_with(self, p):
        self.is_married_to == p._id
        p.is_married_to=self.__id
        if(self.get_genre == 'Female'):
            self.last_name = p.last_name
        else:
            p.last_name = self.last_name
    
    


class Teenager(Person):

    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        Person.__init__(self, id, first_name, date_of_birth, genre, eyes_color)
        self.is_married_to = 0

    
    '''return True if the Class is Teenager or Adult'''
    def can_run(self):
        return True if (self.getname()== 'Teenager') or (self.getname()== 'Adult') else False 

    '''return True if the Class is Baby or Senior'''
    def need_help(self):
         return True if (self.getname()== 'Baby') or (self.getname()== 'Senior') else False 


    '''return True if the Class is Baby or Teenager'''
    def is_young(self):
         return True if (self.getname()== 'Baby') or (self.getname()== 'Teenager') else False 


    '''return True if the Class is Adult or Senior'''
    def can_vote(self):
         return True if (self.getname()== 'Adult') or (self.getname()== 'Senior') else False 


    ''' return True if the Class is Adult or Senior '''
    def can_be_married(self):
         return True if (self.getname()== 'Adult') or (self.getname()== 'Senior') else False 

    '''return True if is_married_to is different of 0'''
    def is_married(self):
        return True if self.is_married_to != 0 else False

    ''' will unlink 2 persons => assign is_married_to of each person to 0. Don't change the last_name, it's too late!'''
    def divorce(self, p):
        self.is_married_to == 0
        p.is_married_to == 0

    '''assign is_married_to with the id of the other person (assign both person by crossing id) and change the last_name of the '''
    def just_married_with(self, p):
        self.is_married_to == p._id
        p.is_married_to=self.__id
        if(self.get_genre == 'Female'):
            self.last_name = p.last_name
        else:
            p.last_name = self.last_name
    

    
        
        

class Senior(Person):


    '''return True if the Class is Teenager or Adult'''
    def can_run(self):
        return True if (self.getname()== 'Teenager') or (self.getname()== 'Adult') else False 

    '''return True if the Class is Baby or Senior'''
    def need_help(self):
         return True if (self.getname()== 'Baby') or (self.getname()== 'Senior') else False 


    '''return True if the Class is Baby or Teenager'''
    def is_young(self):
         return True if (self.getname()== 'Baby') or (self.getname()== 'Teenager') else False 


    '''return True if the Class is Adult or Senior'''
    def can_vote(self):
         return True if (self.getname()== 'Adult') or (self.getname()== 'Senior') else False 

    ''' return True if the Class is Adult or Senior '''
    def can_be_married(self):
         return True if (self.getname()== 'Adult') or (self.getname()== 'Senior') else False 

    ''' return True if the Class is Adult or Senior '''
    def can_be_married(self):
         return True if (self.getname()== 'Adult') or (self.getname()== 'Senior') else False 

    '''return True if is_married_to is different of 0'''
    def is_married(self):
        return True if self.is_married_to != 0 else False

    ''' will unlink 2 persons => assign is_married_to of each person to 0. Don't change the last_name, it's too late!'''
    def divorce(self, p):
        self.is_married_to == 0
        p.is_married_to == 0

    '''assign is_married_to with the id of the other person (assign both person by crossing id) and change the last_name of the '''
    def just_married_with(self, p):
        self.is_married_to == p._id
        p.is_married_to=self.__id
        if(self.get_genre == 'Female'):
            self.last_name = p.last_name
        else:
            p.last_name = self.last_name
    

def save_to_file(list, filename):
    with open(filename,'w') as outfile:
        for person in list:
            outfile.write(json.dumps(person.json(),indent=2))


def load_from_file(filename):
    if type(filename) is not str or (not os.path.isfile(filename)) :
        Exception("filename is not valid or doesn't exist")
    else:
        with open(filename) as datafile:
            data = json.load(datafile)
            Persons = []
            for d in data["Persons"]:
                p = Person(0,'',[12,12,12],"Male","Blue")
                p.load_from_json(d)
                Persons.append(p)                
            return Persons

    

