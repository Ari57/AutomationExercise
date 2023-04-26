from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # launch browser
driver.maximize_window()

seconds = str(int(time()))

driver.get("https://selenium-blog.herokuapp.com/signup")

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
