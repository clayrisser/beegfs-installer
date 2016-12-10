#!/bin/bash

# settings
MANAGEMENT_NODE=node01
STORAGE_SERVICE_ID=3
STORAGE_TARGET_ID=301

if [ $(whoami) = "root" ]; then # if run as root

# gather information
read -p "Management Node (\"$MANAGEMENT_NODE\"): " $MANAGEMENT_NODE_NEW
if [ $MANAGEMENT_NODE_NEW ]; then
    MANAGEMENT_NODE=$MANAGEMENT_NODE_NEW
fi
read -p "Storage Service ID (\"$STORAGE_SERVICE_ID\"): " $STORAGE_SERVICE_ID_NEW
if [ $STORAGE_SERVICE_ID_NEW ]; then
    STORAGE_SERVICE_ID=$STORAGE_SERVICE_ID_NEW
fi
read -p "Storage Target ID (\"$STORAGE_TARGET_ID\"): " $STORAGE_TARGET_ID_NEW
if [ $STORAGE_TARGET_ID_NEW ]; then
    STORAGE_TARGET_ID=$STORAGE_TARGET_ID_NEW
fi

sed -i --follow-symlinks 's/^SELINUX=.*/SELINUX=disabled/g' /etc/sysconfig/selinux && cat /etc/sysconfig/selinux
echo 0 > /selinux/enforce
curl -o /etc/yum.repos.d/beegfs-rhel7.repo http://www.beegfs.com/release/beegfs_6/dists/beegfs-rhel7.repo
rpm --import http://www.beegfs.com/release/latest-stable/gpg/RPM-GPG-KEY-beegfs
yum install -y beegfs-storage
/opt/beegfs/sbin/beegfs-setup-storage -p /mnt/myraid1/beegfs_storage -s $STORAGE_SERVICE_ID -i $STORAGE_TARGET_ID -m $MANAGEMENT_NODE

else # not run as root
    echo "this program must be run as root"
    echo "exiting"
fi
