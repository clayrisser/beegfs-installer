# BeeGFS Docker

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

## Starting

### Management Server
```sh
curl -o management-start.sh https://raw.githubusercontent.com/jamrizzi/beegfs-docker/master/management-start.sh && sudo bash management-start.sh
```

### Metadata Server
```sh
curl -o metadata-start.sh https://raw.githubusercontent.com/jamrizzi/beegfs-docker/master/metadata-start.sh && sudo bash metadata-start.sh
```

### Storage Server
```sh
curl -o storage-start.sh https://raw.githubusercontent.com/jamrizzi/beegfs-docker/master/storage-start.sh && sudo bash storage-start.sh
```

### Client
```sh
curl -o client-start.sh https://raw.githubusercontent.com/jamrizzi/beegfs-docker/master/client-start.sh && sudo bash client-start.sh
```

### Admon Server (optional for graphical interface)
```sh
curl -o admon-start.sh https://raw.githubusercontent.com/jamrizzi/beegfs-docker/master/admon-start.sh && sudo bash admon-start.sh
```
