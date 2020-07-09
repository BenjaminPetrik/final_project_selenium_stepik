from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_message(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_EMPTY_MESSAGE), "There is no message that basket is empty"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "There are items on the basket"