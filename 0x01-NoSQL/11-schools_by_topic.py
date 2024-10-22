#!/usr/bin/env python3
"""Select on topic"""

from pymongo.collection import Collection


def schools_by_topic(mongo_collection: Collection, topic):
    return [school for school in
            mongo_collection.find({'topics': {'$all': [topic]}})]
