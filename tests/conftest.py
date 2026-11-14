
import os
import pytest

from config.settings import BASE_URL, USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import get_logger

logger = get_logger(__name__)


@pytest.fixture(scope="function")
def app_url():
    """Return application base URL."""
    return BASE_URL


@pytest.fixture(scope="function")
def login_page(page, app_url):
    """
    Initialize login page and navigate
    to SauceDemo login screen.
    """
    login = LoginPage(page)

    login.open_login_page(app_url)

    logger.info("Opened SauceDemo login page")

    return login


@pytest.fixture(scope="function")
def logged_in_page(page):
    """
    Login using valid credentials and
    return authenticated Playwright page.
    """
    login = LoginPage(page)

    login.open_login_page(BASE_URL)

    login.login(USERNAME, PASSWORD)

    inventory = InventoryPage(page)

    inventory.verify_inventory_page()

    logger.info("Successfully logged into SauceDemo")

    return page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Capture screenshot when a test fails.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:

            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = os.path.join(
                "screenshots",
                f"{item.name}.png"
            )

            page.screenshot(
                path=screenshot_path,
                full_page=True
            )

            logger.error(
                f"Test failed: {item.name}"
            )
