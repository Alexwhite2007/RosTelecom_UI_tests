from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HeaderLocators:
    HEADER_ALL = (By.ID, "app-header")
    LOGO = (By.CLASS_NAME, "rt-footer-left")


class HeaderHelper(BasePage):
    def header(self):
        return self.find_element(HeaderLocators.HEADER_ALL, time=5)

    def header_logo(self):
        return self.find_element(HeaderLocators.LOGO, time=5)
