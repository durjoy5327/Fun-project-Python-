
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

path = "K:/chromedriver-win64/chromedriver.exe"
s = Service(path)

# Chrome options to block notifications
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

# Create a new instance of Chrome with options
driver = webdriver.Chrome(service=s, options=chrome_options)


driver.get("https://www.facebook.com/")
time.sleep(4)


"""
copy url of your profile= https://www.facebook.com/durjoybarua.durjoybarua.754
then remove front portion and the user name will be = durjoybarua.durjoybarua.
then push or put it to the user_name variable then put password
"""
user_name = "**************"
password = "**********"

# Find and fill in the login form
driver.find_element(By.ID, "email").send_keys(user_name)
driver.find_element(By.ID, "pass").send_keys(password)

# Submit the login form
driver.find_element(By.NAME, "login").click()

# Wait for login to complete and the page to load
time.sleep(5)

# Give here the url of that profile which one you want to send messages copy url and put it
profile_url = "*************"
driver.get(profile_url)

# Click the Message button
driver.find_element(By.XPATH, '//div[@aria-label="Message"]').click()

# Wait for the message input field to become interactable
time.sleep(2)

# Locate the new message input field
message_input = driver.find_element(By.XPATH, '//div[@aria-label="Message" and @contenteditable="true"]')
    
# Click the input field to focus
message_input.click()
    
# Send the message
message_input.send_keys("Hello How are You??")
message_input.send_keys(Keys.RETURN)


# Close the browser
driver.quit()