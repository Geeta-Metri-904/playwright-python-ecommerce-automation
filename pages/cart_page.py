
from playwright.sync_api import expect
from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.cart_title = page.locator(".title")

        self.cart_items = page.locator(
            ".cart_item"
        )

        self.checkout_button = page.locator(
            "[data-test='checkout']"
        )

        self.continue_shopping = page.locator(
            "[data-test='continue-shopping']"
        )

    def verify_cart_page(self):
        expect(self.cart_title).to_have_text("Your Cart")

    def get_cart_item_count(self):
        return self.cart_items.count()

    def verify_product_in_cart(self, product_name):
        expect(
            self.page.locator(".cart_item")
        ).to_contain_text(product_name)

    def remove_product(self, product_name):
        item = self.page.locator(
            ".cart_item"
        ).filter(
            has_text=product_name
        )

        item.locator("button").click()

    def click_checkout(self):
        self.checkout_button.click()

    def continue_shopping_click(self):
        self.continue_shopping.click()
