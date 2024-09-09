#!/usr/bin/env python3
''' Updating a document in a collection '''


def update_topics(mongo_collection, name, topics):
    ''' Changes all topics of a school document based on the name '''
    query = {'name': name}
    values = { '$set': {'topics': topics}}
    mongo_collection.update_many(query, values)
