#!/usr/bin/python2

import json

with open('config.json', 'r') as f:
    config = json.load(f)

print (config)


# to edit config programatically
config['something'] = 'something'
config['somethingnumeric'] = 101001113

with open('config.json', 'w') as f:
    json.dump(config, f, indent=4) 

