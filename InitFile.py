from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def Driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # 1. launch browser
    driver.maximize_window()
    driver.get("https://www.automationexercise.com/")  # 2. navigate to url
    assert driver.current_url == "https://www.automationexercise.com/"  # 3. verify home page

    return driver