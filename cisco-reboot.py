# Selenium script to restart CISCO modem
# Hanno 2022

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

url = " http://192.168.178.1/"

driver = webdriver.Firefox()
driver.get(url + "login_zig.asp")
driver.set_window_size(1024, 720)

driver.find_element(By.ID, "Zigloginnaam").click()
driver.find_element(By.ID, "Zigloginnaam").send_keys("hanno")
driver.find_element(By.ID, "Zigpassword").send_keys("TRfrakt01CISC")
driver.find_element(By.LINK_TEXT, "Inloggen >").click()

driver.get(url + "Devicerestart.asp")
#driver.find_element(By.CSS_SELECTOR, "a > img").click()
#driver.find_element(By.CSS_SELECTOR, ".MainTabL23").click()
#driver.find_element(By.CSS_SELECTOR, ".SubTabL23").click()
driver.find_element(By.NAME, "mtenRestore").click()
assert driver.switch_to.alert.text == "Select OK to restart the device."
driver.switch_to.alert.dismiss()
  
#driver.quit()
