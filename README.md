# ParaBank Selenium + Behave Automation

Este projeto é uma suíte de automação de testes web em Python, utilizando Behave, Selenium e Page Object Model (POM), com foco em qualidade, reutilização e boas práticas para processos seletivos de QA Automation.

## Tecnologias utilizadas
- Python 3
- Behave
- Selenium WebDriver
- Page Object Model (POM)
- WebDriverWait para esperas explícitas
- Logging e screenshots automáticos em caso de falha


# 🧪 Testes Automatizados ParaBank

Este projeto contém testes automatizados para o site [ParaBank](https://parabank.parasoft.com/), utilizando o framework **Behave** (BDD) com **Python** e **Selenium**.

---

## 📂 Estrutura do Projeto

| Pasta / Arquivo | Descrição |
|------------------|------------|
| **features/** | Contém os arquivos `.feature` escritos em Gherkin (cenários de teste). |
| **features/steps/** | Implementações dos steps (`Given`, `When`, `Then`) em Python. |
| **locators/** | Mapeamento dos elementos da interface (IDs, XPaths, CSS Selectors). |
| **pages/** | Classes de Page Object que encapsulam as ações das páginas. |
| **reports/** | Relatórios de execução dos testes em formato JUnit XML. |
| **utils/** | Funções auxiliares e utilitários. |
| **behave.ini** | Configurações do Behave. |
| **requirements.txt** | Lista de dependências do projeto. |
| **environment.py** | Configurações globais de setup e teardown dos testes. |

---

## 🚀 Como Executar os Testes

1. **Instalar dependências**
   ```bash
   pip install -r requirements.txt


## Requisitos
- Python 3.10+
- Google Chrome instalado
- ChromeDriver compatível com a versão do Chrome

## Instalação
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Execução
```bash
python -m behave
```

## Geração de relatório HTML
```bash
python -m behave -f html -o reports/behave-report.html
```

## Visualizar evidências
- Screenshots são salvos em reports/screenshots
- Logs aparecem no console durante a execução

## Boas práticas aplicadas
- Separação entre features, steps, pages, locators e utilitários
- Hooks Before/After para abertura e fechamento do navegador
- Esperas explícitas com WebDriverWait
- Centralização de elementos em locators
- Reutilização de steps e funções utilitárias
- Tratamento de exceções e screenshot em falha

