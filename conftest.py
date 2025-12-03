# conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def driver():
    # Налаштування Chrome
    chrome_options = Options()
    # chrome_options.add_argument("--headless") # Запуск у безголовому режимі (опціонально)
    
    # Ініціалізація WebDriver (переконайтеся, що chromedriver доступний у PATH)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    # Виконання логіну для доступу до сторінки інвентаризації
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    yield driver
    
    # Завершення: закриття браузера
    driver.quit()