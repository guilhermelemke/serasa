from behave import given, when, then
from Pages import indexPage, loginPage, accountPage

website = {
    'homepage': 'https://www.serasaconsumidor.com.br'
}

@given('the user is on Serasa {homepage}')
def go_to_page(context, homepage):
    context.homepage = indexPage(context.browser, homepage)
    context.homepage.open()

@when('the user clicks on ENTRAR')
def click_enter(context):
    context.homepage.click_enter()

@And('the user clicks on Confirmar')
def click_confirm(context):
    context.homepage.click_confirm()

@Then('the message {element} should be displayed')
def assert_message(context, element):
    pass
    #element = element.lower().replace(' ', '_')
    #page_element = getattr(context.page, element)
    #assert 'element' == loginPage.empty_cpf_message