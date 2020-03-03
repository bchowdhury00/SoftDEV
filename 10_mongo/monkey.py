from pymongo import MongoClient 
from bson.json_util import loads
import pprint
client = MongoClient('localhost',27017)
db = client['database']
prizes = db['prizes']

def fillCollection():
    f = open("primer-dataset.json",'r')
    data = f.readlines()
    print(data[0])
    print(type(loads(data[0])))
    for i in range(len(data)):
        prizes.insert_one(loads(data[i]))
    return
