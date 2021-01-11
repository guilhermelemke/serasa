from selenium.webdriver import Firefox
from behave import given, when, then
from Pages.indexPage import IndexPage
from Pages.loginPage import LoginPage
from Pages.accountPage import AccountPage
from time import sleep


@given('the user is on Serasa homepage on {homepage}')
def go_to_page(context, homepage):
    context.browser.get('https://www.serasaconsumidor.com.br')
    context.homepage = IndexPage(context.browser)

@when('the user clicks on ENTRAR')
def click_enter(context):
    context.homepage.click_enter()

@when('the user clicks on Confirmar')
def click_confirm(context):
    context.homepage = LoginPage(context.browser)
    context.homepage.click_confirm()

@when('the user informs the CPF {cpf}')
def enter_cpf(context, cpf):
    context.homepage = LoginPage(context.browser)
    context.homepage.enter_cpf(cpf)

@then('the message {message} should be displayed')
def assert_message(context, message):
    actual_page = LoginPage(context.browser)
    assert actual_page.error_cpf_message() == message

@then('the password requirements text should be {password_requirements_text}')
def password_requirements_text(context, password_requirements_text):
    actual_page = AccountPage(context.browser)
    sleep(3)
    message = actual_page.password_requirements_message()
    assert message == password_requirements_text
