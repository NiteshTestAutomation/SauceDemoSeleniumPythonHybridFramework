import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.LoginPage import LoginPage
from pages.ProductPage import ProductPage
from tests.BaseTest import BaseTest
from utilities import ExcelReader


class TestProduct(BaseTest):
    @pytest.mark.parametrize("username,password", ExcelReader.get_data_from_excel("excelFile/SauceLab.xlsx", "Login"))
    def test_addProductToCart(self,username,password):
        login = LoginPage(self.driver)
        login.enterLoginDetails(username,password)
        product = ProductPage(self.driver)
        product.viewSauceLabBagProduct_and_AddToCart()
        assert product.getNumberOfItemAddedToCart().__eq__("1")
