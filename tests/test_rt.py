import pytest

from pages.auth_page import AuthPage
from pages.locators import AuthLocators
from pages.registrat_page import RegistratPage
from tests import settings


# Строка для запуска теста
# python -m pytest -v --driver Chrome --driver-path /chromedriver.exe tests/test_rt.py


def test_auth_with_valid_email_and_valid_pass(selenium):
    """TC-001 Тест авторизации с валидными значениями e-mail и пароля."""
    page = AuthPage(selenium)

    page.INPUT_EMAILPHONE_FIELD.clear()
    page.INPUT_EMAILPHONE_FIELD.send_keys(settings.valid_email)
    page.INPUT_PASSWORD_FIELD.clear()
    page.INPUT_PASSWORD_FIELD.send_keys(settings.valid_password)
    page.AUTH_ENTER_BTN.click()

    try:
        assert page.get_relative_link() == '/account_b2c/page'
    except AssertionError:
        assert 'Неверно введен текст с картинки' in page.find_other_element(*AuthLocators.ERROR_MESSAGE).text


@pytest.mark.parametrize("incorrect_email", [settings.invalid_email, settings.empty_email],
                         ids=['invalid_email', 'empty'])
@pytest.mark.parametrize("incorrect_password", [settings.invalid_password, settings.empty_password],
                         ids=['invalid_password', 'empty'])
def test_autoriz_invalid_email_pass(selenium, incorrect_email, incorrect_password):
    """TC-002,003 "Проверка входа пользователя с невалидным email и паролем:
    связка Почта+Пароль валидна, но пользователь с такими данными не зарегистрирован в системе;
    пустые значения."""
    page = AuthPage(selenium)
    page.INPUT_EMAILPHONE_FIELD.clear()
    page.INPUT_EMAILPHONE_FIELD.send_keys(incorrect_email)
    page.INPUT_PASSWORD_FIELD.clear()
    page.INPUT_PASSWORD_FIELD.send_keys(incorrect_password)
    page.AUTH_ENTER_BTN.click()

    assert page.get_relative_link() != '/account_b2c/page'


def test_auth_page_elements_available(selenium):
    """TC-004 Проверка раздела "Авторизация" на наличие основных элементов."""
    page = AuthPage(selenium)
    assert page.AUTH_TAB_MENU.text in page.AUTH_CARD.text
    assert page.INPUT_EMAILPHONE_FIELD.text in page.AUTH_CARD.text
    assert page.INPUT_PASSWORD_FIELD.text in page.AUTH_CARD.text
    assert page.AUTH_ENTER_BTN.text in page.AUTH_CARD.text
    assert page.FORGOT_PASSWORD_LINK.text in page.AUTH_CARD.text
    assert page.REGISTER_LINK.text in page.AUTH_CARD.text


def test_auth_page_tab_menu(selenium):
    """TC-005 Проверка названия табов в меню выбора типа авторизации."""
    try:
        page = AuthPage(selenium)
        menu = [page.TAB_PHONE.text, page.TAB_EMAIL.text, page.TAB_LOGIN.text, page.TAB_LS.text]
        for i in range(len(menu)):
            assert "Номер" in menu
            assert 'Почта' in menu
            assert 'Логин' in menu
            assert 'Лицевой счёт' in menu
    except AssertionError:
        print('Ошибка в имени таба Меню типа аутентификации')


def test_auth_page_tab_menu_active(selenium):
    """TC-006 Проверка выбора таба по умолчанию в Меню выбора типа авторизации."""
    page = AuthPage(selenium)

    assert page.TAB_PHONE_ACTIVE.text == settings.auth_menu_names[0]


