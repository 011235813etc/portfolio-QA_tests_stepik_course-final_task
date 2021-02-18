from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес

        # ищем кнопку для перехода на страницу регистрации
        login_page = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        # переходим на страницу регистрации
        login_page.click()
        # получаем url текущей страницы
        current_url = self.browser.current_url
        # проверяем наличие слова "login" в url текущей страницы
        assert "login" in current_url, "Login page don't have 'login' word in url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
