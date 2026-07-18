Feature: Registro inválido no ParaBank

  Scenario: Registro com dados incompletos
    Given que estou na página de registro
    When eu preencho um formulário incompleto
    And eu envio o formulário de registro
    Then devo ver uma mensagem de erro de validação
