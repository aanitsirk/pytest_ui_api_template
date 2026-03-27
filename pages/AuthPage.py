import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from configuration.ConfigProvider import ConfigProvider

class AuthPage:
    def __init__(self, driver: WebDriver) -> None:
        url = ConfigProvider().get('ui', 'base_url')
        self.__url = url
        # __ чтобы скрыть элементы от внешнего мира
        self.__driver = driver

    @allure.step("Перейти на страницу авторизации")
    def go(self):
        self.__driver.get(self.__url)

    @allure.step("Авторизоваться под {email}:{password}")
    def login_as(self, email: str, password: str):
        self.__driver.find_element(
            By.CSS_SELECTOR, '[type="email"]').send_keys(email)
        self.__driver.find_element(
            By.CSS_SELECTOR, '[type="password"]').send_keys(password)
        self.__driver.find_element(
            By.CSS_SELECTOR, '[role="button"]').click()

    def get_current_url(self):
        return self.__driver.current_url
