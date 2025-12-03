# pages/base_page.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        
    def find_element(self, by_locator, timeout=10):
        """Знаходить елемент, очікуючи його появи."""
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))