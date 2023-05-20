wget https://archive.org/download/bliss-600dpi/bliss-600dpi.png -P ~/Pictures
git clone https://github.com/B00merang-Project/Windows-XP.git Windows-XP-Themes
git clone https://github.com/B00merang-Artwork/Windows-XP.git Windows-XP-Icons
mkdir -p ~/.themes ~/.icons
mv -r 'Windows-XP-Themes/Windows XP Luna' ~/.themes
mv -r 'Windows-XP-Icons/' ~/.icons