#!/usr/bin/env python2

import os
import sys
import platform

def main():
    if os.getuid() != 0:
        print('Requires root privileges')
        sys.exit('Exiting installer')

    if (platform.dist()[0] == 'centos'):
        os.system('''
        yum update -y
        yum install -y git curl
        ''')
    elif (platform.dist()[0] == 'Ubuntu'):
        os.system('''
        apt-get update -y
        apt-get install -y git curl
        ''')
    else:
        print('Operating system not supported')
        sys.exit('Exiting installer')

    os.system('''
    curl -L https://bootstrap.pypa.io/get-pip.py | python2.7
    git clone https://github.com/jamrizzi/beegfs-installer.git
    pip install future
    ''')

    if len(sys.argv) > 1:
        if sys.argv[1] == 'admon':
            os.system('python2 ./beegfs-installer/src/admon-install.py')
        elif sys.argv[1] == 'client':
            os.system('python2 ./beegfs-installer/src/client-install.py')
        elif sys.argv[1] == 'management':
            os.system('python2 ./beegfs-installer/src/management-install.py')
        elif sys.argv[1] == 'metadata':
            os.system('python2 ./beegfs-installer/src/metadata-install.py')
        elif sys.argv[1] == 'storage':
            os.system('python2 ./beegfs-installer/src/storage-install.py')
    else:
        print('No command given')
        sys.exit('Exiting installer')

    os.system('rm -rf ./install.py ./beegfs-installer')

main()
