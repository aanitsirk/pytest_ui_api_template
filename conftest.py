import pytest
import allure
from selenium import webdriver

from api.ProjectApi import ProjectApi
from configuration.ConfigProvider import ConfigProvider
from testdata.DataProvider import DataProvider


@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):

        timeout = ConfigProvider().getint('ui', 'timeout')

        browser = webdriver.Chrome()
        browser.implicitly_wait(timeout)
        browser.maximize_window()
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()


@pytest.fixture(scope="session")
def api_client():
    DataProvider().get_email()
    api = ProjectApi()
    login = DataProvider().get_email()
    password = 'SkyPro114.2'
    companyId = '4075d252-8e95-40f7-a3f0-08502c97e043'

    api.get_auth_token(login, password, companyId)
    return api


@pytest.fixture
def api_client_no_auth():
    api = ProjectApi()
    login = ''
    password = ''
    companyId = ''

    api.get_auth_token(login, password, companyId)
    return api


@pytest.fixture
def test_data():
    return DataProvider()