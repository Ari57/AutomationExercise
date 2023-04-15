from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # 1. launch browser
driver.maximize_window()
driver.get("https://www.automationexercise.com/") # 2. navigate to url
assert driver.current_url == "https://www.automationexercise.com/" # 3. verify home page

def TestCases():
    TestCaseButton = driver.find_element(By.LINK_TEXT, "Test Cases")  # find the "Test Cases" element
    TestCaseButton.click()  # 4. click on Test Cases link

    if "google_vignette" in driver.current_url:  # temp fix for dealing with Google adverts
        driver.get("https://www.automationexercise.com/test_cases")

    assert driver.current_url == "https://www.automationexercise.com/test_cases" # 5. verify that user is brought to test cases page

TestCases()

driver.close()
driver.quit()