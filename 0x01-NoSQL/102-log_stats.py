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

    # print top ips
    print('IPs:')
    by_ip = nginx_collection.aggregate([
        {
            '$group': {
                '_id': '$ip',
                'req_count': {'$sum': 1}
            }
        },
        {
            '$sort': {'req_count': -1}
        },
        {'$limit': 10}
    ])
    for ip in by_ip:
        print("\t{}: {}".format(ip.get('_id'), ip.get('req_count')))
