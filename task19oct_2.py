from selenium import webdriver
import allure
import pytest
import time

from selenium.webdriver.common.by import By


@allure.title("Verify Invalid credentials of  https://app.vwo.com/")
def test_task_case():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/")

    user_login = driver.find_element(By.ID, "login-username")
    user_login.send_keys("abcd@gmail.com")

    user_pwd = driver.find_element(By.ID, "login-password")
    user_pwd.send_keys("abcd1234")
    time.sleep(10)

    assert driver.current_url == "https://app.vwo.com/#/login"
    content = driver.page_source
    assert "Your email, password, IP address or location did not match" in content
