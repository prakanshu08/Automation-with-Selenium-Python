#Date:07/10/21
#Gmail Login Automation

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
print("test case started")

driver = webdriver.Chrome()                                             #used to open chrome webbrowser

driver.maximize_window()                                                #used to set the browser window size

driver.delete_all_cookies()                                             #it delete the cookies

driver.get("https://www.gmail.com")                                     #google searches the value

driver.find_element_by_id("identifierId").send_keys("demo@gmail.com")    #writes email in the username
time.sleep(2)

driver.find_element_by_xpath("//span[@class='VfPpkd-vQzf8d'][1]").click()       #click on the next button
time.sleep(2)

driver.find_element_by_name("password").send_keys("test@Demo")                #identify the password text box and enter the value
time.sleep(2)

driver.find_element_by_xpath("//span[contains(text(),'Next')][1]").click(       #click on the next button
time.sleep(2))

driver.close()                                                              #close the browser
print("Gmail login has been successfully completed")