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
sudo apt install --no-install-recommends --no-install-suggests python3-selenium
sudo apt install --no-install-recommends --no-install-suggests xvfb python3-xvfbwrapper libgtk-3-0 libdbus-glib-1-2
```

# selenium webdriver firefox
wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux32.tar.gz
tar -x geckodriver -zf geckodriver-v0.30.0-linux32.tar.gz
sudo mv geckodriver /usr/bin/

pip3 install PyOpenSSL
pip3 install selenium
pip3 install --upgrade requests
```

# setup

Add the username and password for the modem in `.bash.rc`

```bash
# .bashrc
ZiggoUser="user name"
ZiggoPasw="password"
```
