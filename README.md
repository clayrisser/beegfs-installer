# beegfs-installer
A clustered storage solution

## Installation

### Management Server
```sh
curl -o management-install https://github.com/jamrizzi/beegfs-installer/releases/download/v0.0.1/management-install && sudo chmod +x ./management-install && sudo ./management-install
```

### Metadata Server
```sh
curl -o metadata-install https://github.com/jamrizzi/beegfs-installer/releases/download/v0.0.1/metadata-install && sudo chmod +x ./metadata-install && sudo ./metadata-install
```

### Storage Server
```sh
curl -o storage-install https://github.com/jamrizzi/beegfs-installer/releases/download/v0.0.1/storage-install && sudo chmod +x ./storage-install && sudo ./storage-install
```

### Client
```sh
curl -o client-install https://github.com/jamrizzi/beegfs-installer/releases/download/v0.0.1/client-install && sudo chmod +x ./client-install && sudo ./client-install
```
Make sure your client machine restarts after installation.

### Admon Server (optional for graphical interface)
```sh
curl -o admon-install https://github.com/jamrizzi/beegfs-installer/releases/download/v0.0.1/admon-install && sudo chmod +x ./admon-install && sudo ./admon-install
```

## Building
1. Install pyinstaller
```sh
sudo pip install pyinstaller
```

2. Run pyinstaller on each python script
```sh
pyinstaller --onefile --noupx python-script.py
```
