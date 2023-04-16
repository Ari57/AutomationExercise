from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, NoSuchFrameException

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # 1. launch browser
driver.maximize_window()
driver.get("https://www.automationexercise.com/") # 2. navigate to url
assert driver.current_url == "https://www.automationexercise.com/" # 3. verify home page

def VerifyAllProducts():
    ProductsButton = driver.find_element(By.LINK_TEXT, " Products")  # find the Products element
    ProductsButton.click()  # 4. click on Products button
    driver.implicitly_wait(0.5)

    RemoveGoogleAdvert()
    assert driver.current_url == "https://www.automationexercise.com/products" # 5. user is navigated to products page

    ProductList = driver.find_element(By.CSS_SELECTOR, "div[class='features_items'") # 6. verify products list is visible

    driver.execute_script("window.scrollTo(0, 900)") # scroll down to find other elements
    ViewFirstProduct = driver.find_element(By.LINK_TEXT, "View Product")
    ViewFirstProduct.click() # 7. click on "view product" on first product

    RemoveGoogleAdvert()

    assert driver.current_url == "https://www.automationexercise.com/product_details/1" # 8. user landed on product detail page

    ProductInformation = driver.find_element(By.CSS_SELECTOR, "div[class='product-information'")
    SpanElements = ProductInformation.find_elements(By.CSS_SELECTOR, "span")
    PElements = ProductInformation.find_elements(By.CSS_SELECTOR, "p")

    ProductName = ProductInformation.find_element(By.CSS_SELECTOR, "h2")

    for ProductPrice in SpanElements:
        if "Rs." in ProductPrice.text:
            break

    for element in PElements:
        if "Category" in element.text:
            ProductCategory = element
        if "Stock" in element.text:
            ProductStock = element
        if "Condition" in element.text:
            ProductCondition = element
        if "Brand" in element.text:
            ProductBrand = element

    # 9. verify that the product details are visible

    print(ProductName.text)
    print(ProductCategory.text)
    print(ProductStock.text)
    print(ProductCondition.text)
    print(ProductBrand.text)

def RemoveGoogleAdvert():
    try:
        driver.switch_to.frame("aswift_4")  # might be buried under a parent
        driver.switch_to.frame("ad_iframe")
        RemoveGoogleAd = driver.find_element(By.CSS_SELECTOR, "div[id='dismiss-button']")  # remove the google ad that pops up
        RemoveGoogleAd.click()
    except (NoSuchElementException, NoSuchFrameException):
        pass

VerifyAllProducts()

driver.close()
driver.quit()