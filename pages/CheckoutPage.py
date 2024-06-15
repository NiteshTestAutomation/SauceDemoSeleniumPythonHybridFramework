from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class CheckoutPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    firstName_filed = "first-name"
    secondName_filed = "last-name"
    postCode_filed = "postal-code"
    continue_button = "//*[@class='btn_primary cart_button']"
    finish_button = "//*[contains(text(),'FINISH')]"
    order_success_message = "//*[@class='complete-header']"


    def enterCheckoutDetails_and_Continue(self):
        firstName = "Nitesh"
        lastName = "Badge"
        postCode = "15226"

        self.driver.find_element(By.ID,self.firstName_filed).send_keys(firstName)
        self.driver.find_element(By.ID,self.secondName_filed).send_keys(lastName)
        self.driver.find_element(By.ID,self.postCode_filed).send_keys(postCode)
        self.driver.find_element(By.XPATH,self.continue_button).click()
        self.driver.find_element(By.XPATH,self.finish_button).click()

    def getorderSuccessMessage(self):
        actualMessage = self.driver.find_element(By.XPATH,self.order_success_message).text
        return actualMessage

