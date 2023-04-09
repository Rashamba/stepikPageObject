from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_button_add_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_BASKET), "Button is not presented"

    def click_button_add_basket(self):
        button_add_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET)
        button_add_basket.click()

    def message_add_product_in_basket(self):
        name_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        name_product_in_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_BASKET).text
        assert name_product == name_product_in_basket, f"The product name does not match. Expected '{name_product}', got '{name_product_in_basket}'"

    def price_basket(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        assert price_product == price_basket, f"The cost of the product in the basket does not match. Expected '{price_product}', got '{price_basket}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD_BASKET), "Success message is presented, but should not be"

    def the_success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD_BASKET), "Success message is presented, but should not be"
