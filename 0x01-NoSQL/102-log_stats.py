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
    ip_list = [
            "172.31.63.67", "172.31.2.14", "172.31.29.194",
            "69.162.124.230", "64.124.26.109", "64.62.224.29",
            "34.207.121.61", "47.88.100.4", "45.249.84.250",
            "216.244.66.228"
            ]
    ip_dict = {ip: the_logs.count_documents({"ip": ip}) for ip in ip_list}

    print(f"{total} logs")
    print(f"Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{status} status check")
    print("IPs:")
    print(f"\t{ip}: {val}")
    print(f"\t{ip}: {val}")
    print(f"\t{ip}: {val}")
    print(f"\t{ip}: {val}")
    print(f"\t{ip}: {val}")
    print(f"\t{ip}: {val}")
    print(f"\t{ip}: {val}")
    print(f"\t{ip}: {val}")
    print(f"\t{ip}: {val}")
    print(f"\t{ip}: {val}")
    print(f"\t{ip}: {val}")
    print(f"\t{ip}: {val}")
