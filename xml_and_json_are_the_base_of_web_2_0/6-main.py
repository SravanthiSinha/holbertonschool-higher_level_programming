import json
from car import Car

data = []
cars = []

with open('6-main.json') as data_file:    
    data = json.load(data_file)

for car in data:
    cars.append(Car(car).to_comma())

print "".join(cars)
    
