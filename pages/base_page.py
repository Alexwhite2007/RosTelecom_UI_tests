from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """ Класс, содержащий базовые методы для проверки страницы """
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://b2c.passport.rt.ru/"

    def go_to_page(self):
        """ Открытие страницы """
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        """ Поиск элемента на странице """
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Not found {locator}')

    def find_elements(self, locator, time=10):
        """ Поиск элементов на странице """
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'Not found {locator}')

    def submit(self):
        """ Функция, запускающая валидацию в полях ввода, кликая в свободном месте страницы """
        return self.find_element((By.TAG_NAME, "body")).click()

    def agreement_contract_page(self):
        """ Вывод заголовка пользовательского соглашения """
        return self.find_element((By.CSS_SELECTOR, "h1[class='offer-title']"), time=5)
