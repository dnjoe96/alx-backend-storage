#!/usr/bin/env python3

def schools_by_topic(mongo_collection, topic):
    all_schools = mongo_collection.find({"topics": topic})
    return all_schools
