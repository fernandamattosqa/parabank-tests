from selenium.webdriver.common.by import By

class LoginLocators:
    # Campos de login
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")

    # Botão de login
    LOGIN_BUTTON = (By.XPATH, "//input[@type='submit' and @value='Log In']")

    # Mensagem de erro exibida no painel direito
    # Ajuste: muitas vezes o erro aparece como <p class="error">Error!</p>
    ERROR_MESSAGE = (By.CSS_SELECTOR, "#rightPanel p.error")

    # Mensagem exibida após login bem-sucedido
    WELCOME_MESSAGE = (By.CSS_SELECTOR, "h1.title")

    # Link de logout
    LOGOUT_LINK = (By.LINK_TEXT, "Log Out")

    # Título da tela de login (opcional, útil para validações)
    LOGIN_TITLE = (By.CSS_SELECTOR, "#rightPanel > h1")
