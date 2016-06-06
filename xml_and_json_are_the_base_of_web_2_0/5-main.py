import json
from car import Car
from xml.dom.minidom import Document

data = []
cars = []
brands = []
doors = 0
doc = Document()


with open('cars.json') as data_file:    
    data = json.load(data_file)

xml_cars = doc.createElement('cars')
doc.appendChild(xml_cars)

for car in data:
    cars.append(Car(car))

for car in cars:

    '''Creates a list of unique brands'''
    brand = car.get_brand()
    if not brand in brands:
        brands.append(brand)
        
    '''cumulative number of doors for all cars'''
    doors += car.get_nb_doors()

    '''Adds the car to the XML document'''
    car_xml = car.to_xml_node(doc)
    xml_cars.appendChild(car_xml)

    
'''Prints the number of brands, door count, the 4th car, and the XML doc'''
print len(brands)
print doors
print cars[3]
print doc.toxml(encoding='utf-8')


