import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.title("Verify the number of Mac mini in the search")
@allure.description("Verify all the prices and products are fetched")
def test_ebay():

    driver = webdriver.Chrome()

    try:

        driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")
        search_box = driver.find_element(By.XPATH, "//input[@aria-label='Search for anything']")
        search_box.send_keys("Macmini")
        search_button = driver.find_element(By.XPATH, "//input[@value='Search']")
        search_button.click()

        time.sleep(4)

        titles = driver.find_elements(By.XPATH, "//h3[@class='s-item__title']")

        prices = driver.find_elements(By.XPATH, "//span[@class='s-item__price']")

        if len(titles) != len(prices):
            print("Mismatch in the number of titles and prices.")
        else:

            product_data = []
            price_values = []

            for title, price in zip(titles, prices):
                title_text = title.text
                price_text = price.text.replace(",", "").replace("$", "").split()[0]

                try:
                    price_value = float(price_text)
                    product_data.append((title_text, price_value))
                    price_values.append(price_value)
                except ValueError:
                    print(f"Skipping invalid price: {price_text}")

            print("\nProduct Titles and Prices:")
            for title, price in product_data:
                print(f"{title} - ${price}")

            if price_values:
                max_price = max(price_values)
                min_price = min(price_values)
                print(f"\nMaximum Price: ${max_price}")
                print(f"Minimum Price: ${min_price}")
            else:
                print("\nNo valid prices found.")
    finally:
        driver.quit()
