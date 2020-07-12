from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#register_form [type='email']")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#register_form [name*='password1']")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#register_form [name*='password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name*='registration_submit']")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    NAME = (By.TAG_NAME, "h1")
    NAME_MESSAGE = (By.CSS_SELECTOR, "#messages div:first-child strong")
    PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini .btn:first-child")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
