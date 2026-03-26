from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__url = 'https://ru.yougile.com/team/'
        self.__driver = driver

    def get_current_url(self) -> str:
        return self.__driver.current_url

    def get_my_company_name(self) -> str:
        company_name = self.__driver.find_element(
            By.CSS_SELECTOR, '.mr-6.whitespace-nowrap.h1-semibold')
        return company_name.text
