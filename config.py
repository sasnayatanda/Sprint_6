import pytest
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def order_page(driver):
    from pages.order_page import OrderPage
    page = OrderPage(driver)
    page.open_url("https://qa-scooter.praktikum-services.ru/")
    yield page

@pytest.fixture
def faq_page(driver):
    from pages.faq_page import FAQPage
    page = FAQPage(driver)
    page.open_and_initialize()
    yield page