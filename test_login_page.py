from .pages.login_page import LoginPage
from time import sleep
from .pages.locators import LoginPageLocators


def test_guest_can_go_to_enter_account(browser):
    link = LoginPageLocators.LOGIN_URL
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = LoginPage(browser, link)
    # открываем страницу
    page.open()
    # выполняем метод проверки наличия формы войти в аккаунт
    page.should_be_login_form()
    sleep(3)


def test_guest_can_go_to_register_account(browser):
    link = LoginPageLocators.LOGIN_URL
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = LoginPage(browser, link)
    # открываем страницу
    page.open()
    # выполняем метод проверки наличия формы регистрации
    page.should_be_register_form()
    sleep(3)


def test_correct_url_page_enter_or_register(browser):
    link = LoginPageLocators.LOGIN_URL
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()
    sleep(2)
