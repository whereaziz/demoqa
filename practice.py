import pytest
import time
import os
from playwright.sync_api import sync_playwright, expect

# Константы для тестирования
BASE_URL = "https://demoqa.com"
FORMS_URL = f"{BASE_URL}/Practice-form"

# Тестовые данные
USER_DATA = {
    "First name":"Vasiliy",
    "Last name":"Pupkin",
    "Email":"vasyapupkin@gmail.com",
    "Gender":"Male",
    "Mobile":"+71112223344",
    "Date_of_birth":"30 Mar 2010",
    "Subjects":"Economics",
    "Hobbies":"Reading",
    "Picture":"",
    "Current_address":"Netaji Subhash Marg, Lal Qila, Chandni Chowk, New Delhi",
    "State_and_City":["NCR", "Delhi"]
}

# Фикстура для инициализации Playwright и создания страницы
@pytest.fixture
def page():
    # Запускаем Playwright
    with sync_playwright() as playwright:
        # Создаём браузер и страницу
        browser = playwright.chromium.launch(
            headless=False)  # headless=False позволяет видеть браузер во время выполнения
        page = browser.new_page()

        # Настраиваем размер окна браузера
        page.set_viewport_size({"width": 1920, "height": 1080})

        # Передаём страницу в тест
        yield page

        # Закрываем браузер после окончания теста
        browser.close()

# Заполняем текстовые поля
page.fill("#firstName", new_user["firstName"])
page.fill("#lastName", new_user["lastName"])