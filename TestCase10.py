from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, NoSuchFrameException

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # 1. launch browser
driver.maximize_window()
driver.get("https://www.automationexercise.com/") # 2. navigate to url
assert driver.current_url == "https://www.automationexercise.com/" # 3. verify home page

def VerifySubscription():
    driver.execute_script("window.scrollTo(0, 1080)") # 4. Scroll down to footer

    FooterWidget = driver.find_element(By.CSS_SELECTOR, "div[class='single-widget'")
    SubscriptionText = FooterWidget.find_element(By.CSS_SELECTOR, "h2")
    assert SubscriptionText.text == "SUBSCRIPTION" # 5. Verify text 'SUBSCRIPTION'

    SubscriptionEmail = driver.find_element(By.CSS_SELECTOR, "input[id='susbscribe_email'")
    SubscriptionEmail.send_keys("njds7777@gmail.com") # 6. Enter email address in input and click arrow button

    SubscriptionButton = driver.find_element(By.CSS_SELECTOR, "button[id='subscribe'")
    SubscriptionButton.click() # 6. Enter email address in input and click arrow button

    SubscribeSuccess = driver.find_element(By.CSS_SELECTOR, "div[id='success-subscribe'")
    assert SubscribeSuccess.text == "You have been successfully subscribed!"

def RemoveGoogleAdvert():
    try:
        driver.switch_to.frame("aswift_4")  # might be buried under a parent
        driver.switch_to.frame("ad_iframe")
        RemoveGoogleAd = driver.find_element(By.CSS_SELECTOR, "div[id='dismiss-button']")  # remove the google ad that pops up
        RemoveGoogleAd.click()
    except (NoSuchElementException, NoSuchFrameException):
        pass

VerifySubscription()

driver.close()
driver.quit()