import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@allure.title("Select Delhi in SpiceJet")
@allure.description("Select 'Delhi' from the 'From' dropdown")
def test_select_delhi_spicejet():

    driver = webdriver.Chrome()
    driver.get("https://www.spicejet.com/")
    driver.maximize_window()
    fromcity = driver.find_element(By.XPATH, "//div[text()='From']")
    time.sleep(5)
    actions = ActionChains(driver)
    (actions.
     move_to_element(fromcity)
     .click().send_keys("del")    # for mumbai type mum
     .perform())
    time.sleep(5)

    driver.quit()
