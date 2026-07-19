Feature: Cadastro bem-sucedido no ParaBank
  Para garantir que o sistema permita criar uma conta válida,
  o usuário deve ver a mensagem de sucesso quando todos os campos são preenchidos corretamente.

  Scenario: Registro com dados válidos
    Given que estou na página de registro
    When eu preencho o formulário com dados válidos
    And eu envio o formulário de registro
    Then devo ver a mensagem de sucesso "Your account was created successfully"
