#Date:07/10/21
#Gmail Login Automation

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
print("Logging Into LinkedIn")

driver = webdriver.Chrome()                                             #used to open chrome webbrowser

driver.maximize_window()                                                #used to set the browser window size

driver.delete_all_cookies()                                             #it delete the cookies

driver.get("https://www.linkedin.com/")                                     #google searches the value

driver.find_element_by_id("session_key").send_keys("prakanshu.srivastava@appinventiv.com")    #writes email in the username

driver.find_element_by_id("session_password").send_keys("Admin@@250821")                #identify the password text box and enter the value

driver.find_element_by_class_name("sign-in-form__submit-button").click()       #click on the next button
time.sleep(2)

driver.close()                                                              #close the browser
print("LinkedIn login has been successfully completed")
