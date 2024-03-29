#!/usr/bin/python3
""" X-Request_Id Header of an URL """

import urllib.request
import sys


if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as res:
        header = res.info()
        print(header['X-Request-Id'])
