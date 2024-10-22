#!/usr/bin/env python3
"""Select on topic"""


def schools_by_topic(mongo_collection, topic):
    return [school for school in
            mongo_collection.find({'topics': {'$all': [topic]}})]
