Feature: Cadastro no ParaBank

  Scenario Outline: Registro com diferentes validações de entrada
    Given que estou na página de registro
    When eu preencho o formulário com os dados:<first_name>,<last_name>,<address>,<city>,<state>,<zip_code>,<phone>,<ssn>,<username>,<password>
    And eu envio o formulário de registro
    Then devo ver "<expected_message>"

    Examples:
      | first_name | last_name | address          | city        | state | zip_code  | phone        | ssn      | username       | password | expected_message                                             |
      | Fernanda   | Teste     | Rua Exemplo 123 | Santo André | SP    | 09000-000 | 11999999999  | 123456789 | userauto123    | senha123 | Your account was created successfully                       |
      |            | Teste     | Rua Exemplo 123 | Santo André | SP    | 09000-000 | 11999999999  | 123456789 |               |          | Error                                                        |
      | Fernanda   | Teste     | Rua Exemplo 123 | Santo André | SP    | 09000-000 | abc          | 123456789 | useremail      | senha123 | Error                                                        |
      | Fernanda   | Teste     | Rua Exemplo 123 | Santo André | SP    | 09000-000 | 11999999999  | 123456789 | userweak       | 123      | Error                                                        |
      | Fernanda   | Teste     | Rua Exemplo 123 | Santo André | SP    | 09000-000 | 11999999999  | 123456789 | userauto123    | senha123 | Error                                                        |
