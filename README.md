# beegfs-installer
A clustered storage solution

## Installation

### Management Server
```sh
curl -o management-install.sh https://raw.githubusercontent.com/jamrizzi/beegfs-docker/master/management-install.sh && sudo bash management-install.sh
```

### Metadata Server
```sh
curl -o metadata-install.sh https://raw.githubusercontent.com/jamrizzi/beegfs-docker/master/metadata-install.sh && sudo bash metadata-install.sh
```

### Storage Server
```sh
curl -o storage-install.sh https://raw.githubusercontent.com/jamrizzi/beegfs-docker/master/storage-install.sh && sudo bash storage-install.sh
```

### Client
```sh
curl -o client-install.sh https://raw.githubusercontent.com/jamrizzi/beegfs-docker/master/client-install.sh && sudo bash client-install.sh
```
Make sure your client machine restarts after installation.

### Admon Server (optional for graphical interface)
```sh
curl -o admon-install.sh https://raw.githubusercontent.com/jamrizzi/beegfs-docker/master/admon-install.sh && sudo bash admon-install.sh
```
