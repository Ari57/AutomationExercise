import sys
import time
from selenium.common.exceptions import WebDriverException, NoSuchElementException, NoSuchFrameException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from password import password

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

try:
    driver.get("https://www.automationexercise.com/") # navigate to url
except WebDriverException: # will raise an exception if link is invalid (if page exists)
    sys.exit(1) # exit if link is invalid

def SignUp():
    RemoveGoogleAdvert()

    SignUpLogin = driver.find_element(By.LINK_TEXT, "Signup / Login") # find the Signup element
    SignUpLogin.click() # click on Signup link
    driver.implicitly_wait(0.5)

    RemoveGoogleAdvert()

    assert driver.current_url == "https://www.automationexercise.com/login"

    NewUsers = driver.find_elements(By.TAG_NAME, "h2")

    for NewUser in NewUsers:
        if NewUser.text == "New User Signup!":  # verify that new user signup exists, it will raise an exception otherwise
            break

    assert NewUser.text == "New User Signup!"

    SignUpName = driver.find_element(By.CSS_SELECTOR, "input[name='name']") # find the Signup Name element
    SignUpName.send_keys("Nathan") # type in my name
    SignupEmail = driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']") # find the Signup Email element
    SignupEmail.send_keys("njds7777@gmail.com") # type in my email
    SignUpButton = driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']") # find the Signup Button element
    SignUpButton.click() # click on signup button

    RemoveGoogleAdvert()

    driver.implicitly_wait(0.5) # need to wait for account exist element to load

    try:
        AccountAlreadyExist = driver.find_element(By.CSS_SELECTOR, "p[style='color: red;']")  # Find the "AccountAlreadyExist" text, if it exists
    except NoSuchElementException:
        pass

    try:
        if AccountAlreadyExist.text == "Email Address already exist!":
            Login()
            return
    except (UnboundLocalError, AttributeError) as error:
        pass

    EnterAccountInfo = driver.find_element(By.CSS_SELECTOR, "h2[class='title text-center']") # Find the "EnterAccountInfo" text

    assert EnterAccountInfo.text == "ENTER ACCOUNT INFORMATION" # verify that it exists

    SignUpGender = driver.find_element(By.CSS_SELECTOR, "input[id='id_gender1']") # Find the Male option
    SignUpGender.click()
    SignUpPassword = driver.find_element(By.CSS_SELECTOR, "input[data-qa='password']") # find the Signup Password element
    SignUpPassword.send_keys(password)

    Day = Select(driver.find_element(By.CSS_SELECTOR, "select[data-qa='days']"))
    Day.select_by_value("5")

    Month = Select(driver.find_element(By.CSS_SELECTOR, "select[data-qa='months']"))
    Month.select_by_value("2")

    Year = Select(driver.find_element(By.CSS_SELECTOR, "select[data-qa='years']"))
    Year.select_by_value("2003") # website seems to store it as a str

    driver.implicitly_wait(5) # need to wait for element to load

    driver.execute_script("window.scrollTo(0, 540)")

    Newsletter = driver.find_element(By.CSS_SELECTOR, "input[id='newsletter']") # Enable Newsletter option
    Newsletter.click()

    SpecialOffers = driver.find_element(By.CSS_SELECTOR, "input[id='optin']") # Find the Male option
    SpecialOffers.click()

    FirstName = driver.find_element(By.CSS_SELECTOR, "input[data-qa='first_name']")
    FirstName.send_keys("Nathan") # type in my name

    LastName = driver.find_element(By.CSS_SELECTOR, "input[data-qa='last_name']")
    LastName.send_keys("Last Name")

    Company = driver.find_element(By.CSS_SELECTOR, "input[data-qa='company']")
    Company.send_keys("Example Company")

    Address = driver.find_element(By.CSS_SELECTOR, "input[data-qa='address']")
    Address.send_keys("Example Address")

    Country = Select(driver.find_element(By.CSS_SELECTOR, "select[data-qa='country']"))
    Country.select_by_value("United States")

    State = driver.find_element(By.CSS_SELECTOR, "input[data-qa='state']")
    State.send_keys("Example State")

    City = driver.find_element(By.CSS_SELECTOR, "input[data-qa='city']")
    City.send_keys("London")

    Zipcode = driver.find_element(By.CSS_SELECTOR, "input[data-qa='zipcode']")
    Zipcode.send_keys("Example Zipcode")

    PhoneNumber = driver.find_element(By.CSS_SELECTOR, "input[data-qa='mobile_number']")
    PhoneNumber.send_keys("Example Phone Number")

    driver.execute_script("window.scrollTo(0, 1080)")

    CreateAccount = driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']")
    CreateAccount.click()

    RemoveGoogleAdvert()

    assert driver.current_url == "https://www.automationexercise.com/account_created" # make sure it's on the right page
    AccountCreated = driver.find_element(By.CSS_SELECTOR, "h2[data-qa='account-created']")
    assert AccountCreated.text == "ACCOUNT CREATED!"

    AccountCreatedContinue = driver.find_element(By.CSS_SELECTOR, "a[data-qa='continue-button']")
    AccountCreatedContinue.click()

    RemoveGoogleAdvert()

    LoginName = driver.find_element(By.PARTIAL_LINK_TEXT, "Logged in as")  # Find the "Logged in as 'name'" element

    assert "Logged in as" in LoginName.text # check to see if login failed or not

def Login():
    driver.get("https://www.automationexercise.com/login") # navigate to login page url

    RemoveGoogleAdvert()

    LoginEmail = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-email']")  # find the LoginEmail element
    LoginEmail.send_keys("njds7777@gmail.com")  # type in my name

    LoginPassword = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-password']")  # find the LoginPassword element
    LoginPassword.send_keys(password)  # type in my name

    LoginButton = driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']")  # Find the LoginButton element
    LoginButton.click()

    RemoveGoogleAdvert()

    LoginName = driver.find_element(By.PARTIAL_LINK_TEXT, "Logged in as")  # Find the "Logged in as 'name'" element
    if LoginName.text == "":
        sys.exit(1) # login failed

    DeleteConfirmation = input("Enter 'Y' to delete account: ")
    if DeleteConfirmation == "Y":
        DeleteAccount()

    return
def DeleteAccount():
    driver.get("https://www.automationexercise.com/") # navigate back to home page

    DeleteAccountButton = driver.find_element(By.PARTIAL_LINK_TEXT, "Delete Account")
    DeleteAccountButton.click()

    # time.sleep(120)

    # RemoveGoogleAdvert()

    assert driver.current_url == "https://www.automationexercise.com/delete_account"
    AccountDeleted = driver.find_element(By.CSS_SELECTOR, "h2[data-qa='account-deleted']")
    assert AccountDeleted.text == "ACCOUNT DELETED!"

def RemoveGoogleAdvert():
    # every time the page changes, call this function
    try:
        driver.switch_to.frame('ad_iframe')
        RemoveGoogleAd = driver.find_element(By.CSS_SELECTOR, "div[id='dismiss-button']")  # remove the google ad that pops up
        RemoveGoogleAd.click()
    except (NoSuchElementException, NoSuchFrameException) as error:
        print("Remove Google Ad error")
        pass

if __name__ == "__main__":
    SignUp()
    # Login()

driver.close()
driver.quit()

# TODO click past adverts that come up
