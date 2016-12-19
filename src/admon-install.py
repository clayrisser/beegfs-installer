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
    install_admon(options)

def get_defaults():
    return {
        'management_node': 'node01',
    }

def gather_information(defaults):
    options = {}
    options['management_node'] = default_prompt('Management Node', defaults['management_node'])
    return options

def default_prompt(name, fallback):
    response = input(name + ' (' + fallback + '): ')
    assert isinstance(response, str)
    if (response):
        return response
    else:
        return fallback

def install_admon(options):
    if (platform.dist()[0] == 'centos'):
        os.system('yum install -y beegfs-admon')
    elif (platform.dist()[0] == 'Ubuntu'):
        os.system('apt-get install -y beegfs-admon')
    else:
        print('Operating system not supported')
        sys.exit('Exiting installer')
    find_replace('/etc/beegfs/beegfs-admon.conf', 'sysMgmtdHost                 =', 'sysMgmtdHost                 = ' + options['management_node'])
    os.system('/etc/init.d/beegfs-admon status')
    os.system('/etc/init.d/beegfs-admon start')

def find_replace(path, find, replace):
    filedata = None
    with open(path, 'r') as file:
        filedata = file.read()
        filedata = filedata.replace(find, replace)
    with open(path, 'w') as file:
        file.write(filedata)

main()
