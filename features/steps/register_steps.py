from behave import given, when, then
from pages.register_page import RegisterPage

@given('que estou na página de registro')
def step_open_register_page(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.open_register_page()

@when('eu preencho o formulário com dados válidos')
def step_fill_form(context):
    context.register_page.fill_registration_form(
        first_name="Fernanda",
        last_name="Silva",
        address="Rua Teste, 123",
        city="Santo André",
        state="SP",
        zip_code="09100-000",
        phone="11999999999",
        ssn="123-45-6789",
        username="fernanda_teste",
        password="senha123",
        confirm="senha123"
    )

@when('eu envio o formulário de registro')
def step_submit_form(context):
    context.register_page.submit_registration()

@then('devo ver a mensagem de sucesso "{expected_message}"')
def step_validate_register_success(context, expected_message):
    message = context.register_page.get_success_message()
    assert message == expected_message, \
        f"Esperado '{expected_message}', mas obtido '{message}'"
