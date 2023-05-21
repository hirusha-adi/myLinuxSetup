# myLinuxSetup

```
.
├── desktop
│   ├── arch.py             <- for Arch Linux
│   ├── cinnamon            <- for Cinnamon Desktop Environment
│   │   └── windowsXP.sh    <- Windows XP Theme
│   ├── kali.md             <- for Kali Linux (+ NVIDIA Guide)
│   ├── ubuntu.py           <- for Ubuntu
│   ├── user-dirs.dirs      <- Specific to @mainrig
│   └── __utils.py
├── README.md
└── server
    ├── jellyfin.sh         <- install Jellyfin Server
    └── ssh-setup.sh        <- start SSH Server
```

# Initial Setup

### Arch Linux

```
sudo pacman -Sy python python2 python-pip base-devel wget curl git --no-confirm
```

### Ubuntu

```
sudo apt install update && sudo apt install python3 python3-pip git curl wget -y
```
