from selenium.webdriver.common.by import By
from InitFile import Driver

driver = Driver()

def CartPage():
    CartButton = driver.find_element(By.LINK_TEXT, "Cart")  # find the Products element
    CartButton.click() # 4. Click 'Cart' button
    driver.execute_script("window.scrollTo(0, 1080)") # 5. Scroll down to footer

def VerifySubscriptionText():
    FooterWidget = driver.find_element(By.CSS_SELECTOR, "div[class='single-widget'")
    SubscriptionText = FooterWidget.find_element(By.CSS_SELECTOR, "h2")
    assert SubscriptionText.text == "SUBSCRIPTION"  # 6. Verify text 'SUBSCRIPTION'

def EnterEmail():
    SubscriptionEmail = driver.find_element(By.CSS_SELECTOR, "input[id='susbscribe_email'") # miss-spelt on purpose
    SubscriptionEmail.send_keys("njds7777@gmail.com")  # 7. Enter email address in input and click arrow button

def SubscribeButton():
    SubscriptionButton = driver.find_element(By.CSS_SELECTOR, "button[id='subscribe'")
    SubscriptionButton.click()

def VerifySubscriptionConfirmation():
    SubscribeSuccess = driver.find_element(By.CSS_SELECTOR, "div[id='success-subscribe'")
    assert SubscribeSuccess.text == "You have been successfully subscribed!" # 8. Verify success message 'You have been successfully subscribed!' is visible

def main():
    CartPage()
    VerifySubscriptionText()
    EnterEmail()
    SubscribeButton()
    VerifySubscriptionConfirmation()

main()
