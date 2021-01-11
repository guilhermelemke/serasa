Feature: Login Page

    Intended to test if the page behaves according to the user actions on login

    Scenario: Login on Serasa Page without CPF
    Given the user is on Serasa homepage on "https://www.serasaconsumidor.com.br"
    When the user clicks on ENTRAR
    And the user clicks on Confirmar
    Then the message Por favor preencha seu CPF. should be displayed


    Scenario: Login on Serasa Page with an invalid CPF
    Given the user is on Serasa homepage on "https://www.serasaconsumidor.com.br"
    When the user clicks on ENTRAR
    And the user informs the CPF "12345678900"
    And the user clicks on Confirmar
    Then the message Você precisa informar um CPF válido. should be displayed


    Scenario: Login on Serasa page informing a valid CPF and validating the password requirements text
    Given the user is on Serasa homepage on "https://www.serasaconsumidor.com.br"
    When the user clicks on ENTRAR
    And the user informs the CPF "04603676093"
    And the user clicks on Confirmar
    Then the password requirements text should be Sua senha não pode conter: seu nome, sobrenome, cpf, números sequenciais ou menos de 8 caracteres.