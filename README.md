# cisco_reboot

## dependencies

```bash
# headless firefox
```bash
sudo apt install xvfb
sudo apt install software-properties-common
sudo add-apt-repository ppa:mozillateam/ppa
sudo apt update
sudo apt install firefox

# or?
```
sudo apt install --no-install-recommends --no-install-suggests python3-selenium
sudo apt install --no-install-recommends --no-install-suggests xvfb python3-xvfbwrapper libgtk-3-0 libdbus-glib-1-2
```

# selenium webdriver firefox
```
wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux32.tar.gz
tar -x geckodriver -zf geckodriver-v0.30.0-linux32.tar.gz
sudo mv geckodriver /usr/local/bin/

pip3 install PyOpenSSL
pip3 install selenium
pip3 install --upgrade requests
```

# setup

## Create a bash script `cisco-reboot.sh'

```bash
!/usr/bin/bash

export DISPLAY=:0
export ZiggoUser="user"
export ZiggoPassw="password"
export PATH=/usr/local/bin:$PATH
/usr/bin/python3 /home/hanno/cisco_reboot/cisco-reboot.py --headless --hot
```

## Cron
```
0 5 * * * /usr/bin/bash -c /home/hanno/cisco_reboot/cisco-reboot.sh
```

