#!/usr/bin/env python

import sys
import os
import platform
import fileinput
from helper import Helper
from builtins import input
helper = Helper()

def main():
    if os.getenv("SUDO_USER") == None:
        print('Requires root privileges')
        sys.exit('Exiting installer')
    options = gather_information(get_defaults())
    helper.prepare()
    install_metadata(options)
    reboot(options)

def get_defaults():
    return {
        'management_node': 'node01',
        'metadata_service_id': '2'
    }

def gather_information(defaults):
    options = {}
    options['management_node'] = default_prompt('Management Node', defaults['management_node'])
    options['metadata_service_id'] = default_prompt('Metadata Service ID', defaults['metadata_service_id'])
    return options

def default_prompt(name, fallback):
    response = input(name + ' (' + fallback + '): ')
    assert isinstance(response, str)
    if (response):
        return response
    else:
        return fallback

def install_metadata(options):
    if (platform.dist()[0] == 'centos'):
        os.system('''
        yum install -y beegfs-meta
        ''')
    elif (platform.dist()[0] == 'Ubuntu'):
        os.system('''
        apt-get install -y beegfs-meta
        ''')
    else:
        print('Operating system not supported')
        sys.exit('Exiting installer')
    os.system('''
    beegfs-setup-meta -p /data/beegfs/beegfs_meta -s ''' + options['metadata_service_id'] + ''' -m ''' + options['management_node'] + '''
    /etc/init.d/beegfs-meta start
    /etc/init.d/beegfs-meta status
    ''')

def find_replace(path, find, replace):
    filedata = None
    with open(path, 'r') as file:
        filedata = file.read()
        filedata = filedata.replace(find, replace)
    with open(path, 'w') as file:
        file.write(filedata)

main()
