#!/usr/bin/env python3
""" Module for schools_by_topic function """


def schools_by_topic(mongo_collection, topic):
    """ The function returns all schools that have a certain topic
    in their list of topics
    """
    all_schools = mongo_collection.find({"topics": topic})
    return all_schools
