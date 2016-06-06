import json

data = []
i = 1
f = open("1-json_read.txt","w")
with open('person.json') as data_file:    
    data = json.load(data_file)

'''
# How many phoneNumber items in this JSON file?
phonenumbers = data["phoneNumber"]
f.write(str(i)+") "+str(len(phonenumbers))+"\n")
'''

#What's the value of firstName
f.write(str(i)+ ") " + data["firstName"] + "\n")
i += 1

#What's the value of age?
f.write(str(i)+ ") " + str(data["age"]) + "\n")
i += 1

#What's the value of the postalCode of the addres
f.write(str(i)+ ") " + str(data["address"]["postalCode"]) + "\n")
i += 1

#How many unique keys are used for defining a phoneNumber?
f.write(str(i)+ ") " + str(len(list(set(data["phoneNumber"][0].keys())))) + "\n")
i += 1


#How many unique keys are used for defining the full JSON?
def getKeys(data):
    if type(data) is dict:
        return data.keys() 
    else:
        return 1

f.write(str(i)+ ") " + str(len(list(set(getKeys(data))))) + "\n")
i += 1

# What's the value of the type of first phoneNumber?
f.write(str(i)+ ") " + str(data["phoneNumber"][0]["type"]) + "\n")
i += 1

f.close()
