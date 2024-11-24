from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

'''
use below command in terminal to install requirements
pip install pytest allure-pytest selenium  

For running tests click arrow button which appering on left side of function names
or
run below command in terminal all tests will run one after one
pytest -s automation_analyst_assignment.py

'''

# 1- Navigate to the FitPeo Homepage
def test_open_fitpeo_homepage():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get("https://www.fitpeo.com/")
        time.sleep(5)
        print(f"Page Title: {driver.title}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()


# 2 - Navigate to the Revenue Calculator Page
def test_navigate_to_revenue_calculator():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get("https://www.fitpeo.com/")
        print("Opened FitPeo Homepage")
        time.sleep(5)

        # Locate and click the Revenue Calculator link
        calculator_link = driver.find_element(By.LINK_TEXT, "Revenue Calculator")
        calculator_link.click()
        print("Navigated to Revenue Calculator Page")

        time.sleep(5)

        print(f"Page Title: {driver.title}")
        print(f"Current URL: {driver.current_url}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        driver.quit()


# 3 - Scroll Down to the Slider section
def test_scroll_to_slider():
    # Set up WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get("https://www.fitpeo.com/")
        print("Opened FitPeo Homepage")

        time.sleep(3)

        # Locate and click the Revenue Calculator link
        calculator_link = driver.find_element(By.LINK_TEXT, "Revenue Calculator")  # Example selector
        calculator_link.click()
        time.sleep(8)

        # Locate the Revenue Calculator Slider section
        # Update the selector to match the actual slider's unique identifier
        target_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Medicare Eligible Patients')]"))
        )

        # Scroll to the element
        driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", target_element)
        print("Scrolled to 'Medicare Eligible Patients'")

        # Pause to observe
        time.sleep(3)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        driver.quit()


# 4 - Adjust the Slider
def test_set_slider_value():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        # Open the FitPeo Revenue Calculator page
        driver.get("https://www.fitpeo.com/")
        print("Opened FitPeo Homepage")

        # Navigate to the Revenue Calculator Page
        calculator_link = driver.find_element(By.LINK_TEXT, "Revenue Calculator")
        calculator_link.click()
        print("Navigated to Revenue Calculator Page")

        # Wait for the page to load
        time.sleep(3)


        # Locate the slider input and the text field
        slider = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@data-index='0']/input[@type='range']"))
        )
        text_field = driver.find_element(By.XPATH, "//input[@type='number']")

        min_value = int(slider.get_attribute("aria-valuemin"))
        max_value = int(slider.get_attribute("aria-valuemax"))

        target_value = 820
        if target_value < min_value or target_value > max_value:
            raise ValueError("Target value is out of range.")


        offset = 94

        # Move the slider
        actions = ActionChains(driver)
        actions.click_and_hold(slider).move_by_offset(offset, 0).release().perform()

        time.sleep(4)

        print(f"Slider successfully set to {target_value}, and text field updated.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

 # 5 - Update the Text Field  & 6 - Validate Slider Value
def test_update_slider_via_text_field():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        # Open the FitPeo Revenue Calculator page
        driver.get("https://www.fitpeo.com/")
        print("Opened FitPeo Homepage")

        # Navigate to the Revenue Calculator Page
        calculator_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Revenue Calculator"))  # Replace with actual link text
        )
        calculator_link.click()
        print("Navigated to Revenue Calculator Page")

        # Wait for the page to load
        time.sleep(3)

        # Locate the text field
        text_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='number']"))
        )

        # Clear the text field using backspace
        text_field.click()  # Click to focus on the text field
        current_value = text_field.get_attribute("value")
        for _ in range(len(current_value)):  # Backspace the current value
            text_field.send_keys(Keys.BACKSPACE)
        print(f"Cleared text field")

        # Enter the desired value into the text field (560)
        target_value = 560
        text_field.send_keys(str(target_value))
        print(f"Entered value {target_value} into the text field.")

        # Trigger input, change, and blur events to sync the slider
        driver.execute_script("arguments[0].dispatchEvent(new Event('input'));", text_field)
        driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", text_field)
        driver.execute_script("arguments[0].dispatchEvent(new Event('blur'));", text_field)

        # Allow time for JavaScript to sync the slider
        time.sleep(2)

        # Locate the slider input to verify the updated value
        slider_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='range']"))
        )
        updated_slider_value = slider_input.get_attribute("value")
        print(f"Slider updated to value: {updated_slider_value}")

        # Assert if the slider reflects the entered value
        assert updated_slider_value == str(target_value), f"Expected {target_value}, got {updated_slider_value}"
        print("Slider and text field synchronization successful.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()


# 7 - Select CPT Codes, 8 - Validate Total Recurring Reimbursement, 9 - Verify that the header displaying
def test_select_checkboxes_and_validate_reimbursement():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        # Open the FitPeo Revenue Calculator page
        driver.get("https://www.fitpeo.com/")
        print("Opened FitPeo Homepage")

        # Navigate to the Revenue Calculator Page
        calculator_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Revenue Calculator"))  # Replace with actual link text
        )
        calculator_link.click()
        print("Navigated to Revenue Calculator Page")
        target_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'CPT-99091')]"))
        )

        # Scroll to the element
        driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", target_element)
        print("Scrolled to 'Medicare Eligible Patients'")
        # Wait for the page to load
        time.sleep(3)
        checkboxes = [
            "99091",
            "99453",
            "99454",
            "99474"
        ]
        for checkbox_id in checkboxes:
            checkbox = driver.find_element(By.XPATH,f"//div[@class='MuiBox-root css-1eynrej']//p[contains(text(),'CPT-{checkbox_id}')]/following-sibling::label//input[@type='checkbox']")

            if not checkbox.is_selected():
                checkbox.click()

        time.sleep(5)

        # Validate Total Recurring Reimbursement value
        total_reimbursement_header = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Total Recurring Reimbursement for all Patients Per Month')]"))
        )

        total_reimbursement_value = total_reimbursement_header.text
        print(f"Total Recurring Reimbursement value: {total_reimbursement_value}")

        # Assert that the value is $110700
        assert "$110700" in total_reimbursement_value, f"Expected '$110700', but got: {total_reimbursement_value}"

        print("Total Recurring Reimbursement validated successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()


