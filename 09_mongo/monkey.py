
from pymongo import MongoClient 
from bson.json_util import loads
client = MongoClient('localhost',27017)
db = client['database']
restaurants = db['restaurants']

def fillCollection():
    f = open("primer-dataset.json",'r')
    data = f.readlines()
    print(data[0])
    print(type(loads(data[0])))
    for i in range(len(data)):
        restaurants.insert_one(loads(data[i]))
    return
fillCollection()    
 
