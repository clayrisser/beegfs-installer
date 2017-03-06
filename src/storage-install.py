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
    install_storage(options)

def get_defaults():
    return {
        'management_node': 'localhost',
        'storage_service_id': '3',
        'storage_target_id': '301',
        'storage_mount': 'local'
    }

def gather_information(defaults):
    options = {}
    options['management_node'] = helper.default_prompt('Management Node', defaults['management_node'])
    options['storage_service_id'] = helper.default_prompt('Storage Service ID', defaults['storage_service_id'])
    options['storage_target_id'] = helper.default_prompt('Storage Target ID', defaults['storage_target_id'])
    options['storage_mount'] = helper.default_prompt('Storage Mount', defaults['storage_mount'])
    return options

def install_storage(options):
    if (platform.dist()[0] == 'centos'):
        os.system('yum install -y beegfs-storage')
    elif (platform.dist()[0] == 'Ubuntu'):
        os.system('apt-get install -y beegfs-storage')
    else:
        print('Operating system not supported')
        sys.exit('Exiting installer')
    if options['storage_mount'] != 'local':
        os.system('''
        mkdir -p /mnt/beegfs-storage/
        mkfs.xfs ''' + options['storage_mount'] + '''
        echo "''' + options['storage_mount'] + ' ' + '/mnt/beegfs-storage/' + ''' xfs defaults 0 2" | tee -a /etc/fstab
        mount -a && mount
        chmod -R 777 /mnt/beegfs-storage/
        /opt/beegfs/sbin/beegfs-setup-storage -p /mnt/beegfs-storage/ -s ''' + options['storage_service_id'] + ' -i ' + options['storage_target_id'] + ' -m ' + options['management_node'] + '''
        ''')
    else:
        os.system('/opt/beegfs/sbin/beegfs-setup-storage -p /data/beegfs/beegfs-storage/ -s ' + options['storage_service_id'] + ' -i ' + options['storage_target_id'] + ' -m ' + options['management_node'])
    os.system('''
    /etc/init.d/beegfs-storage start
    /etc/init.d/beegfs-storage status
    ''')

main()
