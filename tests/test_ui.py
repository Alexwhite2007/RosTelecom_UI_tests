import pytest
from selenium.common.exceptions import TimeoutException

from pages.auth_page import AuthPageHelper
from pages.footer import FooterHelper
from pages.header import HeaderHelper
from pages.pass_recovery_page import PassRecoveryPageHelper
from pages.register_page import RegisterPageHelper
from .settings import *


@pytest.mark.auth
def test_auth_page_elements(browser):  # AUTH-1
    auth_page = AuthPageHelper(browser)
    footer = FooterHelper(browser)
    header = HeaderHelper(browser)
    auth_page.go_to_page()

    assert header.header().is_displayed()
    assert header.header_logo().is_displayed()

    assert footer.footer().is_displayed()
    assert footer.footer_info().is_displayed()
    assert footer.footer_phone().is_displayed()
    assert footer.footer_phone().text == '8 800 100 0 800', 'Некорректный номер телефона поддержки'

    left_width = auth_page.side_left_body().size['width']
    right_width = auth_page.side_right_body().size['width']
    assert left_width == right_width

    assert auth_page.side_left_body().is_displayed()
    assert auth_page.side_left_body().text == 'Личный кабинет\nПерсональный помощник в цифровом мире Ростелекома', \
        'Invalid text in left side'
    assert auth_page.body_logo().is_displayed()

    assert auth_page.side_right_body().is_displayed()
    assert auth_page.form_title().text == 'Авторизация', 'Форма авторизации не открылась'


@pytest.mark.auth
def test_footer_elements(browser):  # AUTH-2
    footer = FooterHelper(browser)
    footer.go_to_page()

    assert footer.footer().is_displayed()
    assert footer.footer_info().is_displayed()
    assert footer.footer_phone().is_displayed()
    assert footer.footer_phone().text == '8 800 100 0 800', 'Некорректный номер телефона поддержки'
    assert footer.footer_copyright().is_displayed()
    assert footer.footer_cookies().is_displayed()
    assert footer.footer_agreement().is_displayed()


@pytest.mark.auth
def test_auth_form_elements(browser):  # AUTH-3
    auth_page = AuthPageHelper(browser)
    auth_page.go_to_page()

    assert auth_page.auth_form().is_displayed()
    assert auth_page.form_title().text == 'Авторизация', 'Форма авторизации не открылась'
    assert auth_page.tabs_menu().is_displayed()
    assert auth_page.username_field().is_displayed()
    assert auth_page.password_field().is_displayed()
    assert auth_page.checkbox_remember_me().is_displayed()
    assert auth_page.forgot_password_link().is_displayed()
    assert auth_page.enter_button().is_displayed()
    assert auth_page.agreement_contract_link().is_displayed()
    assert auth_page.social_providers().is_displayed()
    assert auth_page.register_link().is_displayed()


@pytest.mark.auth
def test_tabs_menu_elements(browser):  # AUTH-4
    auth_page = AuthPageHelper(browser)
    auth_page.go_to_page()
    tabs = auth_page.tabs_menu().text
    assert tabs == AuthPageHelper.LIST_ELEMENTS


@pytest.mark.auth
def test_tabs_menu_input_fields(browser):  # AUTH-5
    auth_page = AuthPageHelper(browser)
    auth_page.go_to_page()
    assert auth_page.phone_input_field().is_displayed()

    auth_page.click_tab_menu_email()
    assert auth_page.email_input_field().is_displayed()

    auth_page.click_tab_menu_login()
    assert auth_page.login_input_field().is_displayed()

    auth_page.click_tab_menu_ls()
    assert auth_page.ls_input_field().is_displayed()


@pytest.mark.auth
def test_auto_change_tab(browser):  # AUTH-6
    auth_page = AuthPageHelper(browser)
    auth_page.go_to_page()
    auth_page.enter_username('mailbox@mailbox.ru')
    auth_page.submit()
    assert auth_page.email_input_field().is_displayed()

    auth_page.go_to_page()
    auth_page.enter_username('+79091111111')
    auth_page.submit()
    assert auth_page.phone_input_field().is_displayed()


