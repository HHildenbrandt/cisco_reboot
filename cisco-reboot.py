#!/usr/bin/python3

# Selenium script to restart CISCO modem
# Hanno 2022

import sys
import getopt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options


def main(argv):
    url = " http://192.168.178.1/"
    name = "hanno"
    passw = "TRfrakt01CISC"
    path = r"/usr/bin/firefox"

    try:
        opts, args = getopt.getopt(argv, '', ["hot","headless"])
    except getopt.GetoptError:
        print('cisco-reboot.py [--hot] [--headless]')
        sys.exit(2)

    hot, headless = False, False    
    for opt, arg in opts:
        if opt == "--hot":
            hot = True
        if opt == "--headless":
            headless = True

    options = Options()
    options.headless = headless
    if headless:
        options.add_argument('--disable-gpu')
        
    driver = webdriver.Firefox(options=options)
        
    driver.get(url + "login_zig.asp")
    driver.set_window_size(1024, 720)

    driver.find_element(By.ID, "Zigloginnaam").click()
    driver.find_element(By.ID, "Zigloginnaam").send_keys(name)
    driver.find_element(By.ID, "Zigpassword").send_keys(passw)
    driver.find_element(By.LINK_TEXT, "Inloggen >").click()

    driver.get(url + "Devicerestart.asp")
    driver.find_element(By.NAME, "mtenRestore").click()
    alert = WebDriverWait(driver, 5).until(expected_conditions.alert_is_present())
    assert alert.text == "Select OK to restart the device."
    if hot:
        alert.accept()
        print("Restart device confirmed.")
    else:
        alert.dismiss()
        print("Restart device dismissed. Use --hot")
    driver.quit()
    print(hot, headless)

if __name__ == "__main__":
   main(sys.argv[1:])
