import datetime
import json
import os.path

''' defines a Class Person and its attributes and methods'''
class Person():
    
    EYES_COLORS = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male"]

    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        
        if type(id) is not int or id < 0:
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
        self.children = []
        self.last_name=''
        self.is_married_to = 0
        
    def __str__(self):
        '''base class description) => return a string with first_name and last_name attached by a space '''
        return str(self.__first_name)+" "+str(self.last_name)

    def __iter__(self):
        '''base class description) => return a string with first_name and last_name attached by a space '''
        return str(self.__first_name)+" "+str(self.last_name)
 
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
            'is_married_to' :self.is_married_to,
            'kind':self.getname(),
            'children' : self.children
        }
        return dict

    def load_from_json(self,json):
        if type(json) is not dict:
            raise Exception("json is not valid")
        self.kind = str(json['kind'])
        self.__first_name = str(json['first_name'])
        self.last_name = str(json['last_name'])
        self.__id = json['id']
        self.__date_of_birth = json['date_of_birth']
        self.__genre = str(json['genre'])
        self.__eyes_color = str(json['eyes_color'])
        self.is_married_to=json['is_married_to']
        self.children =json['children']

class Baby(Person):

    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        Person.__init__(self, id, first_name, date_of_birth, genre, eyes_color)
        
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
        self.is_married_to = 0
        p.is_married_to = 0


    '''assign is_married_to with the id of the other person (assign both person by crossing id) and change the last_name of the '''
    def just_married_with(self, p):
        if (self.is_married_to != 0)  or (p.is_married_to !=0):
            raise Exception("Already married")           
        if((not self.can_be_married()) or  (not p.can_be_married())):
            raise Exception("Can't be married")
        self.is_married_to = p.get_id()
        p.is_married_to=self.get_id()
        if(self.get_genre == 'Female'):
            self.last_name = p.last_name
        else:
            p.last_name = self.last_name

    '''return True if the Class is Adult '''
    def can_have_child(self):
        return True if (self.getname()== 'Adult') else False

    ''' return a Baby object and add to children the new id on self and p'''
    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color = ''):
        if (p is None) or ((p.kind != 'Adult') and (p.kind !='Senior')):
            raise Exception("p is not an Adult of Senior")
        if (not p.can_have_child()) or(not self.can_have_child()):
            raise Exception("Can't have baby")        
        if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Blue' :
            eyes_color = 'Blue'
        if self.get_eyes_color() == 'Green' and p.get_eyes_color() == 'Green' :
            eyes_color = 'Green'
        if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Green' :
            eyes_color = 'Blue'
        if p.get_eyes_color() == 'Brown' :
            eyes_color = 'Brown'
        b = Baby(id,first_name,date_of_birth,genre,eyes_color)
        if id not in p.children:
            p.children.append(id)
        if id not in self.children:
            self.children.append(id)        
        return b

    '''link 2 persons by adding c.get_id() to self.children'''
    def adopt_child(self, c):
       if (not self.can_have_child()):
            raise Exception("Can't adopt child")
       self.children.append(c.get_id())


    '''Search in list_person (list of Person) parents of self => return a list of Person'''
    def who_are_my_parents(self, list_person):
        parents = []
        parentsid= []
        if not isinstance(list_person, list):
            raise Exception("list_person is not valid")
        for person in list_person:
            if person.getname() == 'Person':
                raise Exception("list_person is not valid")
            else:
                if self.get_id() in person.children:
                    if id(person) not in parentsid:
                        parents.append(person)
                        parentsid.append(id(person))
        return parents

    '''Search in list_person (list of Person) grandparents of self => return a list of Person'''
    def who_are_my_grand_parents(self, list_person):
        grandparents = []
        parents = []
        grandparentsid = []
        if not isinstance(list_person, list):
            raise Exception("list_person is not valid")
        parents = self.who_are_my_parents(list_person)
        for person in list_person:
            if person.getname() == 'Person':
                raise Exception("list_person is not valid")
            else:
                for parent in parents:
                    for x in parent.who_are_my_parents(list_person):
                        if id(x) not in grandparentsid:
                            grandparents.append(x)
                            grandparentsid.append(id(x))
        return grandparents
        

