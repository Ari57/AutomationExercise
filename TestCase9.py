from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, NoSuchFrameException

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # 1. launch browser
driver.maximize_window()
driver.get("https://www.automationexercise.com/") # 2. navigate to url
assert driver.current_url == "https://www.automationexercise.com/" # 3. verify home page

def SearchForProduct():
    ProductsButton = driver.find_element(By.LINK_TEXT, " Products")  # find the Products element
    ProductsButton.click()  # 4. click on Products button
    driver.implicitly_wait(0.5)

    RemoveGoogleAdvert()

    assert driver.current_url == "https://www.automationexercise.com/products" # 5. user is navigated to products page

    SearchProduct = driver.find_element(By.CSS_SELECTOR, "input[id='search_product'")
    RandomProduct = "Blue Top"
    SearchProduct.send_keys(RandomProduct) # 6. Enter product name in search input and click search button

    SearchProductButton = driver.find_element(By.CSS_SELECTOR, "button[id='submit_search'")
    SearchProductButton.click()

    H2Elements = driver.find_elements(By.CSS_SELECTOR, "h2")

    for SearchedProducts in H2Elements:
        if "SEARCHED" in SearchedProducts.text:
            break

    assert SearchedProducts.text == "SEARCHED PRODUCTS" # 7. Verify 'SEARCHED PRODUCTS' is visible

    ProductList = driver.find_element(By.CSS_SELECTOR, "div[class='features_items'") # 6. verify products list is visible

    ProductName = ProductList.find_elements(By.CSS_SELECTOR, "p")
    for product in ProductName:
        if RandomProduct in product.text:
            print(product.text) # 8. Verify all the products related to search are visible

def RemoveGoogleAdvert():
    try:
        driver.switch_to.frame("aswift_4")  # might be buried under a parent
        driver.switch_to.frame("ad_iframe")
        RemoveGoogleAd = driver.find_element(By.CSS_SELECTOR, "div[id='dismiss-button']")  # remove the google ad that pops up
        RemoveGoogleAd.click()
    except (NoSuchElementException, NoSuchFrameException):
        pass

SearchForProduct()

driver.close()
driver.quit()