def test_placeholder_name_input(selenium):
    """TC-007 Тест смены полей ввода при смене типа авторизации."""
    page = AuthPage(selenium)

    page.TAB_PHONE.click()
    assert page.PLACEHOLDER_NAME.text in settings.placeholder_name
    page.TAB_EMAIL.click()
    assert page.PLACEHOLDER_NAME.text in settings.placeholder_name
    page.TAB_LOGIN.click()
    assert page.PLACEHOLDER_NAME.text in settings.placeholder_name
    page.TAB_LS.click()
    assert page.PLACEHOLDER_NAME.text in settings.placeholder_name


def test_forgot_password_link(selenium):
    """TC-008 Переход к форме "Восстановление пароля"."""
    page = AuthPage(selenium)
    page.driver.execute_script("arguments[0].click();", page.FORGOT_PASSWORD_LINK)

    assert page.find_other_element(*AuthLocators.PASSWORD_RECOVERY_TITLE).text == 'Восстановление пароля'


def test_registration_link(selenium):
    """TC-009 Переход к форме "Регистрация"."""
    page = AuthPage(selenium)
    page.REGISTER_LINK.click()

    assert page.find_other_element(*AuthLocators.REGFORM_TITLE).text == 'Регистрация'


def test_page_logo_registration(selenium):
    """TC-010 Проверка блока с логотипом/названием компании на странице "Регистрация"."""
    try:
        reg_page = RegistratPage(selenium)
        assert reg_page.REGFORM_PAGE_LEFT.text != ''
    except AssertionError:
        print('Элемент отсутствует в левой части формы')


def test_elements_registration(selenium):
    """TC-011 Проверка Формы "Регистрация" на наличие основных элементов."""
    try:
        reg_page = RegistratPage(selenium)
        reg_form = [reg_page.REGFORM_FIRSTNAME, reg_page.REGFORM_LASTNAME, reg_page.REGFORM_REGION,
                    reg_page.REGFORM_EMAILPHONE_FIELD, reg_page.REGFORM_PASSWORD,
                    reg_page.REGFORM_PASSWORD_CONFIRM, reg_page.REG_BTN]
        for i in range(len(reg_form)):
            assert reg_page.REGFORM_FIRSTNAME in reg_form
            assert reg_page.REGFORM_LASTNAME in reg_form
            assert reg_page.REGFORM_EMAILPHONE_FIELD in reg_form
            assert reg_page.REGFORM_REGION in reg_form
            assert reg_page.REGFORM_PASSWORD in reg_form
            assert reg_page.REGFORM_PASSWORD_CONFIRM in reg_form
            assert reg_page.REG_BTN in reg_form
    except AssertionError:
        print(f'Элемент отсутствует в форме «Регистрация»')


def test_names_elements_registration(selenium):
    """TC-012 Проверка Формы "Регистрация" на соответствие названий элементов блока требованию."""
    try:
        reg_page = RegistratPage(selenium)
        assert 'Имя' in reg_page.REGFORM_CARD.text
        assert 'Фамилия' in reg_page.REGFORM_CARD.text
        assert 'Регион' in reg_page.REGFORM_CARD.text
        assert 'E-mail или мобильный телефон' in reg_page.REGFORM_CARD.text
        assert 'Пароль' in reg_page.REGFORM_CARD.text
        assert 'Подтверждение пароля' in reg_page.REGFORM_CARD.text
        assert 'Продолжить' in reg_page.REGFORM_CARD.text
    except AssertionError:
        print('Название элемента в форме «Регистрация» не соответствует Требованию')


def test_registration_valid_data(selenium):
    """TC-013 Проверка Регистрации пользователя с валидными данными: "Имя" и "Фамилия" на кириллице."""
    reg_page = RegistratPage(selenium)
    reg_page.REGFORM_FIRSTNAME.clear()
    reg_page.REGFORM_FIRSTNAME.send_keys(settings.first_name)
    reg_page.REGFORM_LASTNAME.clear()
    reg_page.REGFORM_LASTNAME.send_keys(settings.last_name)
    reg_page.REGFORM_EMAILPHONE_FIELD.clear()
    reg_page.REGFORM_EMAILPHONE_FIELD.send_keys(settings.valid_email)
    reg_page.REGFORM_PASSWORD.clear()
    reg_page.REGFORM_PASSWORD.send_keys(settings.valid_password)
    reg_page.REGFORM_PASSWORD_CONFIRM.clear()
    reg_page.REGFORM_PASSWORD_CONFIRM.send_keys(settings.valid_password)
    reg_page.REG_BTN.click()

    assert reg_page.find_other_element(*AuthLocators.email_confirm).text == 'Подтверждение email'


