#!/usr/bin/python

import os
import json
import sys

connection_name = None
local_directory = None

user = None
host = None
remote = None

home_dir = os.path.expanduser("~")

config_file = home_dir + "/.config/sshmounter.json"

if len(sys.argv) == 1:
    print("\nssh-mount <CONNECTION_NAME>")
    exit(1)
elif len(sys.argv) == 2:
    connection_name = sys.argv[1]
else:
    print("\nssh-mount <CONNECTION_NAME>")
    exit(1)

with open(config_file) as json_file:
    config_data = json.load(json_file)

    local_directory = config_data['connections'][connection_name]['local']

    user = config_data['connections'][connection_name]['user']
    host = config_data['connections'][connection_name]['host']
    remote = config_data['connections'][connection_name]['remote']

if connection_name != None and \
    local_directory != None and \
    user != None and \
    host != None and \
    remote != None:

    if not os.path.isdir(local_directory):
        os.system('mkdir -p ' + local_directory)

    os.system('sshfs ' + user + '@' + host + ':' + remote + ' ' + local_directory)
    print("Mount Directory: " + local_directory)

# os.system('')