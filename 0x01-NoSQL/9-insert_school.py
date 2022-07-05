#!/usr/bin/env python3
""" Module for insert_school function """


def insert_school(mongo_collection, **kwargs):
    """ The function inserts new entry into a collection and returns
        the id of the document
    """
    value = mongo_collection.insert_one(kwargs)
    return value.inserted_id
