#!/usr/bin/env python
# Manipulate csv effectively
dpath = 'data.csv'
with open(dpath, 'r') as f : 
    headers = next(f)
    for line in f: 
        line = line.strip()
        parts = line.split(',')
        parts[1] = float(parts[1])
        parts[4] = float(parts[4])
        print(parts)


