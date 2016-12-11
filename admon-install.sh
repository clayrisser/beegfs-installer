#!/bin/bash

# settings
MANAGEMENT_NODE=node01

if [ $(whoami) = "root" ]; then # if run as root

# gather information
read -p "Management Node ($MANAGEMENT_NODE): " MANAGEMENT_NODE_NEW
if [ $MANAGEMENT_NODE_NEW ]; then
    MANAGEMENT_NODE=$MANAGEMENT_NODE_NEW
fi

curl -o /etc/yum.repos.d/beegfs-rhel7.repo http://www.beegfs.com/release/beegfs_6/dists/beegfs-rhel7.repo
rpm --import http://www.beegfs.com/release/latest-stable/gpg/RPM-GPG-KEY-beegfs
yum install -y beegfs-admon
sed -i "s/sysMgmtdHost                 =/sysMgmtdHost                 = $MANAGEMENT_NODE #/g" /etc/beegfs/beegfs-admon.conf

else # not run as root
    echo "this program must be run as root"
    echo "exiting"
fi
