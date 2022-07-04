#!/usr/bin/env python3

def insert_school(mongo_collection, **kwargs):
    value = mongo_collection.insert_one(kwargs)
    return value.inserted_id
