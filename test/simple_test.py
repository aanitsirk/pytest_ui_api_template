from pages.AuthPage import AuthPage
from pages.MainPage import MainPage


def test_auth(browser):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as('k.ovsyannikova2702@gmail.com', 'SkyPro114.2')

    main_page = MainPage(browser)
    company_name = main_page.get_my_company_name()

    assert company_name == 'QA 114.2'
