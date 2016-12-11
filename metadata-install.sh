#!/bin/bash

# settings
MANAGEMENT_NODE=node01
METADATA_SERVICE_ID=2

if [ $(whoami) = "root" ]; then # if run as root

# gather information
read -p "Management Node (\"$MANAGEMENT_NODE\"): " $MANAGEMENT_NODE_NEW
if [ $MANAGEMENT_NODE_NEW ]; then
    MANAGEMENT_NODE=$MANAGEMENT_NODE_NEW
fi
read -p "Metadata Service ID (\"$METADATA_SERVICE_ID\"): " $METADATA_SERVICE_ID_NEW
if [ $METADATA_SERVICE_ID_NEW ]; then
    METADATA_SERVICE_ID=$METADATA_SERVICE_ID_NEW
fi

curl -o /etc/yum.repos.d/beegfs-rhel7.repo http://www.beegfs.com/release/beegfs_6/dists/beegfs-rhel7.repo
rpm --import http://www.beegfs.com/release/latest-stable/gpg/RPM-GPG-KEY-beegfs
yum install -y beegfs-meta
/opt/beegfs/sbin/beegfs-setup-meta -p /data/beegfs/beegfs_meta -s $METADATA_SERVICE_ID -m $MANAGEMENT_NODE

else # not run as root
    echo "this program must be run as root"
    echo "exiting"
fi
