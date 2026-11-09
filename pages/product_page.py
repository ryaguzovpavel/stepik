from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        basket_link.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), (
            "Product name is not presented"
        )
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), (
            "Message about adding is not presented"
        )
        product_name = (
            self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
            + " has been added to your basket."
        )
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        assert product_name == message, "No product name in the message"

    def should_be_message_about_adding_to_basket(self, product_name):
        assert self.is_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message about adding is not presented"
        actual_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert actual_message == product_name, (
            f"Product name in message ({actual_message!r}) differs from product name ({product_name!r})"
        )

    def should_be_message_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), (
            "Message basket total is not presented"
        )
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), (
            "Product price is not presented"
        )
        message_basket_total = self.browser.find_element(
            *ProductPageLocators.MESSAGE_BASKET_TOTAL
        ).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price in message_basket_total, "No product price in the message"

    def should_be_message_basket_total_price(self, product_price):
        assert self.is_element_present(
            *ProductPageLocators.BASKET_TOTAL
        ), "Basket total message is not presented"
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price == basket_price, (
            f"Product price ({product_price}) is not equal to basket price ({basket_price})"
        )

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.MESSAGE_ABOUT_ADDING
        ), "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.MESSAGE_ABOUT_ADDING
        ), "Success message is presented, but should be disappeared"
