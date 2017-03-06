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
    install_metadata(options)

def get_defaults():
    return {
        'management_node': 'localhost',
        'metadata_service_id': '2',
        'metadata_mount': 'local'
    }

def gather_information(defaults):
    options = {}
    options['management_node'] = helper.default_prompt('Management Node', defaults['management_node'])
    options['metadata_service_id'] = helper.default_prompt('Metadata Service ID', defaults['metadata_service_id'])
    options['metadata_mount'] = helper.default_prompt('Metadata Mount', defaults['metadata_mount'])
    return options

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
    if options['metadata_mount'] != 'local':
        os.system('''
        mkdir -p /mnt/beegfs-meta/
        mkfs.ext4 ''' + options['metadata_mount'] + '''
        echo "''' + options['metadata_mount'] + ' ' + '/mnt/beegfs-meta/' + ''' ext4 defaults 0 2" | tee -a /etc/fstab
        mount -a && mount
        chmod -R 777 /mnt/beegfs-meta/
        rm -rf /mnt/beegfs-meta/* && rm -rf /mnt/beegfs-meta/.*
        /opt/beegfs/sbin/beegfs-setup-meta -p /mnt/beegfs-meta/ -s ''' + options['metadata_service_id'] + ' -m ' + options['management_node'] + '''
        ''')
        helper.find_replace('/etc/beegfs/beegfs-meta.conf', 'sysMgmtdHost                 =', 'sysMgmtdHost                 = ' + options['management_node'])
        helper.find_replace('/etc/beegfs/beegfs-meta.conf', 'storeMetaDirectory           =', 'storeMetaDirectory           = /mnt/beegfs-meta/')
    else:
        os.system('/opt/beegfs/sbin/beegfs-setup-meta -p /data/beegfs/beegfs-meta/ -s ' + options['metadata_service_id'] + ' -m ' + options['management_node'])
    os.system('''
    /etc/init.d/beegfs-meta start
    /etc/init.d/beegfs-meta status
    ''')

main()
