import sys
import os
import platform

class Helper:
    def prepare(self):
        if (platform.dist()[0] == 'centos'):
            if (platform.dist()[0] + platform.dist()[1][0] == 'centos5'):
                os.system('curl -o /etc/yum.repos.d/beegfs-rhel5.repo http://www.beegfs.com/release/beegfs_6/dists/beegfs-rhel5.repo')
            elif (platform.dist()[0] + platform.dist()[1][0] == 'centos6'):
                os.system('curl -o /etc/yum.repos.d/beegfs-rhel6.repo http://www.beegfs.com/release/beegfs_6/dists/beegfs-rhel6.repo')
            elif (platform.dist()[0] + platform.dist()[1][0] == 'centos7'):
                os.system('curl -o /etc/yum.repos.d/beegfs-rhel7.repo http://www.beegfs.com/release/beegfs_6/dists/beegfs-rhel7.repo')
            os.system('rpm --import http://www.beegfs.com/release/latest-stable/gpg/RPM-GPG-KEY-beegfs')
            os.system('yum update -y')
        elif (platform.dist()[0] == 'Ubuntu'):
            os.system('curl -o /etc/apt/sources.list.d/beegfs-deb8.list http://www.beegfs.com/release/beegfs_6/dists/beegfs-deb8.list')
            os.system('wget -q http://www.beegfs.com/release/latest-stable/gpg/DEB-GPG-KEY-beegfs -O- | apt-key add -')
            os.system('apt-get update -y')
        else:
            print('Operating system not supported')
            sys.exit('Exiting installer')

    def is_root():
        if os.getuid() != 0:
            print('Requires root privileges')
            sys.exit('Exiting installer')
