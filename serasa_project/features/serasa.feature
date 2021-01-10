Feature: Login Page

    Intended to test if the page behaves according to the user actions on login

    Scenario Outline: Login on Serasa Page
    Given the user is on Serasa homepage on "https://www.serasaconsumidor.com.br"
    When the user clicks on ENTRAR
    And the user informs the CPF <cpf>
    And the user clicks on Confirmar
    Then the message <message> should be displayed

    Examples:
        | cpf           | message                                |
        | ""            | "Por favor preencha seu CPF."          |
        | "12345678900" | "Você precisa informar um CPF válido." |

"""
    Scenario: Login on Serasa page informing a valid CPF
    Given the user is on Serasa homepage on "https://www.serasaconsumidor.com.br"
    When the user clicks on ENTRAR
    And the user informs the CPF "04603676093"
    Then the message "Você precisa informar um CPF válido." should be displayed
"""








"""
    Scenario: Login on Serasa page without informing CPF
    Given the user is on Serasa homepage on "https://www.serasaconsumidor.com.br"
    When the user clicks on ENTRAR
    And the user clicks on Confirmar
    Then the message "Por favor preencha seu CPF." should be displayed

    Scenario: Login on Serasa page informing an invalid CPF
    Given the user is on Serasa homepage on "https://www.serasaconsumidor.com.br"
    When the user clicks on ENTRAR
    And the user informs the CPF "12345678900"
    Then the message "Você precisa informar um CPF válido." should be displayed
"""
