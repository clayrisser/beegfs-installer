# beegfs-installer
Easy installer for BeeGFS

Installer only supports CentOS and Ubuntu

## Installation

### Management Server
```sh
curl -OL https://raw.githubusercontent.com/jamrizzi/beegfs-installer/master/install.py; sudo python2 install.py management
```

### Metadata Server
```sh
curl -OL https://raw.githubusercontent.com/jamrizzi/beegfs-installer/master/install.py; sudo python2 install.py metadata
```

### Storage Server
```sh
curl -OL https://raw.githubusercontent.com/jamrizzi/beegfs-installer/master/install.py; sudo python2 install.py storage
```

### Client
```sh
curl -OL https://raw.githubusercontent.com/jamrizzi/beegfs-installer/master/install.py; sudo python2 install.py client
```

### Admon Server (optional for graphical interface)
```sh
curl -OL https://raw.githubusercontent.com/jamrizzi/beegfs-installer/master/install.py; sudo python2 install.py admon
```
