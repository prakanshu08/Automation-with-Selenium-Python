#Date-07/10/2021
#Program to automatic open my personal website

from selenium import webdriver                              #import webdriver lib
import time  
from selenium.webdriver.common.keys import Keys
print("Prakanshu.tech is opening in Chrome Browser")

driver = webdriver.Chrome()                                 #used to open chrome webbrowser
driver.maximize_window()                                    #used to set the browser window size
driver.get("http://prakanshu.tech")                         #google searches the value
time.sleep(2)                                               #wait for 2 sec.
driver.close()                                              #close the browser
print("Task Completed Sucessfully !!")