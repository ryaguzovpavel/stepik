from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner ")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alertinner p strong")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini span.btn-group a.btn")


class BasketPageLocators:
    BASKET_CONTENT = (By.CSS_SELECTOR, "#content_inner p")


class LoginPageLocators:
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BTN = (By.NAME, "registration_submit")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
