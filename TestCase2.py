from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from password import password
from TestCase1 import RemoveGoogleAdvert, DeleteAccount
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.automationexercise.com/") # navigate to url
assert driver.current_url == "https://www.automationexercise.com/"

def Login():
   # RemoveGoogleAdvert()

    SignUpLogin = driver.find_element(By.LINK_TEXT, "Signup / Login")  # find the Signup element
    SignUpLogin.click()  # click on Signup link
    driver.implicitly_wait(0.5)

    # RemoveGoogleAdvert()

    H2Elements = driver.find_elements(By.TAG_NAME, "h2")

    for LoginText in H2Elements:
        if LoginText.text == "Login to your account":
            break

    assert LoginText.text == "Login to your account" # verify that login text exists

    LoginEmail = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-email']")  # find the LoginEmail element
    LoginEmail.send_keys("njds7777@gmail.com")  # type in my name

    LoginPassword = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-password']")  # find the LoginPassword element
    LoginPassword.send_keys(password)  # type in my name

    LoginButton = driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']")  # Find the LoginButton element
    LoginButton.click()

    # RemoveGoogleAdvert()

    LoginName = driver.find_element(By.PARTIAL_LINK_TEXT, "Logged in as")  # Find the "Logged in as 'name'" element

    assert LoginName.text != ""

    DeleteConfirmation = input("Enter 'Y' to delete account: ")
    if DeleteConfirmation == "Y":
        DeleteAccount()

if __name__ == "__main__":
    Login()