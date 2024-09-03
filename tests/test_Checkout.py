import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.LoginPage import LoginPage
from pages.ProductPage import ProductPage
from tests.BaseTest import BaseTest
from utilities import ExcelReader


class TestCheckout(BaseTest):

     @pytest.mark.parametrize("username,password", ExcelReader.get_data_from_excel("excelFile/SauceLab.xlsx", "Login"))
     def test_enterCheckoutInformation(self,username,password):
        #self.logger("---*** Checkout Test ***---")
        login = LoginPage(self.driver)
        login.enterLoginDetails(username,password)
        product = ProductPage(self.driver)
        product.viewSauceLabBagProduct_and_AddToCart()
        cartPage = CartPage(self.driver)
        cartPage.openCartPage()
        cartPage.clickOncheckout()
        checkout = CheckoutPage(self.driver)
        checkout.enterCheckoutDetails_and_Continue()
        actualMessage = checkout.getorderSuccessMessage()
        expectedMessage = "THANK YOU FOR YOUR ORDER"
        if actualMessage in expectedMessage:
           print("Order placed Successfully")
        else:
           print("Order not placed ")

