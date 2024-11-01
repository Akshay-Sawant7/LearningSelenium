from selenium import webdriver
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Open the W3Schools homepage
    driver.get('https://www.w3schools.com')

    # Wait for the page to load
    time.sleep(2)

    # Take a screenshot and save it
    driver.save_screenshot('screenshot_w3schools.png')

    # Print confirmation
    print("Screenshot saved as 'screenshot_w3schools.png'")

finally:
    # Close the browser
    driver.quit()
