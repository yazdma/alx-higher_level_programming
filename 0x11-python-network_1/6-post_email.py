#!/usr/bin/python3
"""script for posting data to web servers
"""
if _name_ == "_main_":
    import requests
    import sys
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    response = requests.post(url, data=payload)
    print(response.text)
