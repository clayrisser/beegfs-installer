#!/usr/bin/env python2

import sys
import os
import platform
import fileinput
from helper import Helper
helper = Helper()

def main():
    helper.is_root()
    options = gather_information(get_defaults())
    helper.prepare()
    install_client(options)

def get_defaults():
    return {
        'management_node': 'localhost'
    }

def gather_information(defaults):
    options = {}
    options['management_node'] = helper.default_prompt('Management Node', defaults['management_node'])
    return options

def install_client(options):
    if (platform.dist()[0] == 'centos'):
        os.system('''
        yum install -y kernel-devel
        yum groupinstall -y 'Development Tools'
        yum install -y beegfs-client beegfs-helperd beegfs-utils
        ''')
    elif (platform.dist()[0] == 'Ubuntu'):
        os.system('''
        apt-get install -y linux-headers-generic build-essential
        apt-get install -y beegfs-client beegfs-helperd beegfs-utils
        ''')
    else:
        print('Operating system not supported')
        sys.exit('Exiting installer')
    os.system('''
    /opt/beegfs/sbin/beegfs-setup-client -m ''' + options['management_node'] + '''
    /etc/init.d/beegfs-helperd start
    /etc/init.d/beegfs-client start
    /etc/init.d/beegfs-helperd status
    /etc/init.d/beegfs-client status
    ''')

main()
