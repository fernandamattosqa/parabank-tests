Feature: Cadastro no ParaBank
  Para garantir que o sistema valide corretamente os campos obrigatórios,
  o usuário deve ver mensagens de erro de validação quando o formulário estiver incompleto ou inválido.

  Scenario Outline: Registro com diferentes validações de entrada
    Given que estou na página de registro
    When eu preencho o formulário inválido com "<first_name>", "<last_name>", "<address>", "<city>", "<state>", "<zip_code>", "<phone>", "<ssn>", "<username>", "<password>", "<confirm>"
    And eu envio o formulário de registro
    Then devo ver o erro de validação "<expected_error>"

    Examples:
      | first_name | last_name | address         | city        | state | zip_code  | phone       | ssn        | username | password | confirm   | expected_error             |
      | __EMPTY__  | Teste     | Rua Exemplo 123 | Santo André | SP    | 09000-000 | 11999999999 | 123-45-6789| qauser01 | senha123 | senha123  | First name is required.    |
      | Fernanda   | Teste     | Rua Exemplo 123 | Santo André | SP    | 09000-000 | 11999999999 | 123-45-6789| __EMPTY__| senha123 | senha123  | Username is required.      |
      | Fernanda   | Teste     | Rua Exemplo 123 | Santo André | SP    | 09000-000 | 11999999999 | 123-45-6789| qauser03 | senha123 | senha999  | Passwords did not match.   |
