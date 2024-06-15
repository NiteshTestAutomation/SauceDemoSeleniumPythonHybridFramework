from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.ProductPage import ProductPage
from utilities import ReadConfiguration
class LoginPage(BasePage):
    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)

    login_filed = "user-name"
    password_filed = "password"
    login_button = "login-button"

    def enterLoginDetails(self,userId,password):
        #username = ReadConfiguration.read_Configuaration("info","userName")
        #passord = ReadConfiguration.read_Configuaration("info", "passWord")
        #username = "standard_user"
        #password = "secret_sauce"
        self.driver.find_element(By.ID,self.login_filed).clear()
        self.driver.find_element(By.ID,self.login_filed).send_keys(userId)
        self.driver.find_element(By.ID,self.password_filed).send_keys(password)
        self.driver.find_element(By.ID,self.login_button).click()
        return ProductPage(self)