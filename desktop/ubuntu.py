from __utils import Base


Base.banner('myLinuxSetup')
Base.askExecute("Update Repos", "sudo apt update")
Base.askExecute("Upgrade System", "sudo apt upgrade")



Base.banner('Browsers')
Base.askExecute("Install Chrome (Browser)", [
    'wget "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb" -o "google-chrome-stable_current_amd64.deb"',
    "sudo dpkg -i ./google-chrome-stable_current_amd64.deb",
    "sudo apt install --fix-broken -y"
    ])
Base.askExecute("Install Brave Browser (Browser)", [
    "sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg",
    'echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list',
    "sudo apt update",
    "sudo apt install brave-browser -y"
    ])
Base.askExecute("Install Firefox (Browser)", "sudo apt install firefox -y")



Base.banner('Utilities')
Base.askExecute("Install Yakuake (Utils) (for KDE)", "sudo apt install yakuake -y")
Base.askExecute("Install Guake (Utils) (for GNOME)", "sudo apt install guake -y")
Base.askExecute("Install ffmpegthumbs (Utils)", "sudo apt install ffmpegthumbs -y")
Base.askExecute("Install mplayerthumbs (Utils)", "sudo apt install mplayerthumbs -y")
Base.askExecute("Install qbittorrent (Torrenting)", "sudo apt install qbittorrent -y")

# Base.banner('??') 
Base.askExecute("Install KDE-Connect (Phone Sync)", "sudo apt install kdeconnect -y")
Base.askExecute("Install flatpak (Package Manager)", "sudo apt install flatpak -y")



Base.banner('Media')
Base.askExecute("Install Audacity (Audio Editor)", "sudo apt install audacity -y")
Base.askExecute("Install RawTherapee (Image Editor)", "sudo apt install rawtherapee -y")
Base.askExecute("Install Pinta (Image Editor)", "sudo apt install pinta -y")
Base.askExecute("Install KdenLive (Video Editor)", "sudo apt install kdenlive -y")
Base.askExecute("Install OpenShot (Video Editor)", "sudo apt install openshot-qt -y")
Base.askExecute("Install Shotcut (Video Editor)", "sudo apt install shotcut -y")
Base.askExecute("Install yt-dlp (Video Downloader)", "sudo apt install yt-dlp -y")
Base.askExecute("Install HandBrake (Video Transcoder)", "sudo apt install handbrake -y")
Base.askExecute("Install Spotify (Music player)", [
    'curl -sS https://download.spotify.com/debian/pubkey_5E3C45D7B312C643.gpg | sudo apt-key add - ',
    'echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list',
    'sudo apt-get update',
    'sudo apt-get install spotify-client -y'
])



Base.banner('System Monitor')
Base.askExecute("Install neofetch (System Monitor)", "sudo apt install neofetch -y")
Base.askExecute("Install bpytop (System Monitor)", "sudo apt install bpytop -y")
Base.askExecute("Install Stacer (System Monitor)", [
    'wget "https://github.com/oguzhaninan/Stacer/releases/download/v1.1.0/stacer_1.1.0_amd64.deb" -o "stacer_1.1.0_amd64.deb"',
    "sudo dpkg -i ./stacer_1.1.0_amd64.deb",
    "sudo apt install --fix-broken -y",
])



Base.banner('Password Manager')
Base.askExecute("Install Bitwarden (Password Manager)", [
    'wget "https://vault.bitwarden.com/download/?app=desktop&platform=linux&variant=deb" -o "Bitwarden.deb"',
    "sudo dpkg -i ./Bitwarden.deb",
    "sudo apt install --fix-broken -y"
])
Base.askExecute("Install KeepassXC (Password Manager)", "sudo apt install keepassxc -y")



Base.banner('Messaging')
Base.askExecute("Install Telegram (Messaging)", [
    "sudo add-apt-repository ppa:atareao/telegram",
    "sudo apt update",
    "sudo apt install telegram -y"
])
Base.askExecute("Install Discord (Messaging)", [
    'wget "https://discord.com/api/download?platform=linux&format=deb" -o "discord.deb"',
    "sudo dpkg -i ./discord.deb",
    "sudo apt install --fix-broken -y"
])



