#!/usr/bin/env python3
''' Interacts with the mongoDb database '''


def schools_by_topic(mongo_collection, topic):
    ''' Returns a list of school having a specific topic '''
    return list(mongo_collection.find({'topics': topic}))
