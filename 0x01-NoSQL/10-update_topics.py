#!/usr/bin/env python3
"""Update using pycode"""
from pymongo.collection import Collection


def update_topics(mongo_collection: Collection, name, topics):
    """Intert function"""
    mongo_collection.update_one({name}, {"$eq": {topics}})
