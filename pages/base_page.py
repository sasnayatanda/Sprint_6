from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_locators import BaseLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(BaseLocators.BASE_URL)
        self.accept_cookies()
        
    def accept_cookies(self):
        try:
            cookie_button = self.wait.until(
                EC.element_to_be_clickable(BaseLocators.COOKIE_BANNER)
            )
            cookie_button.click()
        except:
            pass