class Adult(Person):

    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        Person.__init__(self, id, first_name, date_of_birth, genre, eyes_color)
        

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
        self.is_married_to = 0
        p.is_married_to = 0

    '''assign is_married_to with the id of the other person (assign both person by crossing id) and change the last_name of the '''
    def just_married_with(self, p):
        if (self.is_married_to != 0)  or (p.is_married_to !=0):
            raise Exception("Already married")           
        if((not self.can_be_married()) or  (not p.can_be_married())):
            raise Exception("Can't be married")
        self.is_married_to = p.get_id()
        p.is_married_to = self.get_id()
        if(self.get_genre == 'Female'):
            self.last_name = p.last_name
        else:
            p.last_name = self.last_name

    '''return True if the Class is Adult '''
    def can_have_child(self):
        return True if (self.getname()== 'Adult') else False

    ''' return a Baby object and add to children the new id on self and p'''
    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color = ''):
        if (p is None) or ((p.kind != 'Adult') and (p.kind !='Senior')):
            raise Exception("p is not an Adult of Senior")
        if (not p.can_have_child()) or(not self.can_have_child()):
            raise Exception("Can't have baby")        
        if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Blue' :
            eyes_color = 'Blue'
        if self.get_eyes_color() == 'Green' and p.get_eyes_color() == 'Green' :
            eyes_color = 'Green'
        if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Green' :
            eyes_color = 'Blue'
        if p.get_eyes_color() == 'Brown' :
            eyes_color = 'Brown'

        b = Baby(id,first_name,date_of_birth,genre,eyes_color)
        if id not in p.children:
            p.children.append(id)
        if id not in self.children:
            self.children.append(id)        
        return b

 
    '''link 2 persons by adding c.get_id() to self.children'''
    def adopt_child(self, c):
       if (not self.can_have_child()):
            raise Exception("Can't adopt child")
       self.children.append(c.get_id())


    '''Search in list_person (list of Person) parents of self => return a list of Person'''
    def who_are_my_parents(self, list_person):
        parents = []
        parentsid= []
        if not isinstance(list_person, list):
            raise Exception("list_person is not valid")
        for person in list_person:
            if person.getname() == 'Person':
                raise Exception("list_person is not valid")
            else:
                if self.get_id() in person.children:
                    if id(person) not in parentsid:
                        parents.append(person)
                        parentsid.append(id(person))
        return parents

    '''Search in list_person (list of Person) grandparents of self => return a list of Person'''
    def who_are_my_grand_parents(self, list_person):
        grandparents = []
        parents = []
        grandparentsid = []
        if not isinstance(list_person, list):
            raise Exception("list_person is not valid")
        parents = self.who_are_my_parents(list_person)
        for person in list_person:
            if person.getname() == 'Person':
                raise Exception("list_person is not valid")
            else:
                for parent in parents:
                    for x in parent.who_are_my_parents(list_person):
                        if id(x) not in grandparentsid:
                            grandparents.append(x)
                            grandparentsid.append(id(x))
        return grandparents

class Teenager(Person):

    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        Person.__init__(self, id, first_name, date_of_birth, genre, eyes_color)
        
    
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
        self.is_married_to = 0
        p.is_married_to = 0


    '''assign is_married_to with the id of the other person (assign both person by crossing id) and change the last_name of the '''
    def just_married_with(self, p):
        if (self.is_married_to != 0)  or (p.is_married_to !=0):
            raise Exception("Already married")           
        if(not(self.can_be_married()) or (not  p.can_be_married())):
            raise Exception("Can't be married")
        self.is_married_to = p.get_id()
        p.is_married_to = self.get_id()
        if(self.get_genre == 'Female'):
            self.last_name = p.last_name
        else:
            p.last_name = self.last_name

    '''return True if the Class is Adult '''
    def can_have_child(self):
        return True if (self.getname()== 'Adult') else False

    ''' return a Baby object and add to children the new id on self and p'''
    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color = ''):
        if (p is None) or ((p.kind != 'Adult') and (p.kind !='Senior')):
            raise Exception("p is not an Adult of Senior")
        if (not p.can_have_child()) or(not self.can_have_child()):
            raise Exception("Can't have baby")        
        if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Blue' :
            eyes_color = 'Blue'
        if self.get_eyes_color() == 'Green' and p.get_eyes_color() == 'Green' :
            eyes_color = 'Green'
        if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Green' :
            eyes_color = 'Blue'
        if p.get_eyes_color() == 'Brown' :
            eyes_color = 'Brown'
        b = Baby(id,first_name,date_of_birth,genre,eyes_color)
        if id not in p.children:
            p.children.append(id)
        if id not in self.children:
            self.children.append(id)        
        return b

 
    '''link 2 persons by adding c.get_id() to self.children'''
    def adopt_child(self, c):
       if (not self.can_have_child()):
            raise Exception("Can't adopt child")
       self.children.append(c.get_id())


    '''Search in list_person (list of Person) parents of self => return a list of Person'''
    def who_are_my_parents(self, list_person):
        parents = []
        parentsid= []
        if not isinstance(list_person, list):
            raise Exception("list_person is not valid")
        for person in list_person:
            if person.getname() == 'Person':
                raise Exception("list_person is not valid")
            else:
                if self.get_id() in person.children:
                    if id(person) not in parentsid:
                        parents.append(person)
                        parentsid.append(id(person))
        return parents

    '''Search in list_person (list of Person) grandparents of self => return a list of Person'''
    def who_are_my_grand_parents(self, list_person):
        grandparents = []
        parents = []
        grandparentsid = []
        if not isinstance(list_person, list):
            raise Exception("list_person is not valid")
        parents = self.who_are_my_parents(list_person)
        for person in list_person:
            if person.getname() == 'Person':
                raise Exception("list_person is not valid")
            else:
                for parent in parents:
                    for x in parent.who_are_my_parents(list_person):
                        if id(x) not in grandparentsid:
                            grandparents.append(x)
                            grandparentsid.append(id(x))
        return grandparents


