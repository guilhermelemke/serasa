from selenium.webdriver import Firefox
from time import sleep

url = 'https://www.serasaconsumidor.com.br'

# Acesse
# Utilize o bot"ao entrar
# não utilize valor no campo cpf e clique confirmar. Verifique a mensagem de cpf obrigatório
# informe cpf inválido e verifique a mensagem de necessidade de um cpf válido
# informe cpf válido e utilize o botão confirmar, verifique a apresentação do grupo de informações de senha

b = Firefox()
b.get(url)

def enter(browser):
    browser.find_element_by_css_selector('[data-gtm-name="Entrar"]').click()


def login(browser, *cpf):
    browser.find_element_by_class_name('_6qSv4dBZ').send_keys(cpf)
    browser.find_element_by_css_selector('[data-gtm-name="confirmar"]').click()


enter(b)
sleep(2)
login(b, '12345678900')
