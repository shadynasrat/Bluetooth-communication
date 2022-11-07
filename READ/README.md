''' bash
sudo service bluetooth restart
sudo systemctl enable bluetooth
sudo systemctl start bluetooth
sudo systemctl status bluetooth
rfkill unblock bluetooth

sudo rfcomm release rfcomm0
sudo rfcomm bind 0 E8:6D:CB:EC:37:89
'''
