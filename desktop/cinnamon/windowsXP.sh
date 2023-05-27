wget https://archive.org/download/bliss-600dpi/bliss-600dpi.png -P ~/Pictures
git clone https://github.com/B00merang-Project/Windows-XP.git Windows-XP-Themes
git clone https://github.com/B00merang-Artwork/Windows-XP.git Windows-XP-Icons
mkdir -p ~/.themes ~/.icons
cp -r 'Windows-XP-Themes/Windows XP Luna' ~/.themes
cp -r 'Windows-XP-Icons/' ~/.icons
sleep 3
dconf load / < windowsXP.conf