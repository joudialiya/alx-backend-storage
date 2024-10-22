#!/usr/bin/env python3
"""Select avg"""
import pymongo.collection


def top_students(mongo_collection: pymongo.collection.Collection):
    """Logic function"""
    return mongo_collection.aggregate(
        [
            {
                '$set': {
                    'averageScore': {'$avg': '$topics.score'}
                }
            },
            {
                '$sort': {
                    'averageScore': -1
                }
            }
        ]
    )
