#!/usr/bin/python3
import urllib

'''script that feches all he url'''
#use contex manager

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
     content = response.read()
     print("Body response:")
     print(f"  - type: {type(content)}")
     print(f"  - content: {content}")
     print(f"  - utf8 content: {content.decode('utf-8')}")
