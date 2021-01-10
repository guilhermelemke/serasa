from Locators.locators import Locators


class AccountPage():

    def __init__(self, browser):
        self.browser = browser
        
        self.password_message_class = Locators.password_message_class

    def password_requirements_message(self):
        msg = self.browser.find_element_by_xpath(self.password_message_class).text
        return msg