class Senior(Person):

    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        Person.__init__(self, id, first_name, date_of_birth, genre, eyes_color)
       
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

    ''' return True if the Class is Adult or Senior '''
    def can_be_married(self):
         return True if (self.getname()== 'Adult') or (self.getname()== 'Senior') else False 

    '''return True if is_married_to is different of 0'''
    def is_married(self):
        return True if self.is_married_to != 0 else False

    ''' will unlink 2 persons => assign is_married_to of each person to 0. Don't change the last_name, it's too late!'''
    def divorce(self, p):
        self.is_married_to = 0
        p.is_married_to = 0

    '''assign is_married_to with the id of the other person (assign both person by crossing id) and change the last_name of the '''
    def just_married_with(self, p):
        if (self.is_married_to != 0)  or (p.is_married_to !=0):
            raise Exception("Already married")           
        if(not self.can_be_married()) or  (not p.can_be_married()):
            raise Exception("Can't be married")
        self.is_married_to = p.get_id()
        p.is_married_to = self.get_id()
        if(self.get_genre == 'Female'):
            self.last_name = p.last_name
        else:
            p.last_name = self.last_name

    '''return True if the Class is Adult '''
    def can_have_child(self):
        return True if (self.getname()== 'Adult') else False

    ''' return a Baby object and add to children the new id on self and p'''
    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color = ''):
        if (p is None) or ((p.kind != 'Adult') and (p.kind !='Senior')):
            raise Exception("p is not an Adult of Senior")
        if (not p.can_have_child()) or(not self.can_have_child()):
            raise Exception("Can't have baby")        
        if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Blue' :
            eyes_color = 'Blue'
        if self.get_eyes_color() == 'Green' and p.get_eyes_color() == 'Green' :
            eyes_color = 'Green'
        if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Green' :
            eyes_color = 'Blue'
        if p.get_eyes_color() == 'Brown' :
            eyes_color = 'Brown'
        b = Baby(id,first_name,date_of_birth,genre,eyes_color)
        if id not in p.children:
            p.children.append(id)
        if id not in self.children:
            self.children.append(id)        
        return b

    '''link 2 persons by adding c.get_id() to self.children'''
    def adopt_child(self, c):
       if (not self.can_have_child()):
            raise Exception("Can't adopt child")
       self.children.append(c.get_id())


    def who_are_my_grandchildren(self, list_person):
        if not isinstance(list_person, list):
            raise Exception("list_person is not valid")
        children = self.children
        grandchildrenids= []
        grandchildren = []
        for child in children:
            for person in list_person:
                if person.get_id() == child:
                    for c in person.children:
                        grandchildrenids.append(c)

        for id in grandchildrenids:
            for person in list_person:
                if person.get_id() == id:
                    grandchildren.append(person)
                
        return grandchildren

def save_to_file(list, filename):
    with open(filename,'w') as outfile:
        list_of_jsonstrings = []
        for person in list:
            list_of_jsonstrings.append(person.json())
        outfile.write(json.dumps(list_of_jsonstrings,indent=2))


def load_from_file(filename):
    if type(filename) is not str or (not os.path.isfile(filename)) :
        Exception("filename is not valid or doesn't exist")
    else:
        with open(filename) as datafile:
            Persons = []
            if os.stat(filename).st_size != 0:
                data = json.load(datafile)
                for d in data:
                    if d['kind'] == 'Adult':
                        p = Adult(0,'',[12,12,12],"Male","Blue")
                    if d['kind'] == 'Baby':
                        p = Baby(0,'',[12,12,12],"Male","Blue")
                    if d['kind'] == 'Senior':
                        p = Senior(0,'',[12,12,12],"Male","Blue")
                    if d['kind'] == 'Teenager':
                        p = Teenager(0,'',[12,12,12],"Male","Blue")                
                    p.load_from_json(d)
                    Persons.append(p)                
            return Persons
