
import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.mark.smoke
@pytest.mark.cart
def test_add_product_and_verify_cart(logged_in_page):

    inventory = InventoryPage(logged_in_page)

    inventory.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    inventory.open_cart()

    cart = CartPage(logged_in_page)

    cart.verify_cart_page()

    cart.verify_product_in_cart(
        "Sauce Labs Backpack"
    )

    assert cart.get_cart_item_count() == 1


@pytest.mark.regression
@pytest.mark.cart
def test_remove_product_from_cart(logged_in_page):

    inventory = InventoryPage(logged_in_page)

    # Add product
    inventory.add_product_to_cart("Sauce Labs Backpack")

    # Verify cart badge before opening cart
    inventory.verify_cart_badge(1)

    print("Product added successfully")

    # Open cart
    inventory.open_cart()

    cart = CartPage(logged_in_page)

    # Verify cart page
    cart.verify_cart_page()

    # Verify product exists
    assert cart.get_cart_item_count() == 1

    cart.verify_product_in_cart("Sauce Labs Backpack")

    # Remove product
    cart.remove_product("Sauce Labs Backpack")

    # Verify cart is empty
    assert cart.get_cart_item_count() == 0

    print("Product removed successfully")

@pytest.mark.regression
@pytest.mark.cart
def test_cart_with_multiple_products(logged_in_page):

    inventory = InventoryPage(logged_in_page)

    inventory.add_product_to_cart("Sauce Labs Backpack")
    inventory.verify_cart_badge(1)

    inventory.add_product_to_cart("Sauce Labs Bike Light")
    inventory.verify_cart_badge(2)

    inventory.open_cart()

    cart = CartPage(logged_in_page)

    cart.verify_cart_page()

    assert cart.get_cart_item_count() == 2

