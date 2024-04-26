#!/usr/bin/python3
"""script for posting data to web servers
"""
if _name_ == "_main_":
    import requests
    import sys
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code != requests.codes.ok:
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.text)
