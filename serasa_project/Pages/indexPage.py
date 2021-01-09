from Locators.locators import Locators


class IndexPage():

    def __init__(self, browser):
        self.browser = browser

        self.enter_button_css_selector = Locators.enter_button_css_selector

    def click_enter(self):
        self.browser.find_element_by_css_selector(self.enter_button_css_selector).click()
