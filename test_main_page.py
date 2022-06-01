# В самом верху файла нужно импортировать класс, описывающий
# главную страницу(для директории использовать точку вначале):
from .pages.main_page import MainPage
from time import sleep


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser, link)
    # открываем страницу
    page.open()
    # выполняем метод страницы — переходим на страницу логина
    page.go_to_login_page()
    sleep(3)


# Убедитесь, что тест проходит, запустив его все той же командой:
# pytest -v --tb=line --language=en test_main_page.py
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    sleep(3)
