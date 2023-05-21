sudo apt install openssh-server -y
sudo systemctl enable sshd --now
sudo systemctl start sshd