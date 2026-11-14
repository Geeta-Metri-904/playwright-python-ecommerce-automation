
import pytest

from pages.inventory_page import InventoryPage


@pytest.mark.regression
def test_user_logout(logged_in_page):

    inventory = InventoryPage(logged_in_page)

    inventory.logout()

    inventory.verify_logout()
