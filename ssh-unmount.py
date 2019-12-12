#!/usr/bin/python

import os
import json
import sys

connection_name = None
local_directory = None
local_is_temporary = None


if len(sys.argv) == 1:
    print("\nssh-unmount <CONNECTION_NAME>")
    exit(1)
elif len(sys.argv) == 2:
    connection_name = sys.argv[1]
else:
    print("\nssh-unmount <CONNECTION_NAME>")
    exit(1)

with open('config.json') as json_file:
    config_data = json.load(json_file)

    local_directory = config_data['connections'][connection_name]['local']
    local_is_temporary = config_data['connections'][connection_name]['localistemp']

if connection_name != None and local_directory != None:
    if not os.path.isdir(local_directory):
        exit(2)

    os.system('fusermount -u ' + local_directory)

if local_is_temporary:
    os.system('rm -rf ' + local_directory)

# os.system('')