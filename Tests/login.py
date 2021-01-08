from selenium.webdriver import Firefox
from time import sleep
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from serasa.features.steps.Pages.indexPage import IndexPage
from serasa.features.steps.Pages.loginPage import LoginPage
import HtmlTestRunner


class LoginTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.browser = Firefox()
        self.browser.implicitly_wait(10)

    def test_01_login_empty_cpf(self):
        browser = self.browser

        browser.get('https://www.serasaconsumidor.com.br')

        #index_page = IndexPage(browser)
        index_page.click_enter()

        login = LoginPage(browser)
        #sleep(2)
        login.click_confirm()
        #sleep(2)
        login.enter_cpf('')
        #sleep(2)
        login.click_confirm()
        #sleep(2)
        message = login.emty_cpf_message()
        self.assertEqual(message, "Por favor preencha seu CPF.")
        #sleep(2)

    def test_02_login_invalid_cpf(self):
        browser = self.browser

        browser.get('https://www.serasaconsumidor.com.br')

        index_page = IndexPage(browser)
        index_page.click_enter()

        login = LoginPage(browser)
        #sleep(2)
        login.click_confirm()
        #sleep(2)
        login.enter_cpf('12345678900')
        #sleep(2)
        login.click_confirm()
        #sleep(2)
        message = login.invalid_cpf_message()
        self.assertEqual(message, "Você precisa informar um CPF válido.")
        #sleep(2)

    def test_03_login_valid_cpf(self):
        browser = self.browser

        browser.get('https://www.serasaconsumidor.com.br')

        index_page = IndexPage(browser)
        index_page.click_enter()

        login = LoginPage(browser)
        #sleep(2)
        login.click_confirm()
        #sleep(2)
        login.enter_cpf('04603676093')
        #sleep(2)
        login.click_confirm() 
        #sleep(2)
        #message = login.invalid_cpf_message()
        #self.assertEqual(message, "Você precisa informar um CPF válido.")
        #sleep(2)

    @classmethod
    def tearDownClass(self):
        self.browser.close()
        self.browser.quit()
        print('Test Completed')


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Report"))
