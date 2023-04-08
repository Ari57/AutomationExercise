from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # 1. launch browser

driver.maximize_window()

driver.get("https://www.automationexercise.com/") # 2. navigate to url

assert driver.current_url == "https://www.automationexercise.com/" # 3. verify home page

def RegisterExistingEmail():
    SignUpLogin = driver.find_element(By.LINK_TEXT, "Signup / Login")  # find the Signup element
    SignUpLogin.click()  # 4. click on Signup button
    driver.implicitly_wait(0.5)

    NewUsers = driver.find_elements(By.TAG_NAME, "h2")

    for NewUser in NewUsers:
        if NewUser.text == "New User Signup!":  # verify that new user signup exists, it will raise an exception otherwise
            break

    assert NewUser.text == "New User Signup!"  # 5. Verify New User Signup is visible

    SignUpName = driver.find_element(By.CSS_SELECTOR, "input[name='name']")
    SignUpName.send_keys("Nathan")  # 6. Enter name and email address
    SignupEmail = driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SignupEmail.send_keys("njds7777@gmail.com")  # 6. Enter name and email address
    SignUpButton = driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']")
    SignUpButton.click()  # 7. Click Signup button

    driver.implicitly_wait(0.5)  # need to wait for account exist element to load

    AccountAlreadyExist = driver.find_element(By.CSS_SELECTOR, "p[style='color: red;']")

    assert AccountAlreadyExist.text == "Email Address already exist!"

RegisterExistingEmail()


