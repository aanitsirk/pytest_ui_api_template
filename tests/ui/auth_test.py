import allure
from pages.AuthPage import AuthPage
from pages.MainPage import MainPage


def test_auth(browser):
    auth_page = AuthPage(browser)
    email = 'k.ovsyannikova2702@gmail.com'
    password = 'SkyPro114.2'

    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    company_name = main_page.get_my_company_name()

    current_url = main_page.get_current_url()
    with allure.step("Проверить, что URL "
                     + current_url + " заканчивается на team/"):
        assert current_url.endswith("team/")

    with allure.step("Проверить название компании"):
        assert company_name == 'QA 114.2'
