Feature: Cadastro no ParaBank
  Para garantir que o sistema valide corretamente os campos obrigatórios,
  o usuário deve ver mensagens de erro de validação quando o formulário estiver incompleto ou inválido.

  Scenario Outline: Registro com diferentes validações de entrada
    Given que estou na página de registro
    When eu preencho o formulário com os dados:<first_name>,<last_name>,<address>,<city>,<state>,<zip_code>,<phone>,<ssn>,<username>,<password>
    And eu envio o formulário de registro
    Then devo ver "<expected_message>"

    Examples:
      | first_name | last_name | address          | city        | state | zip_code  | phone        | ssn      | username    | password | expected_message                               |
      |            | Teste     | Rua Exemplo 123  | Santo André | SP    | 09000-000 | 11999999999  | 123456789 |             |          | Mensagens de validação nos campos obrigatórios |
      | Fernanda   | Teste     | Rua Exemplo 123  | Santo André | SP    | 09000-000 | abc          | 123456789 | useremail   | senha123 | Mensagens de validação nos campos obrigatórios |
      | Fernanda   | Teste     | Rua Exemplo 123  | Santo André | SP    | 09000-000 | 11999999999  | 123456789 | userweak    | 123      | Mensagens de validação nos campos obrigatórios |
