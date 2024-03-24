#!/usr/bin/python3
''' script that fetches a url'''


import urllib.request
"""use contex manager"""

if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()
        print("Body response:")
        print(f"  - type: {type(content)}")
        print(f"  - content: {content}")
        print(f"  - utf8 content: {content.decode('utf-8')}")
