Feature: Login no ParaBank

  Scenario: Login com usuário válido
    Given que existe um usuário válido recém-cadastrado
    And que estou na página de login
    When eu informo as credenciais do usuário válido criado
    And eu clico em logar
    Then devo ver "Accounts Overview"

  Scenario Outline: Tentativas de login com credenciais inválidas
    Given que estou na página de login
    When eu informo o usuário "<username>" e senha "<password>"
    And eu clico em logar
    Then devo ver "<expected_message>"

    Examples:
      | username        | password     | expected_message   |
      | usuario_invalido| 100910       | Error!             |
      | nonexistentuser | 100910       | Error!             |

  Scenario: Logout do usuário
    Given que existe um usuário válido recém-cadastrado
    And que estou na página de login
    When eu informo as credenciais do usuário válido criado
    And eu clico em logar
    Then devo realizar logout
