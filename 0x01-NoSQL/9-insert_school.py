#!/usr/bin/env python3
""" Implements a functio that delas with Mongo Db """


def insert_school(mongo_collection, **kwargs):
    '''
    inserts a new document in a collection based on kwargs
    '''
    x = mongo_collection.insert_one(kwargs)
    return x.inserted_id
