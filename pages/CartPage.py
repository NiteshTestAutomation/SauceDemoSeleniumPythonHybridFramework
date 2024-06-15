from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.CheckoutPage import CheckoutPage


class CartPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    shoppingcart_link = "//*[@id='shopping_cart_container']/a"
    checkout_btn = "//*[@class='btn_action checkout_button']"

    def openCartPage(self):
        self.driver.find_element(By.XPATH,self.shoppingcart_link).click()

    def clickOncheckout(self):
        self.driver.find_element(By.XPATH,self.checkout_btn).click()
        return CheckoutPage(self)

