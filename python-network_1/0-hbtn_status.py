#!/usr/bin/python3
""" fetch https://intranet.hbtn.io/status """

import urllib.request

url = 'https://intranet.hbtn.io/status'
if url.startswith('https://'):
    url = 'https://alu-intranet.hbtn.io/status'

if _name_ == '_main_':
    with urllib.request.urlopen(url) as responds:
        content = responds.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
