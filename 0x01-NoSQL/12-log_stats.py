#!/usr/bin/env python3
"""Get Logs"""
import pymongo
import pymongo.collection


client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
nginx_collection = client.logs.nginx
print('{:d} logs'.format(nginx_collection.count_documents({})))
for method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
    print('\tmethod {}: {}'.format(
        method,
        nginx_collection.count_documents({'method': method})))
