import pytest
from pages.LoginPage import LoginPage
from pages.ProductPage import ProductPage
from tests.BaseTest import BaseTest
from utilities import ExcelReader


class TestLogin(BaseTest):

  @pytest.mark.parametrize("username,password", ExcelReader.get_data_from_excel("excelFile/SauceLab.xlsx", "Login"))
  def test_loginsaucedemoapp(self,username,password):
      login = LoginPage(self.driver)
      login.enterLoginDetails(username,password)
      product = ProductPage(self.driver)
      pageHeader = product.getPageHeader()
      pageTitle = product.getPageTitle()
      if pageTitle in "Swag Labs":
          print("Verified Home Page title Swag Labs")
      else:
          print("Failure ")





