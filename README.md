# ParaBank Selenium + Behave Automation

Este projeto é uma suíte de automação de testes web em Python, utilizando Behave, Selenium e Page Object Model (POM), com foco em qualidade, reutilização e boas práticas para processos seletivos de QA Automation.

## Tecnologias utilizadas
- Python 3
- Behave
- Selenium WebDriver
- Page Object Model (POM)
- WebDriverWait para esperas explícitas
- Logging e screenshots automáticos em caso de falha

## Estrutura do projeto
```text
project/
├── features/
│   ├── login.feature
│   ├── register.feature
│   ├── transfer.feature
│   ├── steps/
│   └── environment.py
├── pages/
├── locators/
├── utils/
├── config/
├── reports/
├── screenshots/
├── requirements.txt
├── README.md
└── .gitignore
```

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

