from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Абстрактный базовый класс для всех страниц"""
    
    def __init__(self, driver, base_url=None):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self._base_url = base_url

    def open(self):
        if not self._base_url:
            raise NotImplementedError("Дочерний класс должен определить base_url")
        self.driver.get(self._base_url)

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        return element

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))