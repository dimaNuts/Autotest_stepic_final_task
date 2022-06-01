# сделать импорт базового класса BasePage:
from .base_page import BasePage
from .locators import MainPageLocators


# В нем создайте класс  MainPage. Его нужно сделать наследником класса BasePage.
# Класс-предок в Python указывается в скобках:
class MainPage(BasePage):
    # нужно указать аргумент self , чтобы иметь доступ к атрибутам и методам класса:
    def go_to_login_page(self):
        # Так как браузер у нас хранится как аргумент класса BasePage,
        # обращаться к нему нужно соответствующим образом с помощью self:
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    # Сейчас мы намеренно сделали селектор неправильным, чтобы посмотреть,
    # что именно выдаст тест, если поймает баг. Это хорошая практика:
    # писать сначала красные тесты и только потом делать их зелеными
    def should_be_login_link(self):
        assert self.browser.find_element(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
# Теперь модифицируем метод проверки ссылки на логин так, чтобы он выдавал адекватное сообщение об ошибке:
# добавили асерт, исправлен селекетр_инвалид, добавлено сообщение в случае ассерта
# Теперь в классе MainPage замените все строки, где содержится "#login_link", убрали BY