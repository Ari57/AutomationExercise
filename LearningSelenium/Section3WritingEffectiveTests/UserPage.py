from selenium.webdriver.common.by import By

class UsersPage:
    def __init__(self, driver):
        self.driver = driver
        self.BANNER = "div[id='flash_success']"

    def VerifyBannerText(self, user):
        SignUpSuccess = self.driver.find_element(By.CSS_SELECTOR, self.BANNER)
        assert SignUpSuccess.text == "Welcome to the alpha blog " + user
