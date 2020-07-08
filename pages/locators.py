from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_formd")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_formd")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    NAME = (By.TAG_NAME, "h1")
    NAME_MESSAGE = (By.CSS_SELECTOR, "#messages div:first-child strong")
    PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
