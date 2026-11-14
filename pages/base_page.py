
from playwright.sync_api import Page, expect
from config.settings import DEFAULT_TIMEOUT


class BasePage:

    def __init__(self, page: Page):
        self.page = page
        self.page.set_default_timeout(DEFAULT_TIMEOUT)

    def navigate(self, url):
        self.page.goto(url)

    def click(self, locator):
        locator.click()

    def fill(self, locator, value):
        locator.fill(value)

    def get_text(self, locator):
        return locator.inner_text()

    def is_visible(self, locator):
        return locator.is_visible()

    def get_count(self, locator):
        return locator.count()

    def wait_for_url(self, url):
        self.page.wait_for_url(url)

    def assert_visible(self, locator):
        expect(locator).to_be_visible()

    def assert_text(self, locator, expected):
        expect(locator).to_have_text(expected)

    def take_screenshot(self, name):
        self.page.screenshot(
            path=f"screenshots/{name}.png",
            full_page=True
        )
