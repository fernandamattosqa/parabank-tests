Feature: Login no ParaBank

  Scenario Outline: Tentativas de login com diferentes entradas
    Given que estou na página de login
    When eu informo o usuário "<username>" e senha "<password>"
    And eu clico em logar
    Then devo ver "<expected_message>"

    Examples:
      | username         | password     | expected_message |
      | userauto123      | senha123     | Accounts Overview |
      | usuario_invalido | senha_errada | Error            |
      | nonexistentuser  | senha_errada | Error            |
      |  |  | Error |

  Scenario: Logout do usuário
    Given que estou na página de login
    When eu informo o usuário "userauto123" e senha "senha123"
    And eu clico em logar
    Then devo realizar logout
