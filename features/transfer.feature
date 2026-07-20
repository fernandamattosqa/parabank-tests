Feature: Transferência de fundos
  Como cliente do Parabank
  Quero realizar transferências entre contas
  Para validar mensagens de sucesso e erro

  Background:
    Given que estou logado com usuário válido
    And que estou na página de Transfer Funds

  Scenario Outline: Testar diferentes valores de transferência
    When eu realizo uma transferência de "<amount>" entre contas disponíveis
    Then <expected>

    Examples:
      | amount | expected                                        |
      | 100    | devo ver a mensagem de sucesso da transferência |
      | -50    | devo ver a mensagem de erro da transferência    |
      | abc    | devo ver a mensagem de erro da transferência    |