@pytest.mark.auth
def test_wrong_phone_and_pass(browser):  # AUTH-7
    auth_page = AuthPageHelper(browser)
    auth_page.go_to_page()
    auth_page.enter_username('+79091111111')
    auth_page.enter_password('passWD123')
    auth_page.enter_button().click()

    assert auth_page.form_error_message().is_displayed()
    assert auth_page.forgot_password_link().is_displayed()


@pytest.mark.auth
def test_mask_phone(browser):  # AUTH-8
    auth_page = AuthPageHelper(browser)
    auth_page.go_to_page()
    auth_page.enter_username('9')
    assert auth_page.mask_phone_input() == '79'


@pytest.mark.auth
def test_forgot_password_link(browser):  # AUTH-9
    auth_page = AuthPageHelper(browser)
    pass_recovery_page = PassRecoveryPageHelper(browser)
    auth_page.go_to_page()
    auth_page.forgot_password_link().click()

    assert pass_recovery_page.form_title().text == 'Восстановление пароля'


@pytest.mark.auth
def test_agreement_contract_link(browser):  # AUTH-10
    auth_page = AuthPageHelper(browser)
    auth_page.go_to_page()
    auth_page.agreement_contract_link().click()
    browser.switch_to.window(browser.window_handles[1])
    assert auth_page.agreement_contract_page().is_displayed()


@pytest.mark.auth
def test_go_by_register_link(browser):  # AUTH-11
    auth_page = AuthPageHelper(browser)
    register_page = RegisterPageHelper(browser)
    auth_page.go_to_page()
    auth_page.register_link().click()

    assert register_page.form_title().text == 'Регистрация'


@pytest.mark.auth
def test_social_networks_links(browser):  # AUTH-12
    auth_page = AuthPageHelper(browser)
    auth_page.go_to_page()

    assert auth_page.vk_link().is_displayed()
    assert auth_page.yandex_link().is_displayed()
    assert auth_page.ok_link().is_displayed()
    assert auth_page.mail_link().is_displayed()
    assert auth_page.google_link().is_displayed()


@pytest.mark.register
def test_register_form_elements(browser):  # REG-1
    register_page = RegisterPageHelper(browser)
    RegisterPageHelper.go_to_register_page(browser)

    assert register_page.form_title().text == 'Регистрация'
    assert register_page.registration_form().is_displayed()
    assert register_page.firstname_field().is_displayed()
    assert register_page.lastname_field().is_displayed()
    assert register_page.region_dropdown().is_displayed()
    assert register_page.email_or_phone_field().is_displayed()
    assert register_page.password_field().is_displayed()
    assert register_page.password_confirm_field().is_displayed()
    assert register_page.register_btn().is_displayed()
    assert register_page.agreement_link().is_displayed()


@pytest.mark.register
def test_register_form_errors(browser):  # REG-2
    register_page = RegisterPageHelper(browser)
    RegisterPageHelper.go_to_register_page(browser)
    register_page.register_btn().click()

    assert register_page.count_error_messages() == 5


@pytest.mark.register
@pytest.mark.parametrize('name_value', valid_names, ids=valid_names_ids)
def test_firstname_validation_positive(browser, name_value):  # REG-3 - positive test
    if name_value is None:
        name_value = ''
    RegisterPageHelper.go_to_register_page(browser)
    register_page = RegisterPageHelper(browser)
    register_page.enter_firstname(name_value)
    register_page.submit()
    try:
        register_page.error_message()
        assert False, 'Ошибка валидации'
    except TimeoutException:
        assert True


@pytest.mark.register
@pytest.mark.parametrize('name_value', invalid_names, ids=invalid_names_ids)
def test_firstname_validation_negative(browser, name_value):  # REG-4 - negative test
    if name_value is None:
        name_value = ''
    RegisterPageHelper.go_to_register_page(browser)
    register_page = RegisterPageHelper(browser)
    register_page.enter_firstname(name_value)
    register_page.submit()
    try:
        register_page.error_message()
        assert True
    except TimeoutException:
        assert False, 'Ошибка валидации не отобразилась!'


