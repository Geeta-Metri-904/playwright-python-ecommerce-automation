
import pytest

from config.settings import USERNAME, PASSWORD
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
@pytest.mark.login
def test_valid_login(login_page):

    login_page.login(USERNAME, PASSWORD)

    inventory = InventoryPage(login_page.page)

    inventory.verify_inventory_page()

    assert "/inventory.html" in login_page.page.url


@pytest.mark.negative
@pytest.mark.login
def test_locked_user_login(login_page):

    login_page.login(
        "locked_out_user",
        "secret_sauce"
    )

    login_page.verify_login_error(
        "Sorry, this user has been locked out."
    )


@pytest.mark.negative
@pytest.mark.login
def test_invalid_login(login_page):

    login_page.login(
        "invalid_user",
        "wrong_password"
    )

    login_page.verify_login_error(
        "Username and password do not match"
    )


@pytest.mark.negative
@pytest.mark.login
def test_empty_login(login_page):

    login_page.click_login()

    login_page.verify_login_error(
        "Username is required"
    )
