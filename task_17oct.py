from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_cura_login():

    driver = webdriver.Chrome()

    driver.get("https://katalon-demo-cura.herokuapp.com/")

    make_appointment_button = driver.find_element(By.ID, "btn-make-appointment")
    make_appointment_button.click()


    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login", "URL after 'Make Appointment' click is incorrect"

    time.sleep(2)

    username_field = driver.find_element(By.ID, "txt-username")
    username_field.send_keys("John Doe")  # Sample username from the demo

    password_field = driver.find_element(By.ID, "txt-password")
    password_field.send_keys("ThisIsNotAPassword")  # Sample password from the demo

    login_button = driver.find_element(By.ID, "btn-login")
    login_button.click()

    time.sleep(2)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment", "URL after login is incorrect"

    print("Login successful and navigated to appointment page")


    driver.quit()


