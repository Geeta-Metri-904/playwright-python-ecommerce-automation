
from playwright.sync_api import expect
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.first_name = page.locator(
            "[data-test='firstName']"
        )

        self.last_name = page.locator(
            "[data-test='lastName']"
        )

        self.postal_code = page.locator(
            "[data-test='postalCode']"
        )

        self.continue_button = page.locator(
            "[data-test='continue']"
        )

        self.finish_button = page.locator(
            "[data-test='finish']"
        )

        self.order_confirmation = page.locator(
            ".complete-header"
        )

        self.error_message = page.locator(
            "[data-test='error']"
        )

        self.back_home_button = page.locator(
            "[data-test='back-to-products']"
        )

    def enter_checkout_information(
        self, first_name, last_name, postal_code
    ):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def click_continue(self):
        self.continue_button.click()

    def click_finish(self):
        self.finish_button.click()

    def verify_checkout_overview(self):
        expect(
            self.page.locator(".title")
        ).to_have_text("Checkout: Overview")

    def verify_order_confirmation(self):
        expect(
            self.order_confirmation
        ).to_have_text("Thank you for your order!")

    def verify_checkout_error(self, message):
        expect(
            self.error_message
        ).to_contain_text(message)

    def back_to_products(self):
        self.back_home_button.click()
