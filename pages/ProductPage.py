from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.CartPage import CartPage


class ProductPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    page_header = "//*[@class='product_label']"
    sauceLabBackpack = "//*[@id='item_4_img_link']/parent::div"
    addToCart_button = "//*[@class='btn_primary btn_inventory']"
    itemAdded_toCart = "//*[@id='shopping_cart_container']/a/span"


    def getPageHeader(self):
        pageHeaderText = self.driver.find_element(By.XPATH,self.page_header).text
        return pageHeaderText

    def viewSauceLabBagProduct_and_AddToCart(self):
       # self.driver.find_element(By.CLASS_NAME,self.sauceLabBackpack).click()
        self.driver.find_element(By.XPATH,self.sauceLabBackpack).click()
        self.driver.find_element(By.XPATH,self.addToCart_button).click()
        return CartPage(self)

    def getNumberOfItemAddedToCart(self):
        numOfItems = self.driver.find_element(By.XPATH,self.itemAdded_toCart).text
        return numOfItems

    def getPageTitle(self):
        pageTitle = self.driver.title
        return pageTitle
