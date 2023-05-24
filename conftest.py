import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionChrome
from selenium.webdriver.edge.options import Options as OptionEdge
from selenium.webdriver.firefox.options import Options as OptionFirefox


def pytest_addoption(parser):
    parser.addoption('--browser_name', action ='store', default = 'chrome', help="Choose browser: chrome or edge or firefox")
    parser.addoption('--language', action = 'store', default = None)

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = OptionChrome()
        #options.add_argument("--incognito") # Запускает в инкогнито
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        options.add_experimental_option('excludeSwitches', ['enable-logging']) #Отключает ошибки devtool в логах
        browser = webdriver.Chrome(options=options)

    elif browser_name == "edge":
        print("\nstart edge browser for test..")
        options = OptionEdge()
        #options.add_argument("--incognito") # Запускает Edge в инкогнито
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        options.add_experimental_option('excludeSwitches', ['enable-logging']) #Отключает ошибки devtool в логах
        browser = webdriver.Edge(options=options)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = OptionFirefox()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or edge or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
