#!/usr/bin/env python3
"""Update using pycode"""


def update_topics(mongo_collection, name, topics):
    """Intert function"""
    mongo_collection.update_many(
        {'name': name},
        {"$set": {'topics': topics}}
        )
