#!/usr/bin/env python3
''' Provides some stats about Nginx logs stored in MongoDB '''
import pymongo

if __name__ == '__main__':
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    total_docs = nginx_collection.count_documents({})

    get = nginx_collection.count_documents({'method': 'GET'})
    post = nginx_collection.count_documents({'method': 'POST'})
    put = nginx_collection.count_documents({'method': 'PUT'})
    patch = nginx_collection.count_documents({'method': 'PATCH'})
    delete = nginx_collection.count_documents({'method': 'DELETE'})

    methods = {
            'GET': get,
            'POST': post,
            'PUT': put,
            'PATCH': patch,
            'DELETE': delete
            }

    get_status = nginx_collection.count_documents(
            {
                'method': 'GET',
                'path': '/status'
            }
            )

    print('{} logs'.format(total_docs))
    print('Methods:')

    for method, total in methods.items():
        print('\tmethod {}: {}'.format(method, total))

    print('{} status check'.format(get_status))
