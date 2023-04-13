from selenium.webdriver.common.by import By

from pages.auth_page import AuthPageHelper
from pages.base_page import BasePage


class PassRecoveryPageLocators:
    """ Класс локаторов на странице Восстановления пароля """

    FORM_TITLE = (By.CLASS_NAME, "card-container__title")
    USERNAME = (By.ID, "username")
    CAPTCHA = (By.CLASS_NAME, "rt-captcha__image")
    GO_BTN = (By.XPATH, '//button[@id="reset"]')
    GO_BACK_LINK = (By.ID, "reset-back")
    TAB_PHONE = (By.ID, "t-btn-tab-phone")
    TAB_EMAIL = (By.ID, "t-btn-tab-mail")
    TAB_LOGIN = (By.ID, "t-btn-tab-login")
    TAB_LS = (By.ID, "t-btn-tab-ls")
    CAPTCHA_IMG = (By.CLASS_NAME, "rt-captcha__image")
    CAPTCHA_INPUT_FIELD = (By.XPATH, '//input[@id="captcha"]')
    LOGO_IMG = (By.CLASS_NAME, "rt-logo.main-header__logo")
    AGREEMENT_LINK = (By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[2]')
    ERROR_MESSAGE = (By.XPATH, '//span[@id="form-error-message"]')
    VALIDATION_ERROR_MESSAGE = (By.XPATH, '//*[@class="rt-input-container__meta rt-input-container__meta--error"]')


class PassRecoveryPageHelper(BasePage):
    """ Класс, содержащий методы для проверки страницы Восстановления пароля """

    @staticmethod
    def go_to_pass_recovery_page(browser):
        """ Открытие формы 'Восстановление пароля' """
        auth_page = AuthPageHelper(browser)
        auth_page.go_to_page()
        auth_page.forgot_password_link().click()
        return auth_page

    def form_title(self):
        """ Вывод заголовка отображаемой формы ввода данных """
        return self.find_element(PassRecoveryPageLocators.FORM_TITLE, time=10)

    def username_field(self):
        """ Вывод поля ввода данных аутентификатора пользователя """
        return self.find_element(PassRecoveryPageLocators.USERNAME, time=10)

    def enter_username(self, username):
        """ Ввод данных в поле идентификатора пользователя """
        username_field = self.find_element(PassRecoveryPageLocators.USERNAME)
        username_field.clear()
        username_field.send_keys(username)
        return username_field

    def captcha_img(self):
        """ Вывод картинки с капчей """
        return self.find_element(PassRecoveryPageLocators.CAPTCHA_IMG, time=10)

    def captcha_input_field(self):
        """ Вывод поля ввода капчи """
        return self.find_element(PassRecoveryPageLocators.CAPTCHA_INPUT_FIELD, time=10)

    def enter_captcha(self, captcha):
        """ Ввод данных в поле капчи """
        captcha_field = self.find_element(PassRecoveryPageLocators.CAPTCHA_INPUT_FIELD)
        captcha_field.clear()
        captcha_field.send_keys(captcha)
        return captcha_field

    def go_btn(self):
        """ Вывод кнопки 'Продолжить' """
        return self.find_element(PassRecoveryPageLocators.GO_BTN, time=5)

    def click_go_btn(self):
        """ Нажимает кнопку 'Продолжить' """
        return self.find_element(PassRecoveryPageLocators.GO_BTN, time=5).click()

    def go_back_link(self):
        """ Вывод ссылки 'Вернуться назад' """
        return self.find_element(PassRecoveryPageLocators.GO_BACK_LINK, time=5)

    def click_go_back_link(self):
        """ Нажимает ссылку 'Вернуться назад' """
        return self.find_element(PassRecoveryPageLocators.GO_BACK_LINK, time=5).click()

    def tab_menu_phone(self):
        """ Выбор аутентификации через телефон """
        return self.find_element(PassRecoveryPageLocators.TAB_PHONE, time=2)

    def click_phone(self):
        """ Нажимает таб меню 'Телефон' """
        return self.find_element(PassRecoveryPageLocators.TAB_PHONE, time=5).click()

    def tab_menu_email(self):
        """ Выбор аутентификации через электронную почту """
        return self.find_element(PassRecoveryPageLocators.TAB_EMAIL, time=2)

    def click_email(self):
        """ Нажимает таб меню 'Почта' """
        return self.find_element(PassRecoveryPageLocators.TAB_EMAIL, time=5).click()

    def tab_menu_login(self):
        """ Выбор аутентификации через 'Логин' """
        return self.find_element(PassRecoveryPageLocators.TAB_LOGIN, time=2)

    def click_login(self):
        """ Нажимает таб меню 'Логин' """
        return self.find_element(PassRecoveryPageLocators.TAB_LOGIN, time=5).click()

    def tab_menu_ls(self):
        """ Выбор аутентификации через 'Лицевой счет' """
        return self.find_element(PassRecoveryPageLocators.TAB_LOGIN, time=2)

    def click_ls(self):
        """ Нажимает таб меню 'Лицевой счёт' """
        return self.find_element(PassRecoveryPageLocators.TAB_LS, time=5).click()

    def agreement_link(self):
        """ Вывод ссылки на пользовательское соглашение из формы 'Восстановление пароля' """
        return self.find_element(PassRecoveryPageLocators.AGREEMENT_LINK, time=10)

    def form_error_message(self):
        """ Выводит сообщение об ошибке """
        return self.find_element(PassRecoveryPageLocators.ERROR_MESSAGE, time=10)

    def validation_error_message(self):
        """ Выводит сообщение об ошибке валидации """
        return self.find_element(PassRecoveryPageLocators.VALIDATION_ERROR_MESSAGE, time=10)
