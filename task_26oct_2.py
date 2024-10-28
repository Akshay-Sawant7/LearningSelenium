from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


def test_drag_n_drop():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    time.sleep(2)

    source_element = driver.find_element(By.ID, 'draggable')  # Change to the actual ID
    target_element = driver.find_element(By.ID, 'droppable')  # Change to the actual ID

    actions = ActionChains(driver)
    actions.drag_and_drop(source_element, target_element).perform()

    time.sleep(2)

    driver.quit()
