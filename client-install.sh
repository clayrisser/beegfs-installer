#!/bin/bash

# settings
MANAGEMENT_NODE=node01
KERNEL_MODULE_AUTOBUILD=N
RESTART=Y

if [ $(whoami) = "root" ]; then # if run as root

# gather information
read -p "Management Node ($MANAGEMENT_NODE): " MANAGEMENT_NODE_NEW
if [ $MANAGEMENT_NODE_NEW ]; then
    MANAGEMENT_NODE=$MANAGEMENT_NODE_NEW
fi
read -p "Kernel Module Autobuild (y|N): " KERNEL_MODULE_AUTOBUILD_NEW
if [ $KERNEL_MODULE_AUTOBUILD_NEW ]; then
    KERNEL_MODULE_AUTOBUILD=$KERNEL_MODULE_AUTOBUILD_NEW
fi

yum install -y kernel-devel
yum groupinstall -y 'Development Tools'
sed -i --follow-symlinks 's/^SELINUX=.*/SELINUX=disabled/g' /etc/sysconfig/selinux && cat /etc/sysconfig/selinux
curl -o /etc/yum.repos.d/beegfs-rhel7.repo http://www.beegfs.com/release/beegfs_6/dists/beegfs-rhel7.repo
rpm --import http://www.beegfs.com/release/latest-stable/gpg/RPM-GPG-KEY-beegfs
yum install -y beegfs-client beegfs-helperd beegfs-utils
if [ ${KERNEL_MODULE_AUTOBUILD,,}=y ]; then
    sed -i "s/buildArgs=-j8/buildArgs=-j8 BEEGFS_OPENTK_IBVERBS=1/g" /etc/beegfs/beegfs-client-autobuild.conf
    /etc/init.d/beegfs-client rebuild
fi
/opt/beegfs/sbin/beegfs-setup-client -m $MANAGEMENT_NODE

read -p "Restart Machine? (Y|n): " RESTART_NEW
if [ $RESTART_NEW ]; then
    RESTART=$RESTART_NEW
fi
if [ ${RESTART,,}=y ]; then
    restart
fi

else # not run as root
    echo "this program must be run as root"
    echo "exiting"
fi
