import selenium.common.exceptions
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from password import password

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    driver.get("https://www.automationexercise.com/") # navigate to url
except selenium.common.exceptions.WebDriverException: # will raise an exception if link is invalid (if page exists)
    sys.exit(1) # exit if link is invalid

SignUp = driver.find_element(By.LINK_TEXT, "Signup / Login") # find the Signup element
SignUp.click() # click on Signup link
driver.implicitly_wait(0.5)

if driver.current_url == "https://www.automationexercise.com/login":
    pass # we have the correct url
else:
    sys.exit(1) # exit if wrong url is found

NewUsers = driver.find_elements(By.TAG_NAME, "h2")
for NewUser in NewUsers:
    if NewUser.text == "New User Signup!": # verify that new user signup exists, it will raise an exception otherwise
        break

SignUpName = driver.find_element(By.CSS_SELECTOR, "input[name='name']") # find the Signup Name element
SignUpName.send_keys("Nathan") # type in my name
SignupEmail = driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']") # find the Signup Email element
SignupEmail.send_keys("njds7777@gmail.com") # type in my email
SignUpButton = driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']") # find the Signup Button element
SignUpButton.click() # click on signup button

EnterAccountInfo = driver.find_element(By.CSS_SELECTOR, "h2[class='title text-center']") # Find the "EnterAccountInfo" text
if EnterAccountInfo.text != "ENTER ACCOUNT INFORMATION":
    sys.exit(1) # exit if it's not found on the page

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

driver.implicitly_wait(0.5) # need to wait for element to load
Newsletter = driver.find_element(By.CSS_SELECTOR, "input[id='newsletter']") # Enable Newsletter option
Newsletter.click()

driver.implicitly_wait(0.5) # need to wait for element to load
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

CreateAccount = driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']")
CreateAccount.click()

# just finished step 13
driver.close()
driver.quit()
