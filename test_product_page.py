import pytest
from .pages.product_page import ProductPage


#@pytest.mark.parametrize('offer', ["0", "1", "2", "3", "4", "5", "6", "8", "9",
                                   #pytest.param("7", marks=pytest.mark.xfail)])
def test_guest_can_add_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_is_added_to_basket()
    #page.should_not_be_success_message()
    page.should_dissapear_success_message()
