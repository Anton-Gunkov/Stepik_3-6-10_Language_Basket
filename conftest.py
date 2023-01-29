# Тут для Pytest хранятся общие для всех фикстуры.
# Если в поддиретории есть файл, тогда он для файлов только в этой поддиректории

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.firefox.options import Options as OptionsFirefox

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Choose browser: '--browser_name=chrome/firefox'")
    parser.addoption("--language", action="store", default=None,
                     help="Choose language: '--language=en/ru/es/ko/fr' etc.")                 
    
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser_name")
    user_language = request.config.getoption("--language")
    browser = None
    
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        chrome_options = OptionsChrome()
        #chrome_options.add_argument("--headless")
        chrome_options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
        #print(f"Current Lang = {user_language}")
        # отключение вывода служебного инфо
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        browser = webdriver.Chrome(options=chrome_options)
        
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        ff_options = OptionsFirefox()
        ff_options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=ff_options)
                 
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    
    yield browser
    print("\nquit browser..")
    browser.quit()

#-----