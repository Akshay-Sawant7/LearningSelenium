from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open Wikipedia homepage
driver.get('https://www.wikipedia.org/')

# Locate the dropdown element for language selection
dropdown_element = driver.find_element(By.ID, 'searchLanguage')

# Initialize the Select class
dropdown = Select(dropdown_element)

# Select by visible text
dropdown.select_by_visible_text('Eesti')  # Select 'Eesti' (Estonian)

# Wait to see the selection
time.sleep(2)

# Select another option by index
dropdown.select_by_index(5)  # Selects the sixth language in the dropdown

# Wait to see the selection
time.sleep(2)

# Select by value
dropdown.select_by_value('fr')  # Selects the option with value 'fr' (French)

# Wait before closing the browser
time.sleep(2)

# Close the browser
driver.quit()
