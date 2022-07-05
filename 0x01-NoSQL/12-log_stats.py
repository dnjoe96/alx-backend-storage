#!/usr/bin/env python3
""" Script to gather log summary from nginx logs """

if __name__ == '__main__':
    from pymongo import MongoClient
    client = MongoClient('mongodb://127.0.0.1:27017')
    the_logs = client.logs.nginx

    total = the_logs.count_documents({})
    get = the_logs.count_documents({"method": "GET"})
    post = the_logs.count_documents({"method": "POST"})
    put = the_logs.count_documents({"method": "PUT"})
    patch = the_logs.count_documents({"method": "PATCH"})
    delete = the_logs.count_documents({"method": "DELETE"})
    status = the_logs.count_documents({"path": "/status"})
    print(f"{total} logs")
    print(f"Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{status} status check")
