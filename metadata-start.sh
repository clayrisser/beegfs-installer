#!/bin/bash

if [ $(whoami) = "root" ]; then # if run as root

/etc/init.d/beegfs-meta start

else # not run as root
    echo "this program must be run as root"
    echo "exiting"
fi