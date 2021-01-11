from selenium.webdriver import Firefox
from time import sleep
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from Pages.indexPage import IndexPage
from Pages.loginPage import LoginPage
from Pages.accountPage import AccountPage
import HtmlTestRunner


class LoginTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.browser = Firefox()
        self.browser.implicitly_wait(10)

    def test_01_login_empty_cpf(self):
        browser = self.browser

        browser.get('https://www.serasaconsumidor.com.br')

        index_page = IndexPage(browser)
        index_page.click_enter()

        login = LoginPage(browser)
        login.click_confirm()
        login.enter_cpf('')
        login.click_confirm()
        message = login.error_cpf_message()
        self.assertEqual(message, "Por favor preencha seu CPF.")

    def test_02_login_invalid_cpf(self):
        browser = self.browser

        browser.get('https://www.serasaconsumidor.com.br')

        index_page = IndexPage(browser)
        index_page.click_enter()

        login = LoginPage(browser)
        login.click_confirm()
        login.enter_cpf('12345678900')
        login.click_confirm()
        message = login.error_cpf_message()
        self.assertEqual(message, "Você precisa informar um CPF válido.")

    def test_03_login_valid_cpf(self):
        browser = self.browser

        browser.get('https://www.serasaconsumidor.com.br')

        index_page = IndexPage(browser)
        index_page.click_enter()

        login = LoginPage(browser)
        login.click_confirm()
        login.enter_cpf('04603676093')
        login.click_confirm()
        signup = AccountPage(browser)
        message = signup.password_requirements_message()
        self.assertEqual(message, "Sua senha não pode conter: seu nome, sobrenome, cpf, números sequenciais ou menos de 8 caracteres.")

    @classmethod
    def tearDownClass(self):
        self.browser.close()
        self.browser.quit()
        print('Test Completed')


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Report"))
