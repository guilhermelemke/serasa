from behave import given, when, then
from selenium.webdriver import Firefox

@given('the user is on Serasa homepage')
def go_to_page(context):
    context.browser = Firefox()
    context.browser.get('https://selenium.dunossauro.live/todo_list.html')

@when('the user clicks on ENTRAR')
def click_enter(context):
    context.browser.find_element_by_id('todo-name')
    context.browser.find_element_by_id('todo-desc')
    context.browser.find_element_by_id('todo-submit')

@And('the user clicks on Confirmar')
def click_confirm(context):
    ...

@Then('the message '{pilha}' should be displayed')
def assert_message(context, pilha):
    ...