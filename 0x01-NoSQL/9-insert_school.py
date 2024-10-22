#!/usr/bin/env python3
"""Insert using pycode"""
from pymongo.collection import Collection


def insert_school(mongo_collection: Collection, **kwargs):
    """
    Insert to a collection function
    :return int
    """
    return mongo_collection.insert_one(kwargs).__inserted_id
