#!/usr/bin/env python

import sys
import os
import platform
import fileinput
from helper import Helper
from builtins import input
helper = Helper()

def main():
    helper.is_root()
    options = gather_information(get_defaults())
    helper.prepare()
    install_storage(options)

def get_defaults():
    return {
        'management_node': 'node01',
        'storage_service_id': '3',
        'storage_target_id': '301'
    }

def gather_information(defaults):
    options = {}
    options['management_node'] = default_prompt('Management Node', defaults['management_node'])
    options['storage_service_id'] = default_prompt('Storage Service ID', defaults['storage_service_id'])
    options['storage_target_id'] = default_prompt('Storage Target ID', defaults['storage_target_id'])
    return options

def default_prompt(name, fallback):
    response = input(name + ' (' + fallback + '): ')
    assert isinstance(response, str)
    if (response):
        return response
    else:
        return fallback

def install_storage(options):
    if (platform.dist()[0] == 'centos'):
        os.system('yum install -y beegfs-storage')
    elif (platform.dist()[0] == 'Ubuntu'):
        os.system('apt-get install -y beegfs-storage')
    else:
        print('Operating system not supported')
        sys.exit('Exiting installer')
    os.system('''
    /opt/beegfs/sbin/beegfs-setup-storage -p /mnt/myraid1/beegfs_storage -s ''' + options['storage_service_id'] + ''' -i ''' + options['storage_target_id'] + ''' -m ''' + options['management_node'] + '''
    /etc/init.d/beegfs-storage start
    /etc/init.d/beegfs-storage status
    ''')

def find_replace(path, find, replace):
    filedata = None
    with open(path, 'r') as file:
        filedata = file.read()
        filedata = filedata.replace(find, replace)
    with open(path, 'w') as file:
        file.write(filedata)

main()
