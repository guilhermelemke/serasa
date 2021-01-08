from serasa.Locators.locators import Locators

class LoginPage():

    def __init__(self, browser):
        self.browser = browser
        
        self.cpf_field_class_name = Locators.cpf_field_class_name
        self.confirm_button_css_selector = Locators.confirm_button_css_selector
        self.cpf_message_class = Locators.cpf_message_class

    def enter_cpf(self, cpf):
        self.browser.find_element_by_class_name(Locators.cpf_field_class_name).clear()
        self.browser.find_element_by_class_name(Locators.cpf_field_class_name).send_keys(cpf)

    def click_confirm(self):
        self.browser.find_element_by_css_selector(Locators.confirm_button_css_selector).click()

    def emty_cpf_message(self):
        msg = self.browser.find_element_by_class_name(self.cpf_message_class).text
        return msg

    def invalid_cpf_message(self):
        msg = self.browser.find_element_by_class_name(self.cpf_message_class).text
        return msg
