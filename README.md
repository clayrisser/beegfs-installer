# beegfs-installer
Easy installer for BeeGFS

Installer only supports CentOS and Ubuntu

## Installation

### Management Server
```sh
curl -L -o beegfs.py http://bit.ly/2n5lDz5; sudo python2 beegfs.py management
```

### Metadata Server
```sh
curl -L -o beegfs.py http://bit.ly/2n5lDz5; sudo python2 beegfs.py metadata
```

### Storage Server
```sh
curl -L -o beegfs.py http://bit.ly/2n5lDz5; sudo python2 beegfs.py storage
```

### Client
```sh
curl -L -o beegfs.py http://bit.ly/2n5lDz5; sudo python2 beegfs.py client
```
You may need to restart the server and run the following command.
```
sudo service beegfs-client start
```

### Admon Server (optional for graphical interface)
```sh
curl -L -o beegfs.py http://bit.ly/2n5lDz5; sudo python2 beegfs.py admon
```
