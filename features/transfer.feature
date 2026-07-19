Feature: Transferência de fundos
  Como cliente do Parabank
  Quero realizar transferências entre contas
  Para validar mensagens de sucesso e erro

  Background:
    Given que estou logado com usuário válido
    And que estou na página de Transfer Funds

  Scenario Outline: Testar diferentes valores de transferência
    When eu realizo uma transferência de <amount> da conta <from_account> para a conta <to_account>
    Then <expected>

    Examples:
      | amount | from_account | to_account | expected                                        |
      | 100    | 12345        | 67890      | devo ver a mensagem de sucesso da transferência |
      | 0      | 12345        | 67890      | devo ver a mensagem de sucesso da transferência |
      | @@     | 12345        | 67890      | devo ver a mensagem de erro da transferência    |
