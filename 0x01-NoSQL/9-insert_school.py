#!/usr/bin/env python3
"""Insert using pycode"""
import pymongo.collection


def insert_school(
        mongo_collection: pymongo.collection.Collection,
        **kwargs):
    """Insert to a collection function"""
    document = mongo_collection.insert_one(kwargs)
    return document.inserted_id
