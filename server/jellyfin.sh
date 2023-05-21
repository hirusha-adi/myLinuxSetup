sudo apt install curl -y
curl https://repo.jellyfin.org/install-debuntu.sh | sudo bash
sudo systemctl enable jellyfin.service --now
sudo systemctl start jellyfin.service
sudo ufw disable