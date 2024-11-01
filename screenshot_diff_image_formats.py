from selenium import webdriver
from PIL import Image
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Open the W3Schools homepage
    driver.get('https://www.w3schools.com')

    # Wait for the page to load
    time.sleep(2)

    # Take a screenshot and save it as PNG
    screenshot_path = 'screenshot_w3schools.png'
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved as '{screenshot_path}'")

    # Open the PNG image with Pillow
    image = Image.open(screenshot_path)

    # Convert and save as JPEG
    jpeg_path = 'screenshot_w3schools.jpg'
    image.convert('RGB').save(jpeg_path, 'JPEG')
    print(f"Screenshot converted and saved as '{jpeg_path}'")

    # Convert and save as BMP
    bmp_path = 'screenshot_w3schools.bmp'
    image.save(bmp_path, 'BMP')
    print(f"Screenshot converted and saved as '{bmp_path}'")

finally:
    # Close the browser
    driver.quit()
