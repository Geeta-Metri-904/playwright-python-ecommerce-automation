
import pytest

from pages.inventory_page import InventoryPage


@pytest.mark.smoke
@pytest.mark.inventory
def test_inventory_products(logged_in_page):

    inventory = InventoryPage(logged_in_page)

    inventory.verify_inventory_page()

    assert inventory.get_product_count() == 6


@pytest.mark.regression
@pytest.mark.inventory
def test_product_names_available(logged_in_page):

    inventory = InventoryPage(logged_in_page)

    product_names = inventory.get_product_names()

    assert len(product_names) == 6

    assert "Sauce Labs Backpack" in product_names


@pytest.mark.regression
@pytest.mark.inventory
def test_sort_products_low_to_high(logged_in_page):

    inventory = InventoryPage(logged_in_page)

    inventory.sort_products("lohi")

    prices = logged_in_page.locator(
        ".inventory_item_price"
    ).all_text_contents()

    numeric_prices = [
        float(price.replace("$", ""))
        for price in prices
    ]

    assert numeric_prices == sorted(numeric_prices)


@pytest.mark.regression
@pytest.mark.inventory
def test_add_product_to_cart(logged_in_page):

    inventory = InventoryPage(logged_in_page)

    inventory.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    inventory.verify_cart_badge(1)
