import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.CartPage import CartPage
from pages.LoginPage import LoginPage
from pages.ProductPage import ProductPage
from tests.BaseTest import BaseTest
from utilities import ExcelReader


class TestCart(BaseTest):
    @pytest.mark.parametrize("username,password", ExcelReader.get_data_from_excel("excelFile/SauceLab.xlsx", "Login"))
    def test_gotoCartandCheckoutProduct(self,username,password):
        #self.logger("---*** Cart Test ***---")
        login = LoginPage(self.driver)
        login.enterLoginDetails(username,password)
        product = ProductPage(self.driver)
        product.viewSauceLabBagProduct_and_AddToCart()
        cartPage = CartPage(self.driver)
        cartPage.openCartPage()
        cartPage.clickOncheckout()