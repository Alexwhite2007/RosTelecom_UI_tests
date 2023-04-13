from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AuthPageLocators:
    """ Класс локаторов на странице авторизации """

    SIDE_LEFT = (By.ID, "page-left")
    SIDE_RIGHT = (By.ID, "page-right")
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    ENTER_BTN = (By.XPATH, '//*[@id="kc-login"]')
    BODY_LOGO = (By.CLASS_NAME, "rt-logo.main-header__logo")
    FORM_TITLE = (By.CLASS_NAME, "card-container__title")
    AUTH_FORM = (By.CLASS_NAME, "login-form")
    TABS_MENU = (By.CSS_SELECTOR, "div[class *='tabs-input-container__tabs']")
    TAB_PHONE = (By.ID, "t-btn-tab-phone")
    TAB_EMAIL = (By.ID, "t-btn-tab-mail")
    TAB_LOGIN = (By.ID, "t-btn-tab-login")
    TAB_LS = (By.ID, "t-btn-tab-ls")
    TAB_MODE = (By.XPATH, '// span[@class="rt-input__placeholder"]')
    PHONE_INPUT_FIELD = (By.XPATH, "//span[contains(text(), 'Мобильный телефон')]")
    EMAIL_INPUT_FIELD = (By.XPATH, "//span[contains(text(), 'Электронная почта')]")
    LOGIN_INPUT_FIELD = (By.XPATH, "//span[contains(text(), 'Логин')]")
    LS_INPUT_FIELD = (By.XPATH, "//span[contains(text(), 'Лицевой счёт')]")
    REMEMBER_ME = (By.CLASS_NAME, "rt-checkbox")
    FORGOT_PASSWORD_LINK = (By.XPATH, '//*[@id="forgot_password"]')
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")
    AGREEMENT_LINK = (By.LINK_TEXT, "пользовательского соглашения")
    SOCIAL_PROVIDERS = (By.CLASS_NAME, "social-providers")
    VK_LINK = (By.ID, "oidc_vk")
    OK_LINK = (By.ID, "oidc_ok")
    MAIL_LINK = (By.ID, "oidc_mail")
    GOOGLE_LINK = (By.ID, "oidc_google")
    YANDEX_LINK = (By.ID, "oidc_ya")
    ERROR_MESSAGE = (By.XPATH, '//*[@id="form-error-message"]')
    USERNAME_TEXT_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    CAPTCHA_IMG = (By.CLASS_NAME, "rt-captcha__image")


