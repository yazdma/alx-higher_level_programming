#!/usr/bin/python3
"""script for testing status of web pages
"""
if _name_ == "_main_":
    import requests
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)
    content = response.text
    print_str = '''Body response:
\t- type: {}
\t- content: {}'''.format(type(content), content)
    print(print_str)
