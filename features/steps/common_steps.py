from behave import given
from features.pages.login_page import LoginPage

@given('que estou logado com usuário válido')
def step_login_valid(context):
    # Usa login fixo para cenários que precisam de usuário já existente
    context.login_page = LoginPage(context.driver, context.base_url)
    context.login_page.open_login_page()
    context.login_page.login("Fernanda12", "100910")

    # Valida se o login foi bem-sucedido
    assert context.login_page.is_logged_in(), "Login falhou, usuário não autenticado"
