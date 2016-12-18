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
    helper.prepare()
    install_management()

def install_management():
    if (platform.dist()[0] == 'centos'):
        os.system('yum install -y beegfs-mgmtd')
    elif (platform.dist()[0] == 'Ubuntu'):
        os.system('apt-get install -y beegfs-mgmtd')
    else:
        print('Operating system not supported')
        sys.exit('Exiting installer')
    os.system('''
    /opt/beegfs/sbin/beegfs-setup-mgmtd -p /data/beegfs/beegfs_mgmtd
    /etc/init.d/beegfs-mgmtd start
    /etc/init.d/beegfs-mgmtd status
    ''')

main()
