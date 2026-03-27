import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from configuration.ConfigProvider import ConfigProvider


class MainPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.url = ConfigProvider().get('ui', 'base_url')
        self.__url = self.url

    @allure.step('Получить текущий URL')
    def get_current_url(self) -> str:
        return self.__driver.current_url

    @allure.step('Получить название компании')
    def get_my_company_name(self) -> str:
        company_name = self.__driver.find_element(By.CSS_SELECTOR, '.mr-6.whitespace-nowrap.h1-semibold')
        return company_name.text
