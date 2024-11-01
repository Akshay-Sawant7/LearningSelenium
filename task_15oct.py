from selenium import webdriver


def test_cura_healthcare_page():
    driver = webdriver.Chrome()

    driver.get("https://katalon-demo-cura.herokuapp.com/")

    print("Page Title:", driver.title)
    assert driver.title == "CURA Healthcare Service"

    current_url = driver.current_url
    print("Current URL:", current_url)
    assert current_url == "https://katalon-demo-cura.herokuapp.com/"

    page_source = driver.page_source
    assert "CURA Healthcare Service" in page_source



