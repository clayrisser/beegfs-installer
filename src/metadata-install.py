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
        mkfs.ext4 -i 2048 -I 512 -J size=400 -Odir_index,filetype ''' + options['metadata_mount'] + '''
        echo "''' + options['metadata_mount'] + ' ' + '/mnt/beegfs-meta/' + ''' ext4 defaults 0 2" | tee -a /etc/fstab
        mount -a && mount
        /opt/beegfs/sbin/beegfs-setup-meta -p /mnt/beegfs-meta/ -s ''' + options['metadata_service_id'] + ' -m ' + options['management_node'] + '''
        ''')
    else:
        os.system('/opt/beegfs/sbin/beegfs-setup-meta -p /data/beegfs/beegfs-meta/ -s ' + options['metadata_service_id'] + ' -m ' + options['management_node'])
    os.system('''
    /etc/init.d/beegfs-meta start
    /etc/init.d/beegfs-meta status
    ''')

def _default_prompt(name, fallback):
    response = input(name + ' (' + fallback + '): ')
    assert isinstance(response, str)
    if (response):
        return response
    else:
        return fallback

main()
