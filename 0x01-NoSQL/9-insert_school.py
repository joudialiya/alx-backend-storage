#!/usr/bin/env python3
"""Insert using pycode"""
from pymongo.collection import Collection
import typing


def insert_school(
        mongo_collection: Collection,
        **kwargs: typing.Dict[str, typing.Any]):
    """Intert function"""
    return mongo_collection.insert_one(kwargs).__inserted_id
