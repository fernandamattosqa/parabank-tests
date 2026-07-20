from behave import given
from features.pages.login_page import LoginPage
from pages.register_page import RegisterPage
from uuid import uuid4


def _create_valid_user(context):
    if hasattr(context, "valid_username") and hasattr(context, "valid_password"):
        return

    suffix = uuid4().hex[:10]
    context.valid_username = f"u{suffix}"
    context.valid_password = "SenhaForte123"

    register_page = RegisterPage(context.driver, context.base_url)
    register_page.open_register_page()
    register_page.fill_registration_form(
        first_name="QA",
        last_name="Automation",
        address="Rua Teste, 123",
        city="Santo André",
        state="SP",
        zip_code="09100-000",
        phone="11999999999",
        ssn=str(int(suffix[:9], 16)).zfill(9)[:9],
        username=context.valid_username,
        password=context.valid_password,
        confirm=context.valid_password,
    )
    register_page.submit_registration()
    success = register_page.get_success_message()
    assert "Your account was created successfully" in success, \
        f"Falha ao preparar usuário válido. Mensagem: {success}"


@given('que existe um usuário válido recém-cadastrado')
def step_create_valid_user(context):
    _create_valid_user(context)

@given('que estou logado com usuário válido')
def step_login_valid(context):
    _create_valid_user(context)

    context.login_page = LoginPage(context.driver, context.base_url)
    context.login_page.open_login_page()
    context.login_page.login(context.valid_username, context.valid_password)

    # Valida se o login foi bem-sucedido
    assert context.login_page.is_logged_in(), "Login falhou, usuário não autenticado"
