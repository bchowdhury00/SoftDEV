
from pymongo import MongoClient 
from bson.json_util import loads
import pprint
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

pprint.pprint(restaurants.find_one({"borough" : "Queens"}))
pprint.pprint(restaurants.find_one({"address.zipcode":"11377"}))
c = restaurants.count_documents({"grades.score": { "$gt" : 80}})
cur = restaurants.find({"grades.score" : {"$gt" : 80}})
print(c)
print("\n\n\nRestaurants To Not Go To\n\n\n")
for col in cur:
    print("\n")
    pprint.pprint(col)
