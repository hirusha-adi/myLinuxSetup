# Kali-Linux-Setup

personal commands list to run after install Kali Linux for my main computer

## Upgrade System

```bash
sudo apt update
sudo apt upgrade -y
```

## Install Nvidia Drivers

Install the nvidia driver, neglect the conflict warning

```
apt-get install nvidia-driver -y
```

Remove the open source driver

```
sudo nano /etc/modprobe.d/blacklist-nouveau.conf
```

```
blacklist nouveau
options nouveau modeset=0
alias nouveau off
```

save file and exit

```bash
update-initramfs -u
```

```bash
reboot
```
