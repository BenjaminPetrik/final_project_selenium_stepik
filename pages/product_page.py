from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "There is no 'Add to basket' button"

    def should_be_product_is_added_to_basket(self):
        item_name = self.browser.find_element(*ProductPageLocators.NAME).text
        item_message = self.browser.find_element(*ProductPageLocators.NAME_MESSAGE).text
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        price_message = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE).text
        assert item_name == item_message, f"Wrong item is added to the basket; {print(self.browser.current_url)}"
        assert price == price_message, f"Wrong basket price; {print(self.browser.current_url)}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.NAME_MESSAGE), "Success message is presented, but should " \
                                                                       "dissapear "