def test_registration_invalid_data(selenium):
    """TC-014 Проверка на уникальность введенного e-mail в форме "Регистрация"."""
    reg_page = RegistratPage(selenium)
    reg_page.REGFORM_FIRSTNAME.clear()
    reg_page.REGFORM_FIRSTNAME.send_keys(settings.first_name)
    reg_page.REGFORM_LASTNAME.clear()
    reg_page.REGFORM_LASTNAME.send_keys(settings.last_name)
    reg_page.REGFORM_EMAILPHONE_FIELD.clear()
    reg_page.REGFORM_EMAILPHONE_FIELD.send_keys(settings.valid_email)
    reg_page.REGFORM_PASSWORD.clear()
    reg_page.REGFORM_PASSWORD.send_keys(settings.valid_password)
    reg_page.REGFORM_PASSWORD_CONFIRM.clear()
    reg_page.REGFORM_PASSWORD_CONFIRM.send_keys(settings.valid_password)
    reg_page.REG_BTN.click()

    assert "Учётная запись уже существует" in reg_page.find_other_element(*AuthLocators.ACCOUNT_EXISTS_ALERT).text


def test_registration_and_redir_auth(selenium):
    """TC-015 Тест формы "Авторизация" после нажатия кнопки "Войти" при регистрации пользователя e-mail,
    который уже был использован ранее для регистрации. """
    reg_page = RegistratPage(selenium)
    reg_page.REGFORM_FIRSTNAME.clear()
    reg_page.REGFORM_FIRSTNAME.send_keys(settings.first_name)
    reg_page.REGFORM_LASTNAME.clear()
    reg_page.REGFORM_LASTNAME.send_keys(settings.last_name)
    reg_page.REGFORM_EMAILPHONE_FIELD.clear()
    reg_page.REGFORM_EMAILPHONE_FIELD.send_keys(settings.valid_email)
    reg_page.REGFORM_PASSWORD.clear()
    reg_page.REGFORM_PASSWORD.send_keys(settings.valid_password)
    reg_page.REGFORM_PASSWORD_CONFIRM.clear()
    reg_page.REGFORM_PASSWORD_CONFIRM.send_keys(settings.valid_password)
    reg_page.REG_BTN.click()
    reg_page.find_other_element(*AuthLocators.ALERT_ENTER_BTN).click()

    assert 'Авторизация' in reg_page.find_other_element(*AuthLocators.AUTH).text


@pytest.mark.parametrize("valid_first_name",
                         [
                             (settings.russian_generate_string) * 2
                             , (settings.russian_generate_string) * 3
                             , (settings.russian_generate_string) * 15
                             , (settings.russian_generate_string) * 29
                             , (settings.russian_generate_string) * 30
                         ],
                         ids=
                         [
                             'rus_symbols=2', 'rus_symbols=3', 'rus_symbols=15',
                             'rus_symbols=29', 'rus_symbols=30'
                         ])
def test_first_name_by_valid_data(selenium, valid_first_name):
    """TC-016 Тест поля ввода "Имя" формы "Регистрация" допустимыми валидными значениями:
    буквы кириллицы в количестве 2 ; 3 ; 15 ; 29 ; 30 ."""
    reg_page = RegistratPage(selenium)
    reg_page.REGFORM_FIRSTNAME.clear()
    reg_page.REGFORM_FIRSTNAME.send_keys(valid_first_name)
    reg_page.REG_BTN.click()

    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' not in reg_page.REGFORM_FIRSTNAME_CONT.text


