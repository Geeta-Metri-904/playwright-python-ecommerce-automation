
import os
import pytest

from config.settings import BASE_URL, USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import get_logger

logger = get_logger(__name__)


@pytest.fixture(scope="function")
def app_url():
    return BASE_URL


@pytest.fixture(scope="function")
def login_page(page):
    login = LoginPage(page)
    login.open_login_page(BASE_URL)

    logger.info("Opened SauceDemo login page")

    return login


@pytest.fixture(scope="function")
def logged_in_page(page, app_url):
    login = LoginPage(page)

    login.open_login_page(app_url)
    login.login(USERNAME, PASSWORD)

    inventory = InventoryPage(page)
    inventory.verify_inventory_page()

    logger.info("Successfully logged in")

    return page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:

            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = (
                f"screenshots/{item.name}.png"
            )

            page.screenshot(
                path=screenshot_path,
                full_page=True
            )

            logger.error(
                f"Test failed: {item.name}"
            )
