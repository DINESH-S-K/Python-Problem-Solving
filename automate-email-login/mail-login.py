# pip install selenium
# importing modules
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# open Google Chrome browser
driver = webdriver.Chrome()

# maximize the window size
driver.maximize_window()

# delete the cookies
driver.delete_all_cookies()

#navigate to the url
driver.get("https://www.google.com")

#identify the user name text box and enter the value
driver.find_element_by_id("identifyId").sendkeys("dineshsrinivasan2001@gmail.com")
time.sleep(2)

# click on the next button
driver.find_element_by_xpath('//*[@id="identifier next"]/div/button/div[2]').click()
time.sleep(3)

# identify the password text box and enter the value
driver.find_element_by_name("password").sendkeys("dinesh75021")
time.sleep(2)

# click on the next button
driver.find_element_by_xpath('//*[@id="password next"]/div/button/div[2]').click()
time.sleep(3)

# close the browser
driver.close()
print("Gmail Successfully login") 