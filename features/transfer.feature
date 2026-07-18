Feature: Transferência de Fundos

  Scenario Outline: Tentativas de transferência com diferentes entradas
    Given que estou logado com usuário válido
    And estou na página de Transfer Funds
    When eu informo a conta origem "<from_account>", conta destino "<to_account>" e valor "<amount>"
    And eu envio a transferência
    Then devo ver "<expected_message>"

    Examples:
      | from_account | to_account | amount | expected_message     |
      | 12345        | 54321      | 100.00 | Transfer Complete!   |
      | 12345        | 54321      | 999999  | Error                |
      | 12345        | 54321      | 0       | Error                |
      | 12345        | 54321      | -10     | Error                |
      | 12345        | 12345      | 10      | Error                |
      | 99999        | 54321      | 10      | Error                |
