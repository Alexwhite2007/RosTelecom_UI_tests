from selenium.webdriver.common.by import By

from pages.auth_page import AuthPageHelper
from pages.base_page import BasePage


# класс локаторов на странице Регистрации
class RegisterPageLocators:

    FORM_TITLE = (By.CLASS_NAME, "card-container__title")
    REGISTRATION_FORM = (By.CLASS_NAME, "register-form")
    FIRSTNAME = (By.NAME, "firstName")
    LASTNAME = (By.NAME, "lastName")
    REGION = (By.CSS_SELECTOR, "div[class*='register-form__dropdown']")
    EMAIL_PHONE = (By.ID, "address")
    PASSWORD = (By.ID, "password")
    PASSWORD_CONFIRM = (By.ID, "password-confirm")
    REG_BTN = (By.CSS_SELECTOR, "button[name='register']")
    AGREEMENT_LINK = (By.LINK_TEXT, "пользовательского соглашения")
    ERROR_MESSAGES = (By.XPATH, '//*[@class="rt-input-container__meta rt-input-container__meta--error"]')


class RegisterPageHelper(BasePage):
    """ Класс, содержащий методы для проверки страницы регистрации """

    @staticmethod
    def go_to_register_page(browser):
        """ Открытие формы регистрации """
        auth_page = AuthPageHelper(browser)
        auth_page.go_to_page()
        auth_page.register_link().click()
        return auth_page

    def form_title(self):
        """ Вывод заголовка отображаемой формы ввода данных """
        return self.find_element(RegisterPageLocators.FORM_TITLE, time=10)

    def registration_form(self):
        """ Вывод формы регистрации """
        return self.find_element(RegisterPageLocators.REGISTRATION_FORM, time=10)

    def firstname_field(self):
        """ Вывод поля для ввода имени """
        return self.find_element(RegisterPageLocators.FIRSTNAME, time=10)

    def enter_firstname(self, firstname):
        """ Ввод данных в поле 'имя' """
        self.firstname_field().send_keys(firstname)
        return self.firstname_field()

    def lastname_field(self):
        """ Вывод поля для ввода фамилии """
        return self.find_element(RegisterPageLocators.LASTNAME, time=10)

    def enter_lastname(self, lastname):
        """ Ввод данных в поле 'фамилия' """
        self.lastname_field().send_keys(lastname)
        return self.lastname_field()

    def region_dropdown(self):
        """ Вывод поля выбора региона """
        return self.find_element(RegisterPageLocators.REGION, time=10)

    def email_or_phone_field(self):
        """ Вывод поля для ввода почты или телефона """
        return self.find_element(RegisterPageLocators.EMAIL_PHONE, time=10)

    def password_field(self):
        """ Вывод поля для ввода пароля """
        return self.find_element(RegisterPageLocators.PASSWORD, time=10)

    def password_confirm_field(self):
        """ Вывод поля для ввода подтверждения пароля """
        return self.find_element(RegisterPageLocators.PASSWORD_CONFIRM, time=10)

    def enter_email_or_phone(self, email_phone):
        """ Ввод данных в поле 'Email или мобильный телефон' """
        email_phone_field = self.find_element(RegisterPageLocators.EMAIL_PHONE)
        email_phone_field.clear()
        email_phone_field.send_keys(email_phone)
        return email_phone_field

    def enter_password(self, password):
        """ Ввод данных в поле 'Пароль' """
        pass_field = self.find_element(RegisterPageLocators.PASSWORD)
        pass_field.clear()
        pass_field.send_keys(password)
        return pass_field

    def enter_password_confirm(self, password):
        """ Ввод данных в поле 'Подтверждение пароля' """
        pass_conf_field = self.find_element(RegisterPageLocators.PASSWORD_CONFIRM)
        pass_conf_field.send_keys(password)
        return pass_conf_field

    def register_btn(self):
        """ Выводит кнопку 'Зарегистрироваться' """
        return self.find_element(RegisterPageLocators.REG_BTN, time=5)

    def click_register_btn(self):
        """ Нажимает кнопку 'Зарегистрироваться' """
        return self.find_element(RegisterPageLocators.REG_BTN, time=5).click()

    def agreement_link(self):
        """ Выводит ссылку на 'пользовательское соглашение' """
        return self.find_element(RegisterPageLocators.AGREEMENT_LINK, time=5)

    def error_message(self):
        """ Вывод ошибки валидации в форме регистрации """
        return self.find_elements(RegisterPageLocators.ERROR_MESSAGES, time=2)

    def count_error_messages(self):
        """ Считает количество отображаемых ошибок валидации """
        errors_qty = self.find_elements(RegisterPageLocators.ERROR_MESSAGES, time=2)
        return len(errors_qty)