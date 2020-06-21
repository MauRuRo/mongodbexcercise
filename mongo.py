import pymongo
import os

from os import path
if path.exists("env.py"):
    import env

MONGODB_URI = os.environ.get("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not cnnect to MongoDB: %s") % e


conn = mongo_connect(MONGODB_URI)


coll = conn[DBS_NAME][COLLECTION_NAME]

# new_docs = [{'first': 'terry', 'last': 'pratchett', 'dob':'11/03/1952', 'hair_colour':'grey', 'occupation': 'writer', 'nationality': 'english'},
#             {'first': 'george', 'last': 'martin', 'dob':'11/03/1952', 'hair_colour':'grey', 'occupation': 'writer', 'nationality': 'american'}]

# coll.insert_many(new_docs)

coll.update_many({'nationality':'american'}, {'$set':{'hair_colour':'maroon'}})

documents = coll.find({'nationality':'american'})

for doc in documents:
    print(doc)
