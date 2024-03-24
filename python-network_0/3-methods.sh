#!/bin/bash
#return all the allowed methods
curl -I -s "$1" | grep Allow | cut -d" " -f2-
