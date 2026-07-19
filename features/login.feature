Feature: Login no ParaBank

  Scenario Outline: Tentativas de login com diferentes entradas
    Given que estou na página de login
    When eu informo o usuário "<username>" e senha "<password>"
    And eu clico em logar
    Then devo ver "<expected_message>"

    Examples:
      | username        | password     | expected_message   |
      | Fernanda12      | 100910       | Accounts Overview  |
      | usuario_invalido| 100910       | Error!             |
      | nonexistentuser | 100910       | Error!             |

  Scenario: Logout do usuário
    Given que estou na página de login
    When eu informo o usuário "Fernanda12" e senha "100910"
    And eu clico em logar
    Then devo realizar logout
