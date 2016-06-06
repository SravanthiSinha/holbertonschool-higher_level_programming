# -*- coding: utf-8

import json
from car import Car
from xml.dom.minidom import Document
import sys

'''Allows UTF-8 characters'''
reload(sys)
sys.setdefaultencoding('utf8')

data = []
cars = []
doc = Document()

with open('7-main.json') as data_file:    
    data = json.load(data_file)
    
xml_cars = doc.createElement('cars')
doc.appendChild(xml_cars)

for car in data:

    '''Adds the car to the XML document'''
    car_xml = Car(car).to_xml_node(doc)

    '''Add year element to the car xml'''
    year = doc.createElement('year')
    year_content = doc.createTextNode('2015')
    year.appendChild(year_content)
    car_xml.appendChild(year)

    '''Sets the weight attribute of the car'''
    car_xml.setAttribute('weight', '1000')
    
    '''Converts the brand element to a CDATA section with the © symbol added'''
    brand = car_xml.getElementsByTagName('brand')[0]
    new_brand = '©' + brand.childNodes[0].nodeValue
    brand_content = doc.createCDATASection(new_brand)
    brand.removeChild(brand.childNodes[0])
    brand.appendChild(brand_content)

    
    xml_cars.appendChild(car_xml)

print doc.toxml(encoding='utf-8')
