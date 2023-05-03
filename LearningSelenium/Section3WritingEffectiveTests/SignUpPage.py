from selenium.webdriver.common.by import By
from time import time

class SignUpPage:
    # css selectors

    def __init__(self, driver): # constructor
        self.driver = driver
        self.USERNAMEFIELD = "input[id='user_username']"
        self.EMAILFIELD = "input[id='user_email']"
        self.PASSWORDFIELD = "input[id='user_password']"
        self.SUBMITBUTTON = "input[id='submit']"
        self.seconds = str(int(time()))
        self.user = "user" + self.seconds
        self.email = "example" + self.seconds + "@example.com"
        self.password = "password" + self.seconds

    def EnterUsername(self, user):
        UsernameField = self.driver.find_element(By.CSS_SELECTOR, self.USERNAMEFIELD)
        UsernameField.send_keys(user)

    def EnterEmail(self, email):
        EmailField = self.driver.find_element(By.CSS_SELECTOR, self.EMAILFIELD)
        EmailField.send_keys(email)

    def EnterPassword(self, password):
        PasswordField = self.driver.find_element(By.CSS_SELECTOR, self.PASSWORDFIELD)
        PasswordField.send_keys(password)

    def SubmitForm(self):
        SignUpButton = self.driver.find_element(By.CSS_SELECTOR, self.SUBMITBUTTON)
        SignUpButton.click()


    def SignUpUser(self): # signing up a new user
        obj = SignUpPage()
        obj.EnterUsername(self.user)
        obj.EnterPassword(self.password)
        obj.EnterEmail(self.email)
        obj.SubmitForm()
        self.driver.implicitly_wait(0.5)
        obj.VerifyBannerText(self.user)

# SignUpObject = SignUpPage()
# SignUpObject.SignUpUser()
#
# driver.close()
# driver.quit()