Base.banner('Remote Desktop')
Base.askExecute("Install TeamViwer (Remote Desktop)", [
    'wget "https://download.teamviewer.com/download/linux/teamviewer_amd64.deb" -o "teamviewer_amd64.deb"',
    "sudo dpkg -i ./teamviewer_amd64.deb",
    "sudo apt install --fix-broken -y"
])
Base.askExecute("Install AnyDesk (Remote Desktop)", [
    'wget -qO - https://keys.anydesk.com/repos/DEB-GPG-KEY | apt-key add -',
    'echo "deb http://deb.anydesk.com/ all main" > /etc/apt/sources.list.d/anydesk-stable.list',
    'apt update',
    'apt install anydesk -y'
])



Base.banner('Flasher')
Base.askExecute("Install Balena Etcher (Flasher)", [
    'wget "https://github.com/balena-io/etcher/releases/download/v1.18.4/balena-etcher_1.18.4_amd64.deb" -o "balena-etcher_1.18.4_amd64.deb"',
    "sudo dpkg -i ./balena-etcher_1.18.4_amd64.deb",
    "sudo apt install --fix-broken -y"
])
Base.askExecute("Install Popsicle (Flasher)", 'wget "https://github.com/pop-os/popsicle/releases/download/1.3.1/Popsicle_USB_Flasher-1.3.1-x86_64.AppImage" -o "Popsicle_USB_Flasher"')
Base.askExecute("Install UNetbootin (Flasher)", [
    "sudo add-apt-repository ppa:gezakovacs/ppa",
    "sudo apt-get update",
    "sudo apt-get install unetbootin"
])



Base.banner('Development')
Base.askExecute("Install Git (Development)", "sudo apt install git -y")
Base.askExecute("Install Docker (Development)", [
    'sudo apt-get remove docker docker-engine docker.io containerd runc -y',
    'sudo apt-get update',
    'sudo apt-get install ca-certificates curl gnupg lsb-release -y',
    'sudo mkdir -p /etc/apt/keyrings',
    'curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg',
    'echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null',
    'sudo apt-get update',
    'sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-compose -y'
])
Base.askExecute("Install Github Desktop (Development)", [
    'sudo apt install gdebi -y',
    'wget wget https://github.com/shiftkey/desktop/releases/download/release-2.9.3-linux3/GitHubDesktop-linux-2.9.3-linux3.deb',
    'sudo gdebi ./GitHubDesktop-linux-2.9.3-linux3.deb'
])
Base.askExecute("Install Visual Studio Code (Development)", [
    'sudo apt-get install wget gpg',
    'wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg',
    'sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/',
    '''sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list' ''',
    'rm -f packages.microsoft.gpg',
    'sudo apt install apt-transport-https',
    'sudo apt update',
    'sudo apt install code -y'
])
Base.askExecute("Install VirtualBox (Development)", "sudo apt install virtualbox -y")
Base.askExecute("Install OpenJDK v8 (Development)", "sudo apt install openjdk-8-jdk -y")
Base.askExecute("Install NodeJS (Development)", "sudo apt install nodejs -y")
Base.askExecute("Install NPM (Development)", "sudo apt install npm -y")
Base.askExecute("Install TCL (Development)", "sudo apt install tcl -y")
Base.askExecute("Install FPC (Development)", "sudo apt install fpc -y")
Base.askExecute("Install NotepadQQ (Development)", "sudo apt install notepadqq -y")
Base.askExecute("Install codeblocks (Development)", "sudo apt install codeblocks -y")
Base.askExecute("Install MongoDB Compass (Development)", [
    'wget "https://downloads.mongodb.com/compass/mongodb-compass_1.35.0_amd64.deb" -o "mongodb-compass_1.35.0_amd64.deb"',
    "sudo dpkg -i ./mongodb-compass_1.35.0_amd64.deb",
    "sudo apt install --fix-broken -y"
])


