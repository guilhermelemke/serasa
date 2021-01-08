from selenium.webdriver import Firefox
from behave import given, when, then
from Pages.indexPage import IndexPage
from Pages.loginPage import LoginPage
#from Pages.accountPage import AccountPage

website = {
    'homepage': 'https://www.serasaconsumidor.com.br'
}
 
browser = Firefox()

@given('the user is on Serasa {homepage}')
def go_to_page(context, homepage):
    context.homepage = IndexPage(browser, 'https://www.serasaconsumidor.com.br')
    context.homepage.open()

@when('the user clicks on ENTRAR')
def click_enter(context):
    context.homepage.click_enter()

@when('the user clicks on Confirmar')
def click_confirm(context):
    context.homepage.click_confirm()

@Then('the message {element} should be displayed')
def assert_message(context, element):
    pass
