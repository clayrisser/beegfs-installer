# beegfs-installer
Easy installer for BeeGFS

Installer only supports CentOS and Ubuntu

## Installation

```sh
curl -L https://raw.githubusercontent.com/jamrizzi/beegfs-installer/master/scripts/download.sh | bash
```

### Management Server
```sh
sudo beegfs-installer/management-install
```

### Metadata Server
```sh
sudo beegfs-installer/metadata-install
```

### Storage Server
```sh
sudo beegfs-installer/storage-install
```

### Client
```sh
sudo beegfs-installer/client-install
```

### Admon Server (optional for graphical interface)
```sh
sudo beegfs-installer/admon-install
```

## Building
```sh
git clone https://github.com/jamrizzi/beegfs-installer.git
cd beegfs-installer
sudo make
```
