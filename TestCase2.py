from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from password import password
from TestCase1 import RemoveGoogleAdvert, DeleteAccount
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # 1. Launch Browser

driver.maximize_window()

driver.get("https://www.automationexercise.com/") # 2. navigate to url
assert driver.current_url == "https://www.automationexercise.com/" # 3. verify that home page is visible

def LoginCorrectDetails():
    SignUpLogin = driver.find_element(By.LINK_TEXT, "Signup / Login")  # find the Signup element
    SignUpLogin.click()  # 4. click on Signup button
    driver.implicitly_wait(0.5)

    # RemoveGoogleAdvert()

    H2Elements = driver.find_elements(By.TAG_NAME, "h2")

    for LoginText in H2Elements:
        if LoginText.text == "Login to your account":
            break

    assert LoginText.text == "Login to your account" # 5. verify that login text exists

    LoginEmail = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-email']")  # find the LoginEmail element
    LoginEmail.send_keys("njds7777@gmail.com")  # # 6. Enter correct email address

    LoginPassword = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-password']")
    LoginPassword.send_keys(password)  # 6. Enter correct password

    LoginButton = driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']")  # Find the LoginButton element
    LoginButton.click() # 7. Click on login button

    # RemoveGoogleAdvert()

    LoginName = driver.find_element(By.PARTIAL_LINK_TEXT, "Logged in as")  # Find the "Logged in as 'name'" element

    assert "Logged in as" in LoginName.text # 8. Verify that "logged in as username" is visible

    DeleteConfirmation = input("Enter 'Y' to delete account: ")
    if DeleteConfirmation == "Y":
        DeleteAccount() # 9. click delete account button/10. verify that "ACCOUNT DELETED!" is visible

if __name__ == "__main__":
    LoginCorrectDetails()