class AuthPageHelper(BasePage):
    """ Класс, содержащий методы для проверки страницы авторизации """

    TABS_MENU_ELEMENTS = ['Телефон', 'Почта', 'Логин', 'Лицевой счёт']
    LIST_ELEMENTS = ('\n'.join(map(str, TABS_MENU_ELEMENTS)))

    def side_left_body(self):
        """ Вывод левой части страницы авторизации """
        return self.find_element(AuthPageLocators.SIDE_LEFT, time=10)

    def side_right_body(self):
        """ Вывод правой части страницы авторизации """
        return self.find_element(AuthPageLocators.SIDE_RIGHT, time=10)

    def enter_username(self, username):
        """ Ввод данных в поле идентификатора пользователя вне зависимости от выбранного способа авторизации -
         'Мобильный телефон-Почта-Логин-Лицевой счет' """
        username_field = self.find_element(AuthPageLocators.USERNAME_FIELD)
        username_field.clear()
        username_field.send_keys(username)
        return username_field

    def enter_password(self, password):
        """ Ввод данных в поле 'Пароль' """
        password_field = self.find_element(AuthPageLocators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(password)
        return password_field

    def enter_button(self):
        """ Вывод кнопки 'Войти'"""
        return self.find_element(AuthPageLocators.ENTER_BTN, time=3)

    def click_enter_button(self):
        """ Нажимает кнопку 'Войти'"""
        return self.find_element(AuthPageLocators.ENTER_BTN, time=3).click()

    def body_logo(self):
        """ Выводит логотип 'РосТелеком' в теле страницы """
        return self.find_element(AuthPageLocators.BODY_LOGO, time=10)

    def form_title(self):
        """ Вывод заголовка отображаемой формы для ввода данных """
        return self.find_element(AuthPageLocators.FORM_TITLE, time=10)

    def auth_form(self):
        """ Вывод формы авторизации """
        return self.find_element(AuthPageLocators.AUTH_FORM, time=10)

    def tabs_menu(self):
        """ Вывод меню с выбором типа авторизации """
        return self.find_element(AuthPageLocators.TABS_MENU, time=10)

    def tab_menu_phone(self):
        """ Вывод меню с выбором типа авторизации """
        return self.find_element(AuthPageLocators.TAB_PHONE, time=10)

    def username_field(self):
        """ Вывод поля для ввода логина, независимо от выбранного способа ввода """
        return self.find_element(AuthPageLocators.USERNAME_FIELD, time=10)

    def password_field(self):
        """ Вывод поля для ввода пароля """
        return self.find_element(AuthPageLocators.PASSWORD_FIELD, time=10)

    def checkbox_remember_me(self):
        """ Вывод чекбокса 'Запомнить меня'"""
        return self.find_element(AuthPageLocators.REMEMBER_ME, time=10)

    def click_tab_menu_phone(self):
        """ Выбор авторизации через телефон """
        return self.find_element(AuthPageLocators.TAB_PHONE, time=2).click()

    def click_tab_menu_email(self):
        """ Выбор авторизации через электронную почту """
        return self.find_element(AuthPageLocators.TAB_EMAIL, time=2).click()

    def click_tab_menu_login(self):
        """ Выбор авторизации через логин """
        return self.find_element(AuthPageLocators.TAB_LOGIN, time=2).click()

    def click_tab_menu_ls(self):
        """ Выбор авторизации через лицевой счет """
        return self.find_element(AuthPageLocators.TAB_LS, time=2).click()

    def phone_input_field(self):
        """ Вывод поля ввода телефона при регистрации через телефон """
        return self.find_element(AuthPageLocators.PHONE_INPUT_FIELD, time=2)

    def email_input_field(self):
        """ Вывод поля ввода электронной почты при регистрации через электронную почту """
        return self.find_element(AuthPageLocators.EMAIL_INPUT_FIELD, time=2)

    def login_input_field(self):
        """ Вывод поля ввода логина при регистрации через логин """
        return self.find_element(AuthPageLocators.LOGIN_INPUT_FIELD, time=2)

    def ls_input_field(self):
        """ Вывод поля ввода лицевого счета при регистрации через лицевой счет """
        return self.find_element(AuthPageLocators.LS_INPUT_FIELD, time=2)

    def form_error_message(self):
        """ Вывод ошибки при вводе неверного логина или пароля """
        return self.find_element(AuthPageLocators.ERROR_MESSAGE, time=10)

    def forgot_password_link(self):
        """ Вывод ссылки 'Забыл пароль'"""
        return self.find_element(AuthPageLocators.FORGOT_PASSWORD_LINK, time=10)

    def agreement_contract_link(self):
        """ Вывод ссылки на пользовательское соглашение из формы авторизации """
        return self.find_element(AuthPageLocators.AGREEMENT_LINK, time=10)

    def social_providers(self):
        """ Вывод блока ссылок на социальные сети """
        return self.find_element(AuthPageLocators.SOCIAL_PROVIDERS, time=10)

    def vk_link(self):
        """ Вывод ссылки на ВКонтакте """
        return self.find_element(AuthPageLocators.VK_LINK, time=10)

    def yandex_link(self):
        """ Вывод ссылки на Яндекс """
        return self.find_element(AuthPageLocators.YANDEX_LINK, time=10)

    def ok_link(self):
        """ Вывод ссылки на Одноклассники """
        return self.find_element(AuthPageLocators.OK_LINK, time=10)

    def mail_link(self):
        """ Вывод ссылки на Mail.ru """
        return self.find_element(AuthPageLocators.MAIL_LINK, time=10)

    def google_link(self):
        """ Вывод ссылки на Google """
        return self.find_element(AuthPageLocators.GOOGLE_LINK, time=10)

    def register_link(self):
        """ Вывод ссылки на форму регистрации """
        return self.find_element(AuthPageLocators.REGISTER_LINK, time=10)

    def mask_phone_input(self):
        """ Вывод маски номера телефона в поле ввода номера телефона """
        return self.find_element(AuthPageLocators.USERNAME_TEXT_INPUT, time=2).get_attribute("value")

    def captcha_img(self):
        """ Вывод капчи """
        return self.find_element(AuthPageLocators.CAPTCHA_IMG, time=10)
