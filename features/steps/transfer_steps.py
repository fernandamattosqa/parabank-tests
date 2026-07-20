from behave import given, when, then
from features.pages.transfer_page import TransferPage

@given('que estou na página de Transfer Funds')
def step_open_transfer_page(context):
    context.transfer_page = TransferPage(context.driver, context.base_url)
    context.transfer_page.open_transfer_page()

@when('eu realizo uma transferência de "{amount}" entre contas disponíveis')
def step_fill_transfer(context, amount):
    context.transfer_page.fill_transfer(amount)
    context.transfer_page.submit()

@then('devo ver a mensagem de sucesso da transferência')
def step_transfer_success(context):
    msg = context.transfer_page.get_success_message()
    assert msg and "Transfer Complete" in msg, f"Mensagem inesperada: {msg}"

@then('devo ver a mensagem de erro da transferência')
def step_transfer_error(context):
    msg = context.transfer_page.get_error_message()
    assert msg and "Error" in msg, "Mensagem de erro não encontrada ou incorreta"