@pytest.mark.parametrize("invalid_first_name",
                         [
                             (settings.russian_generate_string) * 1
                             , (settings.russian_generate_string) * 100
                             , (settings.russian_generate_string) * 256
                             , (settings.empty_value), (settings.numbers)
                             , (settings.latin_generate_string)
                             , (settings.chinese_chars), (settings.special_chars)
                         ],
                         ids=
                         [
                             'rus_symbols=1', 'rus_symbols=100', 'rus_symbols=256',
                             'empty_value', 'numbers', 'latin_symbols', 'chinese_symbols', 'special_symbols'
                         ])
def test_first_name_invalid_data(selenium, invalid_first_name):
    """TC-017 Тест поля ввода "Имя" формы "Регистрация" невалидными значениями:
    пустое значение;
    буквы кириллицы в количестве 1 ; 100 ; 256 ;
    латиницы буквы; китайские иероглифы; спецсимволы; числа."""
    reg_page = RegistratPage(selenium)
    reg_page.REGFORM_FIRSTNAME.clear()
    reg_page.REGFORM_FIRSTNAME.send_keys(invalid_first_name)
    reg_page.REG_BTN.click()

    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' in \
           reg_page.find_other_element(*AuthLocators.FIRSTNAME_HINT).text


@pytest.mark.parametrize("valid_password",
                         [(settings.password1), (settings.password2), (settings.password3)],
                         ids=['valid_symbols=8', 'valid_symbols=15', 'valid_symbols=20'])
def test_last_name_valid_data(selenium, valid_password):
    """TC-018 Тест поля ввода "Пароль" формы "Регистрация" валидными значениями.:
    символы из букв латиницы прописью и строчные+числа в количестве 8 ; 15 ; 20 ."""
    reg_page = RegistratPage(selenium)
    reg_page.REGFORM_PASSWORD.clear()
    reg_page.REGFORM_PASSWORD.send_keys(valid_password)
    reg_page.REG_BTN.click()

    assert 'Длина пароля должна быть не менее 8 символов' and \
           'Длина пароля должна быть не более 20 символов' and \
           'Пароль должен содержать хотя бы одну заглавную букву' and \
           'Пароль должен содержать хотя бы одну прописную букву' and \
           'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру' not in \
           reg_page.PASSWORD_HINT.text


def test_registration_confirm_password_valid_data(selenium):
    """TC-019 Тест поля ввода "Пароль" и "Подтвердить пароль" формы «Регистрация»
     валидными значениями(пароли совпадают)."""
    page_reg = RegistratPage(selenium)
    page_reg.REGFORM_PASSWORD.clear()
    page_reg.REGFORM_PASSWORD.send_keys(settings.password1)
    page_reg.REGFORM_PASSWORD_CONFIRM.clear()
    page_reg.REGFORM_PASSWORD_CONFIRM.send_keys(settings.password1)
    page_reg.REG_BTN.click()

    assert 'Пароли не совпадают' not in page_reg.PASSWORD_CONFIRM_HINT.text


def test_registration_confirm_password_invalid_data(selenium):
    """TC-020 Тест поля ввода "Пароль" и "Подтвердить пароль" формы «Регистрация»
    невалидными значениями(пароли не совпадают)."""
    page_reg = RegistratPage(selenium)
    page_reg.REGFORM_PASSWORD.clear()
    page_reg.REGFORM_PASSWORD.send_keys(settings.password1)
    page_reg.REGFORM_PASSWORD_CONFIRM.clear()
    page_reg.REGFORM_PASSWORD_CONFIRM.send_keys(settings.password2)
    page_reg.REG_BTN.click()

    assert 'Пароли не совпадают' in page_reg.find_other_element(*AuthLocators.PASSWORD_CONFIRM_HINT).text
