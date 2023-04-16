from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from password import password
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, NoSuchFrameException


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # 1. launch browser
driver.maximize_window()

driver.get("https://www.automationexercise.com/") # 2. navigate to url
assert driver.current_url == "https://www.automationexercise.com/" # 3. verify home page is visible

def LogOut():
    SignUpLogin = driver.find_element(By.LINK_TEXT, "Signup / Login")  # find the Signup element
    SignUpLogin.click()  # 4. click on Signup/Login button
    driver.implicitly_wait(0.5)

    RemoveGoogleAdvert()

    H2Elements = driver.find_elements(By.TAG_NAME, "h2")

    for LoginText in H2Elements:
        if LoginText.text == "Login to your account":
            break

    assert LoginText.text == "Login to your account"  # 5. verify that login text exists

    LoginEmail = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-email']")  # find the LoginEmail element
    LoginEmail.send_keys("njds7777@gmail.com")  # 6. Enter correct email address

    LoginPassword = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-password']")
    LoginPassword.send_keys(password)  # 6. Enter correct password

    LoginButton = driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']")  # Find the LoginButton element
    LoginButton.click()  # 7. Click on login button

    RemoveGoogleAdvert()

    LoginName = driver.find_element(By.PARTIAL_LINK_TEXT, "Logged in as")  # Find the "Logged in as 'name'" element

    assert "Logged in as" in LoginName.text  # 8. Verify that "logged in as username" is visible

    LogOutButton = driver.find_element(By.PARTIAL_LINK_TEXT, "Logout")
    LogOutButton.click() # 9. click "Logout" button

    RemoveGoogleAdvert()

    assert driver.current_url == "https://www.automationexercise.com/login"  # 10. verify user is navigated to login page

def RemoveGoogleAdvert():
    try:
        driver.switch_to.frame("aswift_4")  # might be buried under a parent
        driver.switch_to.frame("ad_iframe")
        RemoveGoogleAd = driver.find_element(By.CSS_SELECTOR, "div[id='dismiss-button']")  # remove the google ad that pops up
        RemoveGoogleAd.click()
    except (NoSuchElementException, NoSuchFrameException):
        pass

LogOut()








