from selenium.webdriver.common.by import By
from InitFile import Driver
from selenium.common.exceptions import NoSuchElementException, NoSuchFrameException
import time

driver = Driver()

def ProductPage():
    ProductsButton = driver.find_element(By.LINK_TEXT, " Products")  # find the Products element
    ProductsButton.click()  # 4. click on Products button
    time.sleep(20)
    # RemoveGoogleAdvert()
    assert driver.current_url == "https://www.automationexercise.com/products" # 5. user is navigated to products page

def AddProductCart():
    # time.sleep(20)
    driver.execute_script("window.scrollTo(0, 200)") # 5. Scroll down to footer
    AddToCartButton = driver.find_element(By.CSS_SELECTOR, "a[data-product-id='1'")
    AddToCartButton.click()

def RemoveGoogleAdvert():
    try:
        # driver.switch_to.frame("aswift_4")  # might be buried under a parent
        # driver.switch_to.frame("ad_iframe")
        RemoveGoogleAd = driver.find_element(By.CSS_SELECTOR, "div[id='dismiss-button']")  # remove the google ad that pops up
        RemoveGoogleAd.click()
    except (NoSuchElementException, NoSuchFrameException):
        pass
        print("Error")

def main():
    ProductPage()
    # AddProductCart()

main()
