#!/bin/bash

if [ $(whoami) = "root" ]; then # if run as root

curl -o /etc/yum.repos.d/beegfs-rhel7.repo http://www.beegfs.com/release/beegfs_6/dists/beegfs-rhel7.repo
rpm --import http://www.beegfs.com/release/latest-stable/gpg/RPM-GPG-KEY-beegfs
yum install -y beegfs-mgmtd
/opt/beegfs/sbin/beegfs-setup-mgmtd -p /data/beegfs/beegfs_mgmtd
/etc/init.d/beegfs-mgmtd start

else # not run as root
    echo "this program must be run as root"
    echo "exiting"
fi
