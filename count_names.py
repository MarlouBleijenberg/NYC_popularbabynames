#!/usr/bin/env python

import json

with open("2014_female_hispanic.json", "r") as inputFile:
    data = json.load(inputFile)

countA = 0
for d in data:
    if d[11].startswith("A"):
        print d[11]
        countA += int(d[12])
        
print countA