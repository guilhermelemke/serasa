from selenium.webdriver import Firefox
from behave import given, when, then
from Pages.indexPage import IndexPage
from Pages.loginPage import LoginPage
from Pages.accountPage import AccountPage

web = {
    'homepage': 'https://www.serasaconsumidor.com.br'
}
 
browser = Firefox()

@given('the user is on Serasa homepage on {homepage}')
def go_to_page(context, homepage):
    browser.get('https://www.serasaconsumidor.com.br')
    context.homepage = IndexPage(browser)

@when('the user clicks on ENTRAR')
def click_enter(context):
    context.homepage.click_enter()

@when('the user clicks on Confirmar')
def click_confirm(context):
    context.homepage = LoginPage(browser)
    context.homepage.click_confirm()

@then('the message {element} should be displayed')
def assert_message(context, element):
    assert element == context.password_requirements_message()

@when('the user informs the CPF {cpf}')
def enter_cpf(context, cpf):
    context.homepage = LoginPage(browser)
    context.homepage.enter_cpf(cpf)