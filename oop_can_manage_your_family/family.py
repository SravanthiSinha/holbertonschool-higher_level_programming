import datetime

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


'''Getter of id, eyes_color, genre, date_of_birth, first_name'''
        
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



    

