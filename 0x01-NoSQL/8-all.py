#!/usr/bin/env python3
"""List from Mongo db server"""\

import pymongo
import pymongo.collection


def list_all(mongo_collection: pymongo.collection.Collection):
  return [element for element in mongo_collection.find()]