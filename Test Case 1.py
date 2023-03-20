import selenium.common.exceptions
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    driver.get("https://www.automationexercise.com/") # navigate to url
except selenium.common.exceptions.WebDriverException: # will raise an exception if link is invalid (if page exists)
    sys.exit(1) # exit if link is invalid

SignUp = driver.find_element(By.LINK_TEXT, "Signup / Login") # find the Signup element
SignUp.click() # click on Signup link
driver.implicitly_wait(0.5)

if driver.current_url == "https://www.automationexercise.com/login":
    pass # we have the correct url
else:
    sys.exit(1) # exit if wrong url is found

# SignUpForm = driver.find_elements(By.CLASS_NAME, "signup-form")

NewUsers = driver.find_elements(By.TAG_NAME, "h2")
for NewUser in NewUsers:
    if NewUser.text == "New User Signup!": # verify that new user signup exists, it will raise an exception otherwise
        break

# just finished step 5
driver.close()
driver.quit()