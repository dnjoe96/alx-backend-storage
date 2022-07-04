#!/usr/bin/env python3

def update_topics(mongo_collection, name, topics):
    myquery = { "name": name }
    newvalues = { "$set": { "topics": topics } }

    mongo_collection.update_one(myquery, newvalues)
