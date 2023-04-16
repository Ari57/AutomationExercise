from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, NoSuchFrameException

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # 1. launch browser
driver.maximize_window()
driver.get("https://www.automationexercise.com/") # 2. navigate to url
assert driver.current_url == "https://www.automationexercise.com/" # 3. verify home page

def ContactUs():
    ContactUsButton = driver.find_element(By.LINK_TEXT, "Contact us")  # find the "Contact us" element
    ContactUsButton.click()  # 4. click on Contact us link

    RemoveGoogleAdvert()

    driver.implicitly_wait(0.5)

    H2Elements = driver.find_elements(By.CSS_SELECTOR, "h2[class='title text-center']")

    for GetInTouch in H2Elements:
        if GetInTouch.text == "GET IN TOUCH":
            break

    assert GetInTouch.text == "GET IN TOUCH" # 5. verify that "Get In Touch" is visible

    ContactName = driver.find_element(By.CSS_SELECTOR, "input[name='name']")
    ContactName.send_keys("Nathan")  # 6. Enter name

    ContactEmail = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
    ContactEmail.send_keys("njds7777@gmail.com")  # 6. Enter email

    ContactSubject = driver.find_element(By.CSS_SELECTOR, "input[name='subject']")
    ContactSubject.send_keys("Automation test case 6") # 6. Enter subject

    ContactMessage = driver.find_element(By.CSS_SELECTOR, "textarea[id='message']")
    ContactMessage.send_keys("Hello World") # 6. Enter message

    driver.execute_script("window.scrollTo(0, 540)") # scroll down to find other elements

    ContactFile = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    ContactFile.send_keys(__file__)  # 7. Upload File

    ContactSubmit = driver.find_element(By.CSS_SELECTOR, "input[name='submit']")
    ContactSubmit.click()  # 8. Click Submit button

    AlertBox = driver.switch_to.alert # switch to alert popup
    AlertBox.accept() # 9. Click on "Ok"

    SuccessBox = driver.find_element(By.CSS_SELECTOR, "div[class='status alert alert-success']")
    assert SuccessBox.text == "Success! Your details have been submitted successfully." # 10. verify that the message exists

    HomeButton = driver.find_element(By.CSS_SELECTOR, "a[class='btn btn-success']")
    HomeButton.click()  # 11. Click Home button

    RemoveGoogleAdvert()

    assert driver.current_url == "https://www.automationexercise.com/"  # 11. Verify that we have arrived at the home page

def RemoveGoogleAdvert():
    try:
        driver.switch_to.frame("aswift_4")  # might be buried under a parent
        driver.switch_to.frame("ad_iframe")
        RemoveGoogleAd = driver.find_element(By.CSS_SELECTOR, "div[id='dismiss-button']")  # remove the google ad that pops up
        RemoveGoogleAd.click()
    except (NoSuchElementException, NoSuchFrameException):
        pass

ContactUs()

driver.close()
driver.quit()