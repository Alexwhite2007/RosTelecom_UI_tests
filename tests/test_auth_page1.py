import pytest
from auth_page import AuthPageHelper
from forgot_pass_page import ForgPassPageHelper
from register_page import RegisterPageHelper
from user_page import UserPagesHelper
from settings import *


# позитивные тесты на авторизацию
@pytest.mark.parametrize("username, password",
                         [(PHONE, PASSWORD), (EMAIL, PASSWORD), (LOGIN, PASSWORD)])
def test_auth_login(browser, username, password):
    # инициализируем страницу авторизации
    rt_auth_page = AuthPageHelper(browser)
    # инициализируем страницу авторизованного пользователя
    rt_user_page = UserPagesHelper(browser)
    # заходим на сайт
    rt_auth_page.go_to_site()
    # вводим юзернайм
    rt_auth_page.enter_username(username)
    # вводим пароль
    rt_auth_page.enter_password(password)
    # нажимаем войти
    rt_auth_page.click_enter()
    # нажимаем выйти
    rt_user_page.click_exit()


# переключение режимов ввода username меняет надпись в поле ввода
@pytest.mark.parametrize("mode, message", [(AuthPageHelper.click_tab_email, 'Электронная почта'),
                                           (AuthPageHelper.click_tab_login, 'Логин'),
                                           (AuthPageHelper.click_tab_ls, 'Лицевой счёт'),
                                           (AuthPageHelper.click_tab_phone, "Мобильный телефон")])
def test_auth_tabs(browser, mode, message):
    # инициализируем страницу авторизации
    auth_page = AuthPageHelper(browser)
    # заходим на сайт
    auth_page.go_to_page()
    # проверяем надпись в поле ввода
    mode(auth_page)
    assert message == auth_page.text_username().text


# наличие и функционирование кнопок авторизации через соцсети
'''БАГ авторизация с помощью яндекс открывается только через дабл-клик по кнопке'''


@pytest.mark.parametrize("network, url",
                         [(AuthPageHelper.click_VK, 'vk.com'), (AuthPageHelper.click_Ok, 'connect.ok.ru'),
                          (AuthPageHelper.click_Google, 'google.com'), (AuthPageHelper.click_Mail, 'mail.ru'),
                          (AuthPageHelper.click_Ya, 'yandex.ru')])
def test_auth_network_button(browser, network, url):
    # инициализируем страницу авторизации
    rt_auth_page = AuthPageHelper(browser)
    # заходим на сайт
    rt_auth_page.go_to_site()
    # нажимаем на значек соцсети
    network(self=rt_auth_page)
    # проверяем переход на страницу соцсети по url
    assert url in browser.current_url


# Страница Регистрация error сообщения на пустые поля
def test_reg_error_messages(browser):
    rt_auth_page = AuthPageHelper(browser)
    rt_auth_page.go_to_site()
    # нажимаем Зарегистрироваться
    rt_auth_page.click_register()
    # инициализируем страницу регистрации
    rt_reg_page = RegisterPageHelper(browser)
    # нажимаем Зарегистрироваться
    rt_reg_page.click_register()
    # считаем всплывшие сообщения
    messages = rt_reg_page.text_error_messages()
    # проверяем, что для каждого незаполненного поля есть сообщение
    print(messages[2].text, '**')
    assert len(messages) == 5


# Страница Регистрация проверка поля Подтверждение пароля
def test_reg_pass_confirm(browser):
    rt_auth_page = AuthPageHelper(browser)
    rt_auth_page.go_to_site()
    rt_auth_page.click_register()
    rt_reg_page = RegisterPageHelper(browser)
    # ввести  qwErtyui123    в     поле    Пароль
    rt_reg_page.enter_password('qwErtyui123')
    # ввести    qwErtyui321    в    поле    Подтверждение пароля
    rt_reg_page.enter_pass_confirm('qwErtyui321')
    # нажать    Зарегистрироваться
    rt_reg_page.click_register()
    # появилось    сообщение    "Пароли не совпадают"
    messages = rt_reg_page.text_error_messages()
    assert messages[-1].text == 'Пароли не совпадают'
    # ввести    qwErtyui123    в    поле    Подтверждение пароля
    rt_reg_page.enter_pass_confirm('qwErtyui123')
    # нажать    Зарегистрироваться
    rt_reg_page.click_register()
    # Предупреждающих    сообщений    относительно    пароля    нет
    messages = rt_reg_page.text_error_messages()
    assert messages[-1].text != 'Пароли не совпадают'


