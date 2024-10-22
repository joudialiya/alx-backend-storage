#!/usr/bin/env python3
"""Get Logs"""
import pymongo
import pymongo.collection

if __name__ == '__main__':
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    print('{:d} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    for method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
        print('\tmethod {}: {}'.format(
            method,
            nginx_collection.count_documents({'method': method})))
    print('{} status check'.format(
        nginx_collection.count_documents({'path': '/status'})))
