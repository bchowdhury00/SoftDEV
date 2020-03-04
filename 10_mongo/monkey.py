# Team quacks - Tammy Chen & Biraj Chowdhury
# SoftDev pd9
# K10: Import/Export Bank
# 2020-03-04

'''
The dataset contains all nobel prize winners & their research. It includes information such as the year & category of the award. 
LINK: http://api.nobelprize.org/v1/prize.json
For our import mechanism, we read the dataset into a list and then used the imported json library to convert the dataset into a dictionary, which is then inserted into the database. We also imported pprint, which makes the information easier to read when printed.  
'''

import pprint, json 
from json import loads
from pymongo import MongoClient

client  = MongoClient()  # sets up clients
db = client.test # sets up database
nobel = db.nobel # nobel database

f = open("nobel.json")
data = json.load(f)
nobel.insert_many(data["prizes"])

'''
# reading json file into database
if (nobel.count() == 0):
    file = open("nobel.json", "r")
    content = file.readlines()
    for line in content:
        nobel.insert_one(loads(line))
'''

def findCategory(category):
    output = []
    for i in nobel.find({"category" : category}):
        output.append(i)
    return pprint.pprint(output)
    #return output
    #print("Hello World")
    #pprint.pprint(nobel.result)
    #for i in history.result.find({"event.date": date}):
    #    pprint.pprint(i)
    #    print("hello")

def findYear(year):
    output = []
    for i in nobel.find({"year" : year}):
        output.append(i)
    return pprint.pprint(output)
    #print("Hello World")

def findFirstName(fName):
    output  = []
    for i in nobel.find({"laureates.firstname" : fName}):
        output.append(i)
    return pprint.pprint(output)
    #print("Hello World")

def findLastName(lName):
    output = []
    for i in nobel.find({"laureates.surname" : lName}):
        output.append(i)
    return pprint.pprint(output)
    #print("Hello World")

#print(findCategory("chemistry"))
#print(findYear("2018"))
#print(findFirstName("John"))
print(findLastName("Obama"))
