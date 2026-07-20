from behave import given, when, then
from pages.login_page import LoginPage

@given('que estou na página de login')
def step_open_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open_login_page()

@when('eu informo o usuário "{username}" e senha "{password}"')
def step_fill_credentials(context, username, password):
    context.login_page.fill_credentials(username, password)


@when('eu informo as credenciais do usuário válido criado')
def step_fill_dynamic_valid_credentials(context):
    assert hasattr(context, "valid_username") and hasattr(context, "valid_password"), \
        "Usuário válido não foi preparado para o cenário"
    context.login_page.fill_credentials(context.valid_username, context.valid_password)

@when('eu clico em logar')
def step_click_login(context):
    context.login_page.click_login_button()

@then('devo ver "{expected_message}"')
def step_validate_message(context, expected_message):
    login_page = context.login_page

    if expected_message == "Accounts Overview":
        # Cenário positivo
        assert login_page.is_logged_in(), "Usuário não logou com sucesso"
    elif expected_message == "Error!":
        error_message = login_page.get_error_message()
        assert error_message and (
            "Error" in error_message or "could not be verified" in error_message
        ), f"Mensagem de erro inesperada: '{error_message}'"
    else:
        # Cenário negativo
        error_message = login_page.get_error_message()
        assert error_message == expected_message, \
            f"Esperado '{expected_message}', mas obtido '{error_message}'"

@then('devo realizar logout')
def step_logout(context):
    login_page = context.login_page
    login_page.logout()
    # Valida que voltou para tela de login
    assert "login" in context.driver.current_url or "index" in context.driver.current_url, \
        "Logout não redirecionou para tela de login"
