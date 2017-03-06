#!/usr/bin/env python2

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
        'management_node': 'localhost',
    }

def gather_information(defaults):
    options = {}
    options['management_node'] = helper.default_prompt('Management Node', defaults['management_node'])
    return options

def install_admon(options):
    if (platform.dist()[0] == 'centos'):
        os.system('yum install -y beegfs-admon')
    elif (platform.dist()[0] == 'Ubuntu'):
        os.system('apt-get install -y beegfs-admon')
    else:
        print('Operating system not supported')
        sys.exit('Exiting installer')
    helper.find_replace('/etc/beegfs/beegfs-admon.conf', 'sysMgmtdHost                 =', 'sysMgmtdHost                 = ' + options['management_node'])
    os.system('/etc/init.d/beegfs-admon status')
    os.system('/etc/init.d/beegfs-admon start')

main()