@pytest.mark.register
@pytest.mark.parametrize('lastname', valid_names, ids=valid_names_ids)
def test_lastname_validation_positive(browser, lastname):  # REG-5 - positive test
    if lastname is None:
        lastname = ''
    RegisterPageHelper.go_to_register_page(browser)
    register_page = RegisterPageHelper(browser)
    register_page.enter_lastname(lastname)
    register_page.submit()
    try:
        register_page.error_message()
        assert False, 'Ошибка валидации'
    except TimeoutException:
        assert True


@pytest.mark.register
@pytest.mark.parametrize('lastname', invalid_names, ids=invalid_names_ids)
def test_lastname_validation_negative(browser, lastname):  # REG-6 - negative test
    if lastname is None:
        lastname = ''
    RegisterPageHelper.go_to_register_page(browser)
    register_page = RegisterPageHelper(browser)
    register_page.enter_lastname(lastname)
    register_page.submit()
    try:
        register_page.error_message()
        assert True
    except TimeoutException:
        assert False, 'Ошибка валидации не отобразилась!'


@pytest.mark.register
@pytest.mark.parametrize('password', valid_password, ids=valid_password_ids)
def test_password_validation_positive(browser, password):  # REG-7 - positive test
    if password is None:
        password = ''
    RegisterPageHelper.go_to_register_page(browser)
    register_page = RegisterPageHelper(browser)
    register_page.enter_password(password)
    # time.sleep(1)
    register_page.submit()
    try:
        register_page.error_message()
        assert False, 'Ошибка валидации'
    except TimeoutException:
        assert True


@pytest.mark.register
@pytest.mark.parametrize('password', invalid_password, ids=invalid_password_ids)
def test_password_validation_negative(browser, password):  # REG-8 - negative test
    if password is None:
        password = ''
    RegisterPageHelper.go_to_register_page(browser)
    register_page = RegisterPageHelper(browser)
    register_page.enter_password(password)
    register_page.submit()
    try:
        register_page.error_message()
        assert True
    except TimeoutException:
        assert False, 'Ошибка валидации не отобразилась!'


@pytest.mark.recovery
def test_recovery_form_elements(browser):  # RCVRY-1
    recovery_page = PassRecoveryPageHelper(browser)
    PassRecoveryPageHelper.go_to_pass_recovery_page(browser)

    assert recovery_page.form_title().text == 'Восстановление пароля'
    assert recovery_page.username_field().is_displayed()
    assert recovery_page.captcha_img().is_displayed()
    assert recovery_page.captcha_input_field().is_displayed()
    assert recovery_page.go_btn().is_displayed()
    assert recovery_page.go_back_link().is_displayed()
    assert recovery_page.tab_menu_phone().is_displayed()
    assert recovery_page.tab_menu_email().is_displayed()
    assert recovery_page.tab_menu_login().is_displayed()
    assert recovery_page.tab_menu_ls().is_displayed()
    assert recovery_page.agreement_link().is_displayed()


@pytest.mark.recovery
def test_recovery_form_error_message(browser):  # RCVRY-2
    recovery_page = PassRecoveryPageHelper(browser)
    recovery_page.go_to_pass_recovery_page(browser)
    recovery_page.enter_username("+79091111111")
    recovery_page.enter_captcha("123")
    recovery_page.click_go_btn()

    assert recovery_page.form_error_message().is_displayed()
    assert 'Неверный логин или текст с картинки' == recovery_page.form_error_message().text


@pytest.mark.recovery
def test_recovery_form_validation_error_message(browser):  # RCVRY-3
    recovery_page = PassRecoveryPageHelper(browser)
    recovery_page.go_to_pass_recovery_page(browser)
    recovery_page.enter_username("+7909111111")
    recovery_page.submit()
    assert recovery_page.validation_error_message().is_displayed()
    assert 'Неверный формат телефона' == recovery_page.validation_error_message().text
