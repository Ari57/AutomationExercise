from selenium.common.exceptions import NoSuchElementException, NoSuchFrameException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from password import password

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # 1. launch browser

driver.maximize_window()

driver.get("https://www.automationexercise.com/") # 2. navigate to url

assert driver.current_url == "https://www.automationexercise.com/" # 3. verify home page

def SignUp():
    RemoveGoogleAdvert()

    SignUpLogin = driver.find_element(By.LINK_TEXT, "Signup / Login") # find the Signup element
    SignUpLogin.click() # 4. click on Signup button
    driver.implicitly_wait(0.5)

    RemoveGoogleAdvert()

    NewUsers = driver.find_elements(By.TAG_NAME, "h2")

    for NewUser in NewUsers:
        if NewUser.text == "New User Signup!":  # verify that new user signup exists, it will raise an exception otherwise
            break

    assert NewUser.text == "New User Signup!" # 5. Verify New User Signup is visible

    SignUpName = driver.find_element(By.CSS_SELECTOR, "input[name='name']") # find the Signup Name element
    SignUpName.send_keys("Nathan") # 6. Enter name and email address
    SignupEmail = driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']") # find the Signup Email element
    SignupEmail.send_keys("njds7777@gmail.com") # 6. Enter name and email address
    SignUpButton = driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']")
    SignUpButton.click() # 7. Click Signup button

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
    except (UnboundLocalError, AttributeError):
        pass

    EnterAccountInfo = driver.find_element(By.CSS_SELECTOR, "h2[class='title text-center']")

    assert EnterAccountInfo.text == "ENTER ACCOUNT INFORMATION" # 8. Verify that "ENTER ACCOUNT INFO" is visible

    # 9. Fill in details (below)

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
    Newsletter.click() # 10. Select newsletter checkbox

    SpecialOffers = driver.find_element(By.CSS_SELECTOR, "input[id='optin']") # Find the Male option
    SpecialOffers.click() # 11. Select offers checkbox

    # 12. Fill in details (below)

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
    CreateAccount.click() # 13. Click "create account" button

    RemoveGoogleAdvert()

    AccountCreated = driver.find_element(By.CSS_SELECTOR, "h2[data-qa='account-created']")
    assert AccountCreated.text == "ACCOUNT CREATED!" # 14. Verify that "ACCOUNT CREATED" exists

    AccountCreatedContinue = driver.find_element(By.CSS_SELECTOR, "a[data-qa='continue-button']")
    AccountCreatedContinue.click() # 15. Click "Continue" button

    RemoveGoogleAdvert()

    LoginName = driver.find_element(By.PARTIAL_LINK_TEXT, "Logged in as")  # Find the "Logged in as 'name'" element

    assert "Logged in as" in LoginName.text # 16. Verify that "Logged in as username" is visible

# below Login function is used to Log in, if account already exists

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

    assert LoginName.text != ""

    DeleteConfirmation = input("Enter 'Y' to delete account: ")
    if DeleteConfirmation == "Y":
        DeleteAccount()

    return

def DeleteAccount():

    driver.get("https://www.automationexercise.com/") # navigate back to home page

    DeleteAccountButton = driver.find_element(By.PARTIAL_LINK_TEXT, "Delete Account")
    DeleteAccountButton.click() # 17. Click "Delete Account Button"

    assert driver.current_url == "https://www.automationexercise.com/delete_account"
    AccountDeleted = driver.find_element(By.CSS_SELECTOR, "h2[data-qa='account-deleted']")
    assert AccountDeleted.text == "ACCOUNT DELETED!" # 18. Verify that "ACCOUNT DELETED" is visible

    AccountDeleteContinue = driver.find_element(By.CSS_SELECTOR, "a[data-qa='continue-button']")
    AccountDeleteContinue.click()  # 18. Click "Continue" button

def RemoveGoogleAdvert():
    # every time the page changes, call this function
    try:
        driver.switch_to.frame('ad_iframe')
        RemoveGoogleAd = driver.find_element(By.CSS_SELECTOR, "div[id='dismiss-button']")  # remove the google ad that pops up
        RemoveGoogleAd.click()
    except (NoSuchElementException, NoSuchFrameException):
        print("Remove Google Ad error")
        pass

if __name__ == "__main__":
    SignUp()
    # Login()

driver.close()
driver.quit()
