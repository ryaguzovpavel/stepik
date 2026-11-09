from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_is_empty(self):
        basket_text = self.browser.find_element(*BasketPageLocators.BASKET_CONTENT).text
        assert "Your basket is empty" in basket_text
