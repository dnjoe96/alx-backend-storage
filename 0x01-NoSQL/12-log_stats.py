#!/usr/bin/env python3

if __name__ == '__main__':
    from pymongo import MongoClient
    client = MongoClient('mongodb://127.0.0.1:27017')
    the_logs = client.logs.nginx

    total = the_logs.count_documents({})
    # 94778
    get = the_logs.count_documents({"method": "GET"})
    # 93842
    post = the_logs.count_documents({"method": "POST"})
    # 229
    put = the_logs.count_documents({"method": "PUT"})
    # 0
    patch = the_logs.count_documents({"method": "PATCH"})
    # 0
    delete =  the_logs.count_documents({"method": "DELETE"})
    # 0
    status = the_logs.count_documents({"path": "/status"})
    # 47415
    print(f"{total} logs\n\
            \rMethods:\n\
            method GET: {get}\n\
            method POST: {post}\n\
            method PUT: {put}\n\
            method PATCH: {patch}\n\
            method DELETE: {delete}\n\
            \r{status} status check")
