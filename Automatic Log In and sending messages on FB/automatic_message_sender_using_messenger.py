#another project is more efficient than it is which name is """Automatic_sending_message_through_url.py"""

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

# Open Facebook login page
driver.get("https://www.facebook.com/")
time.sleep(4)


"""
copy url of your profile= https://www.facebook.com/durjoybarua.durjoybarua.754
then remove front portion and the user name will be = durjoybarua.durjoybarua.
then push or put it to the user_name variable then put password
"""
user_name = "***********"
password = "*********"

# Find and fill in the login form
driver.find_element(By.ID, "email").send_keys(user_name)
driver.find_element(By.ID, "pass").send_keys(password)

# Submit the login form
driver.find_element(By.NAME,"login").click()

# Wait for login to complete and the page to load
time.sleep(5)


#this the url of messenger
profile_url = "https://www.facebook.com/messages/t/100063575775826"
driver.get(profile_url)
time.sleep(5)

"""
it will be little bit complex for u if you don't know the html if you don't know the html
then move to the next project which is more easier 
here you have to put the xpath(from messenger) of person which one you want to send message
"""
texting = driver.find_element(By.XPATH, '//div[@aria-label="Message" and @contenteditable="true"]')
texting.send_keys("Hey, how are you??")
#this for enter or submit the message
texting.send_keys(Keys.RETURN)
time.sleep(5)

# Close the browser
driver.quit()
