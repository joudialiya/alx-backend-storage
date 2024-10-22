#!/usr/bin/env python3
"""Insert using pycode"""
from pymongo.collection import Collection


def insert_school(mongo_collection: Collection, **kwargs):
    """Intert function"""
    return mongo_collection.insert_one(kwargs).__inserted_id
