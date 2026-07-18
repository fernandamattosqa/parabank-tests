import random
import string

from behave import given, then, when

from features.pages.login_page import LoginPage
from features.pages.register_page import RegisterPage
from features.pages.transfer_page import TransferPage
from utils.helpers import logger


@given('que estou na página de registro')
def step_open_register_page(context):
    context.register_page = RegisterPage(context.driver, context.base_url)
    context.register_page.open_register_page()


@given('que estou na página de login')
def step_open_login_page(context):
    context.login_page = LoginPage(context.driver, context.base_url)
    context.login_page.open_login_page()


@given('que estou logado com usuário válido')
def step_login_valid(context):
    context.login_page = LoginPage(context.driver, context.base_url)
    if not hasattr(context, "username") or not hasattr(context, "password"):
        context.username = f"user{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}"
        context.password = "senha123"
        context.register_page = RegisterPage(context.driver, context.base_url)
        context.register_page.open_register_page()
        context.register_page.fill_form(
            first_name="Auto",
            last_name="User",
            address="Rua Exemplo 1",
            city="Cidade",
            state="SP",
            zip_code="00000-000",
            phone="11999999999",
            ssn="123456789",
            username=context.username,
            password=context.password,
        )
        context.register_page.submit()

    context.login_page.open_login_page()
    if not context.login_page.is_logged_in():
        context.login_page.login(context.username, context.password)


@given('estou na página de Transfer Funds')
def step_open_transfer_page(context):
    context.transfer_page = TransferPage(context.driver, context.base_url)
    context.transfer_page.open_transfer_page()


@when('eu informo o usuário "{username}" e senha "{password}"')
def step_login_with_credentials(context, username, password):
    context.current_username = username
    context.current_password = password
    context.login_page.fill_credentials(username or "", password or "")


@when('eu preencho o formulário com os dados:{first_name},{last_name},{address},{city},{state},{zip_code},{phone},{ssn},{username},{password}')
def step_fill_registration_form(context, first_name, last_name, address, city, state, zip_code, phone, ssn, username, password):
    context.register_page.fill_form(
        first_name=first_name or "",
        last_name=last_name or "",
        address=address or "",
        city=city or "",
        state=state or "",
        zip_code=zip_code or "",
        phone=phone or "",
        ssn=ssn or "",
        username=username or "",
        password=password or "",
    )


@when('eu envio o formulário de registro')
def step_submit_registration(context):
    context.register_page.submit()


@when('eu preencho um formulário incompleto')
def step_fill_incomplete_registration(context):
    context.register_page.fill_form(
        first_name="",
        last_name="Teste",
        address="Rua Exemplo 123",
        city="Santo André",
        state="SP",
        zip_code="09000-000",
        phone="11999999999",
        ssn="123456789",
        username="",
        password="",
    )


@then('devo ver uma mensagem de erro de validação')
def step_verify_registration_validation_error(context):
    assert context.register_page.get_error_message(), "Mensagem de erro de validação não encontrada"


@when('eu clico em logar')
def step_click_login(context):
    if hasattr(context, "login_page"):
        context.login_page.click_login_button()


@when('eu informo a conta origem "{from_account}", conta destino "{to_account}" e valor "{amount}"')
def step_fill_transfer(context, from_account, to_account, amount):
    context.transfer_page.fill_transfer(from_account, to_account, amount)


@when('eu envio a transferência')
def step_submit_transfer(context):
    context.transfer_page.submit()


@then('devo ver "{expected_message}"')
def step_assert_text(context, expected_message):
    if expected_message == "Accounts Overview":
        login_page = getattr(context, "login_page", None)
        assert login_page and login_page.is_logged_in(), "Usuário não entrou na área logada"
    elif expected_message == "Error":
        login_page = getattr(context, "login_page", None)
        register_page = getattr(context, "register_page", None)
        transfer_page = getattr(context, "transfer_page", None)
        error_messages = []
        if login_page:
            error_messages.append(login_page.get_error_message())
        if register_page:
            error_messages.append(register_page.get_error_message())
        if transfer_page:
            error_messages.append(transfer_page.get_error_message())
        assert any(error_messages) or "Error" in (getattr(context, "driver", None).page_source if hasattr(context, "driver") else ""), "Mensagem de erro não encontrada"
    elif expected_message == "Transfer Complete!":
        transfer_page = getattr(context, "transfer_page", None)
        assert transfer_page and "Transfer Complete" in transfer_page.get_success_message(), "Confirmação de transferência não encontrada"
    else:
        register_page = getattr(context, "register_page", None)
        assert register_page and expected_message in register_page.get_success_message(), f"Mensagem esperada não encontrada: {expected_message}"

@then('devo realizar logout')
def step_logout(context):
    context.login_page.logout()
    logger.info("Logout realizado com sucesso")
