import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver =  webdriver.Chrome("C:/Users/ramya/PycharmProjects/nopcommerceApp/Drivers/chromedriver.exe")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=r'C:/Users/ramya/PycharmProjects/nopcommerceApp/Driver/geckodriver.exe')
    else:
        driver = webdriver.edge("C:/Users/ramya/1PycharmProjects/nopcommerceApp/Drivers/msedgedriver.exe")
    return driver


def pytest_addoption(parser):
        parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# It is a hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nopcommerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Ramya'


# It is a hook for delete/modify environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