# Страница Регистрация ввод пароля, проверка парольной политики
@pytest.mark.parametrize("mess_one, mess_two",
                         [('qwertyui', 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру'),
                          ('qwertyui123', 'Пароль должен содержать хотя бы одну заглавную букву'),
                          ('ы', 'Длина пароля должна быть не менее 8 символов'),
                          ('ыыыыыыыыыыыыыыыыыыыыы', "Длина пароля должна быть не более 20 символов"),
                          ('ыыыыыыыы', 'Пароль должен содержать только латинские буквы')])
def test_reg_password_logic(browser, mess_one, mess_two):
    rt_auth_page = AuthPageHelper(browser)
    rt_auth_page.go_to_site()
    rt_auth_page.click_register()
    rt_reg_page = RegisterPageHelper(browser)
    # ввести qwertyui в поле Пароль
    rt_reg_page.enter_password(mess_one)
    # поставить курсор в любое другое поле
    rt_reg_page.enter_pass_confirm(' ')
    messages = rt_reg_page.text_error_messages()
    assert messages[-1].text == mess_two


# Страница Регистрация ввод НЕ валидного телефона и email
@pytest.mark.parametrize("mess_one, mess_two", [('example.email.ru',
                                                 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'),
                                                ('example@email',
                                                 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'),
                                                ('+1234567890',
                                                 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'),
                                                ('+375qwertyui',
                                                 "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"),
                                                ('ыыыыыыыы',
                                                 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru')])
def test_reg_username_invalid(browser, mess_one, mess_two):
    rt_auth_page = AuthPageHelper(browser)
    rt_auth_page.go_to_site()
    rt_auth_page.click_register()
    rt_reg_page = RegisterPageHelper(browser)
    # ввести любое НЕ валидное значение в поле E-mail или мобильный телефон
    rt_reg_page.enter_phone_email(mess_one)
    # поставить курсор в любое другое поле
    rt_reg_page.enter_pass_confirm(' ')
    messages = rt_reg_page.text_error_messages()
    assert messages[-1].text == mess_two


# Страница Регистрация ввод латиницей в поля Имя и Фамилия
@pytest.mark.parametrize("mess_one, ex", [('value', 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'),
                                          ('VALUE', 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'),
                                          ('v', 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'),
                                          ('vvvvvvvvvvvvvvvvvvvvv',
                                           "Необходимо заполнить поле кириллицей. От 2 до 30 символов."),
                                          (' " ', 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.')])
def test_reg_name_lastname_invalid(browser, mess_one, ex):
    rt_auth_page = AuthPageHelper(browser)
    rt_auth_page.go_to_site()
    rt_auth_page.click_register()
    rt_reg_page = RegisterPageHelper(browser)
    #  ввести латиницей любое значение в поле Имя
    rt_reg_page.enter_name(mess_one)
    # ввести латиницей любое значение в поле Фамилия
    rt_reg_page.enter_lastname(mess_one)
    # поставить курсор в любое другое поле
    rt_reg_page.enter_pass_confirm(' ')
    # проверяем error сообщения
    messages = rt_reg_page.text_error_messages()
    assert messages[-1].text == ex
    assert messages[-2].text == ex


# Страница Восстановление пароля error-message
def test_forgot_error_messages(browser):
    rt_auth_page = AuthPageHelper(browser)
    rt_auth_page.go_to_site()
    # нажать кнопку Забыл пароль
    rt_auth_page.click_forgot_pass()
    # инициализируем страницу Восстановления пароля
    rt_forg_pass_page = ForgPassPageHelper(browser)
    # ввести ЛЮБОЙ Номер телефона
    rt_forg_pass_page.enter_username("+71234568790")
    # ввести ЛЮБУЮ капчу отличную от картинки
    rt_forg_pass_page.enter_captcha('123')
    # нажать Продолжить
    rt_forg_pass_page.click_enter()
    # появляется сообщение "Неверный логин или текст с картинки"
    assert 'Неверный логин или текст с картинки' == rt_forg_pass_page.text_error_messages().text


# После 3х неудачных попыток войти появляется капча
@pytest.mark.parametrize("phone, password, value", [(PHONE, PASSWORD_PHONE, UserPagesHelper.click_exit),
                                                    ('☺☻♥♦♣♠•◘', PASSWORD_PHONE, None),
                                                    ('№;"?@%', PASSWORD_EMAIL, None),
                                                    ('صسغذئآ', PASSWORD_LOGIN, AuthPageHelper.img_captcha)])
def test_auth_login_invalid(browser, phone, password, value):
    # инициализируем страницу авторизации
    rt_auth_page = AuthPageHelper(browser)
    rt_user_page = UserPagesHelper(browser)
    # заходим на сайт
    rt_auth_page.go_to_site()
    # вводим юзернайм
    rt_auth_page.enter_username(phone)
    # вводим пароль
    rt_auth_page.enter_password(password)
    # нажимаем войти
    rt_auth_page.click_enter()
    # вводим не валидные данные 3 раза
    if value == AuthPageHelper.img_captcha:
        # проверяем капчу на странице
        assert value(rt_auth_page)
    # сбрасываем счетчик ошибок вхождения в лк валидными данными
    elif value == UserPagesHelper.click_exit:
        # выходим из лк
        value(rt_user_page)
    elif value == None:
        pass
