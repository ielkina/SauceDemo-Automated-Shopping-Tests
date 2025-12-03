# pages/inventory_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class InventoryPage(BasePage):
    # Локатори
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    FIRST_ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    
    # def sort_by_price_ascending(self):
    #     """Сортує товари за ціною від низької до високої (price_asc)."""
    #     select = Select(self.find_element(self.SORT_DROPDOWN))
    #     select.select_by_value("price_asc")
    def sort_by_price_ascending(self):
        select = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        select.select_by_value("lohi")  # Исправлено с "price_asc" на "lohi"

    def get_all_prices_as_float(self):
        """Отримує список усіх цін зі сторінки як числа з плаваючою точкою."""
        price_elements = self.driver.find_elements(*self.PRODUCT_PRICES)
        # Прибираємо символ '$' та конвертуємо
        prices = [float(p.text.replace('$', '')) for p in price_elements]
        return prices
    
    def add_first_item_to_cart(self):
        """Клікає на кнопку 'Add to cart' для першого товару."""
        self.find_element(self.FIRST_ADD_TO_CART_BUTTON).click()

    def get_cart_count(self):
        """Повертає кількість товарів у кошику з бейджа."""
        try:
            # Перевіряємо, чи існує бейдж
            return int(self.find_element(self.CART_BADGE, timeout=2).text)
        except:
            return 0