
from playwright.sync_api import expect
from pages.base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.page_title = page.locator(
            ".title"
        )

        self.inventory_items = page.locator(
            ".inventory_item"
        )

        self.product_names = page.locator(
            ".inventory_item_name"
        )

        self.sort_dropdown = page.locator(
            "[data-test='product-sort-container']"
        )

        self.cart_icon = page.locator(
            ".shopping_cart_link"
        )

    def verify_inventory_page(self):
        expect(self.page_title).to_have_text("Products")

    def get_product_count(self):
        return self.inventory_items.count()

    def get_product_names(self):
        return self.product_names.all_text_contents()

    def sort_products(self, option):
        self.sort_dropdown.select_option(option)

    def add_product_to_cart(self, product_name):

        product = self.page.locator(
            ".inventory_item"
        ).filter(
            has_text=product_name
        )

        product.locator(
            "button"
        ).click()

        expect(
            product.locator("button")
        ).to_have_text("Remove")

    def open_cart(self):
        self.cart_icon.click()

    def verify_cart_badge(self, count):
        expect(
            self.page.locator(".shopping_cart_badge")
        ).to_have_text(str(count))

    
    def logout(self):

        menu_button = self.page.locator(
            "#react-burger-menu-btn"
        )

        menu_button.click()

        logout_link = self.page.locator(
            "#logout_sidebar_link"
        )

        logout_link.click()

    def verify_logout(self):

        from playwright.sync_api import expect

        expect(
            self.page.locator("#login-button")
        ).to_be_visible()

