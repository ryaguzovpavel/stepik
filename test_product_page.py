import time

import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
BASE = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
OFFER7 = f"{BASE}7"

LINKS = [
    pytest.param(f"{BASE}{n}", marks=pytest.mark.xfail(reason="bug")) if f"{BASE}{n}" == OFFER7 else f"{BASE}{n}"
    for n in range(10)
]


@pytest.mark.parametrize("promo_link", LINKS)
def test_guest_can_add_product_to_basket_promo(browser, promo_link):
    page = ProductPage(browser, promo_link)
    page.open()
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding_to_basket(product_name)
    page.should_be_message_basket_total_price(product_price)


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(
            browser, "http://selenium1py.pythonanywhere.com/accounts/login/"
        )
        login_page.open()
        email = f"{time.time()}@fakemail.org"
        password = "Stepik132456"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_message_about_adding()
        page.should_be_message_basket_total()

    @pytest.mark.skip
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_not_be_success_message()


class TestGuestAddToBasketFromProductPage:
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_message_about_adding()
        page.should_be_message_basket_total()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_is_empty()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.skip
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_disappeared_success_message()
