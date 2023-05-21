from __utils import Base


Base.banner('myLinuxSetup')
Base.askExecute("Update Repos", "sudo pacman -Syy")
Base.askExecute("Upgrade System", "sudo pacman -Syu")



Base.banner('Setting Up...')
print("Installing yay")
Base.archInstallYay()

Base.askExecute("Install Brave Browser (Browser)", "yay -S brave-bin")
Base.askExecute("Install Firefox (Browser)", "yay -S firefox")



Base.banner('Utilities')
Base.askExecute("Install Yakuake (Utils) (for KDE)", "yay -S yakuake ")
Base.askExecute("Install Guake (Utils) (for GNOME)", "yay -S guake ")
Base.askExecute("Install ffmpegthumbs (Utils)", "yay -S ffmpegthumbs ")
Base.askExecute("Install mplayerthumbs (Utils)", "yay -S mplayerthumbs ")
Base.askExecute("Install qbittorrent (Torrenting)", "yay -S qbittorrent ")

# Base.banner('??') 
Base.askExecute("Install KDE-Connect (Phone Sync)", "yay -S kdeconnect ")
Base.askExecute("Install flatpak (Package Manager)", "yay -S flatpak ")



Base.banner('Media')
Base.askExecute("Install Audacity (Audio Editor)", "yay -S audacity ")
Base.askExecute("Install RawTherapee (Image Editor)", "yay -S rawtherapee ")
Base.askExecute("Install Pinta (Image Editor)", "yay -S pinta ")
Base.askExecute("Install KdenLive (Video Editor)", "yay -S kdenlive ")
Base.askExecute("Install OpenShot (Video Editor)", "yay -S openshot-git ")
Base.askExecute("Install Shotcut (Video Editor)", "yay -S shotcut ")
Base.askExecute("Install yt-dlp (Video Downloader)", "yay -S yt-dlp-git ")
Base.askExecute("Install yt-dlp GUI (Video Downloader)", "yay -S ytdlp-gui ")
Base.askExecute("Install HandBrake (Video Transcoder)", "yay -S handbrake ")
Base.askExecute("Install Spotify (Music player)", "yay -S spotify ")



Base.banner('System Monitor')
Base.askExecute("Install neofetch (System Monitor)", "yay -S neofetch ")
Base.askExecute("Install bpytop (System Monitor)", "yay -S bpytop ")
Base.askExecute("Install Stacer (System Monitor)", "yay -S stacer-bin ")



Base.banner('Password Manager')
Base.askExecute("Install Bitwarden (Password Manager)", "yay -S bitwarden ")
Base.askExecute("Install KeepassXC (Password Manager)", "yay -S keepassxc ")



Base.banner('Messaging')
Base.askExecute("Install Telegram (Messaging)", "yay -S telegram-desktop-bin ")
Base.askExecute("Install Discord (Messaging)", "yay -S discord")



Base.banner('Remote Desktop')
Base.askExecute("Install TeamViwer (Remote Desktop)", "yay -S teamviewer")
Base.askExecute("Install AnyDesk (Remote Desktop)", "yay -S anydesk-bin ")



Base.banner('Flasher')
Base.askExecute("Install Balena Etcher (Flasher)", "yay -S etcher-bin ")
Base.askExecute("Install Popsicle (Flasher)", "yay -S popsicle-bin ")
Base.askExecute("Install UNetbootin (Flasher)", "yay -S unetbootin ")



Base.banner('Development')
Base.askExecute("Install Git (Development)", "yay -S git ")
Base.askExecute("Install Docker (Development)", [
    "yay -S docker",
    "yay -S docker-compose"
])
Base.askExecute("Install Github Desktop (Development)", "github-desktop-bin ")
Base.askExecute("Install Visual Studio Code (Development)", "yay -S visual-studio-code-bin")
Base.askExecute("Install VirtualBox (Development)", "yay -S virtualbox ")
Base.askExecute("Install OpenJDK v8 (Development)", "yay -S jdk8-openjdk ")
Base.askExecute("Install NodeJS (Development)", "yay -S nodejs ")
Base.askExecute("Install Pycharm Community Edition (Development)", "yay -S pycharm-community-edition")
Base.askExecute("Install Eclipse (Development)", "yay -S eclipse")
Base.askExecute("Install NPM (Development)", "yay -S npm ")
Base.askExecute("Install TCL (Development)", "yay -S tcl ")
Base.askExecute("Install FPC (Development)", "yay -S fpc ")
Base.askExecute("Install NotepadQQ (Development)", "yay -S notepadqq ")
Base.askExecute("Install codeblocks (Development)", "yay -S codeblocks ")
Base.askExecute("Install MongoDB Compass (Development)", "yay -S mongodb-compoass")


