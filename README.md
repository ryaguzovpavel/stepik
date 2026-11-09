# Финальный проект — курс Stepik «Selenium и Python»

Автотесты для [selenium1py.pythonanywhere.com](http://selenium1py.pythonanywhere.com) на **pytest** и паттерне **Page Object**.

## Установка

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Нужен Chrome и совместимый ChromeDriver (или Firefox для `--browser_name=firefox`).

## Запуск

Все тесты с маркером для рецензии:

```bash
pytest -v --tb=line --language=en -m need_review
```

Пример с языком интерфейса:

```bash
pytest -v --language=es test_main_page.py
```

Негативные проверки:

```bash
pytest -v test_product_page_negative.py
```

## Структура

- `pages/` — Page Object (base, main, product, login, basket, locators)
- `conftest.py` — фикстура `browser`, опции `--language`, `--browser_name`
- `test_main_page.py`, `test_product_page.py` — основные сценарии
- `selenium-language-tests/` — задание про язык браузера (отдельная папка)
