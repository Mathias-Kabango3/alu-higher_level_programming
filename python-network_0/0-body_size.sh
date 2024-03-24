#!/bin/bash
#content-length
curl -s -I "$1" | grep Content-Length | cut -d" " -f2
