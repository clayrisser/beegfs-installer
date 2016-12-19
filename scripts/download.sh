#!/bin/bash

curl -L https://raw.githubusercontent.com/jamrizzi/beegfs-installer/master/scripts/get_distro.sh | bash

if [ "$DISTRO" == "Ubuntu" ]; then
    curl -L https://github.com/jamrizzi/beegfs-installer/releases/download/v0.0.5/beegfs-installer-ubuntu.tar.gz | tar zxv
elif [ "$DISTRO" == "centos" ]; then
    curl -L https://github.com/jamrizzi/beegfs-installer/releases/download/v0.0.5/beegfs-installer-centos.tar.gz | tar zxv
fi
