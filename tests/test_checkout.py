
import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from utils.test_data import generate_user_details


@pytest.mark.smoke
@pytest.mark.checkout
def test_successful_checkout(logged_in_page):

    inventory = InventoryPage(logged_in_page)

    # Step 1: Add product
    inventory.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    # Step 2: Open cart
    inventory.open_cart()

    cart = CartPage(logged_in_page)

    cart.verify_cart_page()

    # Step 3: Checkout
    cart.click_checkout()

    checkout = CheckoutPage(logged_in_page)

    # Step 4: Enter customer information
    user = generate_user_details()

    checkout.enter_checkout_information(
        user["first_name"],
        user["last_name"],
        user["postal_code"]
    )

    checkout.click_continue()

    # Step 5: Verify order overview
    checkout.verify_checkout_overview()

    # Step 6: Finish order
    checkout.click_finish()

    # Step 7: Verify order confirmation
    checkout.verify_order_confirmation()


@pytest.mark.negative
@pytest.mark.checkout
def test_checkout_without_first_name(logged_in_page):

    inventory = InventoryPage(logged_in_page)

    inventory.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    inventory.open_cart()

    cart = CartPage(logged_in_page)

    cart.click_checkout()

    checkout = CheckoutPage(logged_in_page)

    checkout.enter_checkout_information(
        "",
        "Tester",
        "560001"
    )

    checkout.click_continue()

    checkout.verify_checkout_error(
        "First Name is required"
    )
