from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
# Open the main page
driver.get('https://www.w3schools.com')

# Wait for the page to load
time.sleep(2)

# Open a new tab using JavaScript
driver.execute_script("window.open('https://www.w3schools.com/html/', '_blank');")

# Wait for the new tab to load
time.sleep(2)

# Get the original window's handle
original_window = driver.current_window_handle

# Switch to the new window (the last one opened)
for handle in driver.window_handles:
    if handle != original_window:
        driver.switch_to.window(handle)
        break

# Now we are in the new window, interact with it
print("Title of the new window:", driver.title)  # Print the title of the new page

# Wait for a moment to observe
time.sleep(2)

# Close the new window
driver.close()  # Close the new tab/window

# Switch back to the original window
driver.switch_to.window(original_window)

# Confirm we are back in the original window
print("Switched back to the original window. Title is:", driver.title)

# Wait before closing the browser
time.sleep(2)

# Close the browser
driver.quit()
