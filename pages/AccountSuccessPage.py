from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class AccountSuccessPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    account_creation_message_xpath = "/html/body/div[2]/div/div/h1"

    def retrieve_account_creation_message(self):
        return self.retrieve_element_text("account_creation_message_xpath",self.account_creation_message_xpath)