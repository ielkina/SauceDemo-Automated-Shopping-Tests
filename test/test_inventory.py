# tests/test_inventory.py

import pytest

@pytest.fixture(scope="module")
def your_fixture():
    pass
    # ваш код

from pages.inventory_page import InventoryPage

# Фікстура driver автоматично надається з conftest.py

# Створюємо фікстуру, яка ініціалізує Page Object для тестів
@pytest.fixture(scope="module")
def inventory_page(driver):
    return InventoryPage(driver)

## Сценарій 1: Тестування сортування за ціною
def test_price_sorting_low_to_high(inventory_page: InventoryPage):
    """
    Перевіряє, чи коректно сортуються товари після вибору опції "Price (low to high)".
    """
    # 1. Виконання дії: Сортування
    inventory_page.sort_by_price_ascending()
    
    # 2. Отримання фактичних даних
    actual_prices = inventory_page.get_all_prices_as_float()
    
    # 3. Визначення очікуваних даних (сортування фактичного списку)
    expected_prices = sorted(actual_prices)
    
    # 4. Асерція
    assert actual_prices == expected_prices, (
        f"Сортування не працює коректно. Очікувано: {expected_prices}, "
        f"Фактично: {actual_prices}"
    )


## Сценарій 2: Тестування додавання товару у кошик
def test_add_item_to_cart(inventory_page: InventoryPage):
    """
    Перевіряє, чи коректно збільшується лічильник товарів у кошику після додавання першого товару.
    """
    # 1. Початковий стан: отримуємо поточну кількість (має бути 0 або скинуто після логіну)
    initial_count = inventory_page.get_cart_count()

    # 2. Виконання дії: додаємо товар
    inventory_page.add_first_item_to_cart()

    # 3. Перевірка: отримуємо нову кількість
    new_count = inventory_page.get_cart_count()

    # 4. Асерція: лічильник має збільшитися рівно на 1
    assert new_count == initial_count + 1, (
        f"Лічильник кошика не оновився. Очікувалося {initial_count + 1}, "
        f"фактично {new_count}"
    )