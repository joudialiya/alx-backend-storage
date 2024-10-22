#!/usr/bin/env python3
"""Insert using pycode"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert to a collection function
    :return int
    """
    return mongo_collection.insert_one(kwargs).__inserted_id
