from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from password import fakePassword
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, NoSuchFrameException

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # 1. launch browser
driver.maximize_window()

driver.get("https://www.automationexercise.com/") # 2. navigate to url
assert driver.current_url == "https://www.automationexercise.com/" # 3. verify home page is visible

def LoginIncorrectDetails():
    SignUpLogin = driver.find_element(By.LINK_TEXT, "Signup / Login")  # find the Signup element
    SignUpLogin.click()  # 4. click on Signup button
    driver.implicitly_wait(0.5)

    H2Elements = driver.find_elements(By.TAG_NAME, "h2")

    for LoginText in H2Elements:
        if LoginText.text == "Login to your account":
            break

    assert LoginText.text == "Login to your account"  # 5. verify that login text exists

    LoginEmail = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-email']")
    LoginEmail.send_keys("email@email.com")  # # 6. Enter incorrect email address

    LoginPassword = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-password']")
    LoginPassword.send_keys(fakePassword)  # 6. Enter incorrect password

    LoginButton = driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']")
    LoginButton.click()  # 7. Click on login button

    driver.implicitly_wait(0.5)

    try:
        driver.switch_to.frame("aswift_4")  # might be buried under a parent
        driver.switch_to.frame("ad_iframe")
        RemoveGoogleAd = driver.find_element(By.CSS_SELECTOR, "div[id='dismiss-button']")  # remove the google ad that pops up
        RemoveGoogleAd.click()
    except (NoSuchElementException, NoSuchFrameException):
        pass

    IncorrectDetails = driver.find_element(By.CSS_SELECTOR, "p[style='color: red;']")  # Find the "Incorrect details" text

    assert IncorrectDetails.text == "Your email or password is incorrect!" # 8. verify that the "incorrect email/password" text is visible

LoginIncorrectDetails()