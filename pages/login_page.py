
from playwright.sync_api import expect
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator(
            "[data-test='error']"
        )

    def open_login_page(self, url):
        self.navigate(url)

    def enter_username(self, username):
        self.fill(self.username, username)

    def enter_password(self, password):
        self.fill(self.password, password)

    def click_login(self):
        self.click(self.login_button)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def verify_login_error(self, expected_message):
        expect(self.error_message).to_contain_text(
            expected_message
        )
