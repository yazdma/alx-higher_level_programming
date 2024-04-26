#!/usr/bin/python3
"""script for testing status of web pages
"""
if _name_ == "_main_":
    import requests
    import sys
    url = sys.argv[1]
    response = requests.get(url)
    meta = response.headers
    print(meta.get('X-Request-Id'))
