from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the W3Schools Tryit Editor page with an alert
driver.get('https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert')

# Wait for the page to load
time.sleep(2)

# Switch to the iframe where the button is located
driver.switch_to.frame("iframeResult")

# Locate and click the button that triggers the alert
try:
    button = driver.find_element(By.XPATH, '//button[text()="Try it"]')
    button.click()  # Click the button to trigger the alert
except NoSuchElementException:
    print("Button not found.")

# Wait for the alert to appear
time.sleep(2)

# Handle the alert
try:
    alert = driver.switch_to.alert
    print("Alert text:", alert.text)  # Print the alert text
    alert.accept()  # Accept (close) the alert
except NoAlertPresentException:
    print("No alert found.")

# Switch back to the main content
driver.switch_to.default_content()

# Wait to observe the action
time.sleep(2)

# Close the browser
driver.quit()
