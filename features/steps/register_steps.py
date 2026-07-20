from behave import given, when, then
from uuid import uuid4

from pages.register_page import RegisterPage


def _normalize(value):
    if value == "__EMPTY__":
        return ""
    return value

@given('que estou na página de registro')
def step_open_register_page(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.open_register_page()

@when('eu preencho o formulário com dados válidos')
def step_fill_form(context):
    unique_suffix = f"u{uuid4().hex[:10]}"
    context.register_page.fill_registration_form(
        first_name="Fernanda",
        last_name="Silva",
        address="Rua Teste, 123",
        city="Santo André",
        state="SP",
        zip_code="09100-000",
        phone="11999999999",
        ssn="123-45-6789",
        username=unique_suffix,
        password="senha123",
        confirm="senha123"
    )


@when('eu preencho o formulário inválido com "{first_name}", "{last_name}", "{address}", "{city}", "{state}", "{zip_code}", "{phone}", "{ssn}", "{username}", "{password}", "{confirm}"')
def step_fill_invalid_form(context, first_name, last_name, address, city, state, zip_code, phone, ssn, username, password, confirm):
    context.register_page.fill_registration_form(
        first_name=_normalize(first_name),
        last_name=_normalize(last_name),
        address=_normalize(address),
        city=_normalize(city),
        state=_normalize(state),
        zip_code=_normalize(zip_code),
        phone=_normalize(phone),
        ssn=_normalize(ssn),
        username=_normalize(username),
        password=_normalize(password),
        confirm=_normalize(confirm),
    )

@when('eu envio o formulário de registro')
def step_submit_form(context):
    context.register_page.submit_registration()

@then('devo ver a mensagem de sucesso "{expected_message}"')
def step_validate_register_success(context, expected_message):
    message = context.register_page.get_success_message()
    assert expected_message in message, \
        f"Esperado '{expected_message}', mas obtido '{message}'"


@then('devo ver o erro de validação "{expected_error}"')
def step_validate_register_error(context, expected_error):
    errors = context.register_page.get_validation_errors()
    assert any(expected_error == error for error in errors), \
        f"Erro esperado '{expected_error}' não encontrado. Erros atuais: {errors}"
