from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FooterLocators:
    FOOTER_ALL = (By.ID, "app-footer")
    INFO = (By.CLASS_NAME, "rt-footer-left")
    PHONE = (By.XPATH, "//*[@id='app-footer']/div[2]/a")
    COPYRIGHT = (By.CSS_SELECTOR, "div[class *='copyright']")
    COOKIES = (By.CSS_SELECTOR, "span[class *='cookies']")
    AGREEMENT = (By.ID, "rt-footer-agreement-link")


class FooterHelper(BasePage):
    def footer(self):
        return self.find_element(FooterLocators.FOOTER_ALL, time=5)

    def footer_info(self):
        return self.find_element(FooterLocators.INFO, time=5)

    def footer_phone(self):
        return self.find_element(FooterLocators.PHONE, time=5)

    def footer_copyright(self):
        return self.find_element(FooterLocators.COPYRIGHT, time=5)

    def footer_cookies(self):
        return self.find_element(FooterLocators.COOKIES, time=5)

    def footer_agreement(self):
        return self.find_element(FooterLocators.AGREEMENT, time=5)
