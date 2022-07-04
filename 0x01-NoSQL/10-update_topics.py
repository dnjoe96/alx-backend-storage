#!/usr/bin/env python3
""" Module for update_topics function """


def update_topics(mongo_collection, name, topics):
    """ The function updates a document in a collection with
    a list of topics
    """
    myquery = {"nae": name}
    newvalues = {"$set": {"topics": topics}}

    mongo_collection.update_one(myquery, newvalues)
