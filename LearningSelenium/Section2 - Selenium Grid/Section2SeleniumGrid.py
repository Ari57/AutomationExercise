from selenium import webdriver
from selenium.webdriver.common.by import By
from time import time
from RemoteServerIP import RemoteIP

ChromeOptions = webdriver.ChromeOptions()
driver = webdriver.Remote(command_executor=RemoteIP, options=ChromeOptions)

driver.get("https://selenium-blog.herokuapp.com/signup")

driver.maximize_window()
seconds = str(int(time()))

def SignUpUser(): # signing up a new user
    Username = driver.find_element(By.CSS_SELECTOR, "input[id='user_username']")
    user = "user" + seconds
    Username.send_keys(user)

    Email = driver.find_element(By.CSS_SELECTOR, "input[id='user_email']")
    Email.send_keys("example" + seconds + "@example.com")

    Password = driver.find_element(By.CSS_SELECTOR, "input[id='user_password']")
    Password.send_keys("password" + seconds)

    SignUpButton = driver.find_element(By.CSS_SELECTOR, "input[id='submit']")
    SignUpButton.click()

    driver.implicitly_wait(0.5)

    SignUpSuccess = driver.find_element(By.CSS_SELECTOR, "div[id='flash_success']")
    assert SignUpSuccess.text == "Welcome to the alpha blog " + user

SignUpUser()

driver.close()
driver.quit()


# java -jar '.\LearningSelenium\Section2 - Selenium Grid\selenium-server-4.9.0.jar' hub
# java -jar '.\LearningSelenium\Section2 - Selenium Grid\selenium-server-4.9.0.jar' node --port 5555
# make sure port number is unique for each node

