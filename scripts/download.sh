#!/bin/bash

BEEGFS_INSTALLER_RELEASE=v0.1.0

UNAME=$(uname | tr "[:upper:]" "[:lower:]")
if [ "$UNAME" == "linux" ]; then
    if [ -f /etc/lsb-release -o -d /etc/lsb-release.d ]; then
        export DISTRO=$(lsb_release -i | cut -d: -f2 | sed s/'^\t'//)
    else
        export DISTRO=$(ls -d /etc/[A-Za-z]*[_-][rv]e[lr]* | grep -v "lsb" | cut -d'/' -f3 | cut -d'-' -f1 | cut -d'_' -f1)
    fi
fi
[ "$DISTRO" == "" ] && export DISTRO=$UNAME
unset UNAME
if [ "$(echo $DISTRO | awk '{print substr($0,0,6)}')" == "centos" ]; then
    export DISTRO=centos
fi
if [ "$DISTRO" == "Ubuntu" ]; then
    curl -L https://github.com/jamrizzi/beegfs-installer/releases/download/$BEEGFS_INSTALLER_RELEASE/beegfs-installer-ubuntu.tar.gz | tar zxv
elif [ "$DISTRO" == "centos" ]; then
    curl -L https://github.com/jamrizzi/beegfs-installer/releases/download/$BEEGFS_INSTALLER_RELEASE/beegfs-installer-centos.tar.gz | tar zxv
fi
