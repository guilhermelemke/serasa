Feature: Login Page

    Intended to test if the page behaves according to the user actions on login

    Scenario: Login on Searsa page without informing CPF
    Given the user is on Serasa homepage
    When the user clicks on ENTRAR
    And the user clicks on Confirmar
    Then the message 'Por favor preencha seu CPF.' should be displayed