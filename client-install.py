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
    install_client(options)
    reboot(options)

def get_defaults():
    return {
        'management_node': 'node01',
        'kernel_module_autobuild': 'N',
        'restart': 'Y'
    }

def gather_information(defaults):
    options = {}
    options['management_node'] = default_prompt('Management Node', defaults['management_node'])
    options['kernel_module_autobuild'] = boolean_prompt('Kernel Module Autobuild', defaults['kernel_module_autobuild'])
    options['restart'] = boolean_prompt('Restart', defaults['restart'])
    return options

def default_prompt(name, fallback):
    response = input(name + ' (' + fallback + '): ')
    assert isinstance(response, str)
    if (response):
        return response
    else:
        return fallback

def boolean_prompt(name, fallback):
    default = 'Y|n'
    fallback = fallback.upper()
    if (fallback == 'N'):
        default = 'y|N'
    response = input(name + ' (' + default + '): ')
    assert isinstance(response, str)
    if (response):
        return response.upper()
    else:
        return fallback

def install_client(options):
    if (platform.dist()[0] == 'centos'):
        os.system('''
        yum install -y kernel-devel
        yum groupinstall -y 'Development Tools'
        yum install -y beegfs-client beegfs-helperd beegfs-utils
        ''')
#        if (options['kernel_module-autobuild'] == 'Y'):

    elif (platform.dist()[0] == 'Ubuntu'):
        os.system('''
        apt-get install -y kernel-devel
        apt-get groupinstall -y 'Development Tools'
        apt-get install -y beegfs-client beegfs-helperd beegfs-utils
        ''')
    else:
        print('Operating system not supported')
        sys.exit('Exiting installer')
    os.system('''
    /opt/beegfs/sbin/beegfs-setup-client -m ''' + options['management_node'] + '''
    /etc/init.d/beegfs-client start
    /etc/init.d/beegfs-helperd start
    /etc/init.d/beegfs-client status
    /etc/init.d/beegfs-helperd status
    ''')

def reboot(options):
    if (options['reboot'] == 'Y'):
        os.system('reboot')

def find_replace(path, find, replace):
    filedata = None
    with open(path, 'r') as file:
        filedata = file.read()
        filedata = filedata.replace(find, replace)
    with open(path, 'w') as file:
        file.write(filedata)

main()
