'''Defines class Car attributes and methods'''
class Car:
    
    def __init__(self, *args, **kwargs):

        '''Checks for named values in keyword arguments'''
        if 'name' in kwargs:
            name = kwargs.pop('name')
        if 'brand' in kwargs:
            brand = kwargs.pop('brand')
        if 'nb_doors' in kwargs:
            nb_doors = kwargs.pop('nb_doors')
        
        '''Checks for invalid data'''

        if name == None or not isinstance(name, str) or name == "":
            raise Exception("name is not a string")
        elif brand == None or not isinstance(brand, str) or brand == "":
            raise Exception("brand is not a string")
        elif nb_doors == None or not isinstance(nb_doors, int) or nb_doors <= 0:
            raise Exception("nb_doors is not > 0")

        '''Sets private attributes for the class'''
        self.__name = name
        self.__brand = brand
        self.__nb_doors = nb_doors
    

    '''Returns the name of the car'''
    def get_name(self):
        return self.__name

    '''Returns the brand of the car'''
    def get_brand(self):
        return self.__brand

    '''Returns the number of doors on the car'''
    def get_nb_doors(self):
        return self.__nb_doors

        '''Converts the private attributes to a hash'''
    def to_hash(self):
        return  {
            'nb_doors': self.__nb_doors,
            'brand': self.__brand,
            'name': self.__name
        }

    '''Responds to __str__ call with defined string'''
    def __str__(self):
        return self.__name + " " + self.__brand + " (" + str(self.__nb_doors) + ")"

