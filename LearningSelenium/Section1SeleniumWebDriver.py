from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import time
from Section3WritingEffectiveTests.SignUpPage import SignUpPage
from Section3WritingEffectiveTests.UserPage import UsersPage

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # launch browser
driver.maximize_window()

driver.get("https://selenium-blog.herokuapp.com/signup")

def EnterUsername(user):
    UsernameField = driver.find_element(By.CSS_SELECTOR, "input[id='user_username']")
    UsernameField.send_keys(user)

def EnterEmail(email):
    EmailField = driver.find_element(By.CSS_SELECTOR, "input[id='user_email']")
    EmailField.send_keys(email)

def EnterPassword(password):
    PasswordField = driver.find_element(By.CSS_SELECTOR, "input[id='user_password']")
    PasswordField.send_keys(password)

def SubmitForm():
    SignUpButton = driver.find_element(By.CSS_SELECTOR, "input[id='submit']")
    SignUpButton.click()

def VerifyBannerText(user):
    SignUpSuccess = driver.find_element(By.CSS_SELECTOR, "div[id='flash_success']")
    assert SignUpSuccess.text == "Welcome to the alpha blog " + user

def SignUpUser(): # signing up a new user
    seconds = str(int(time()))
    user = "user" + seconds
    email = "example" + seconds + "@example.com"
    password = "password" + seconds

    SignupPage = SignUpPage(driver)

    SignupPage.EnterUsername(user)
    SignupPage.EnterPassword(password)
    SignupPage.EnterEmail(email)

    SignupPage.SubmitForm()
    driver.implicitly_wait(0.5)
    UserPage = UsersPage(driver)
    UserPage.VerifyBannerText(user)

SignUpUser()

driver.close()
driver.quit()
