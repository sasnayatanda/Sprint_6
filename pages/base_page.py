from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть URL '{url}'")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Кликнуть по элементу")
    def click_element(self, element):
        self.wait.until(EC.element_to_be_clickable(element))
        element.click()

    @allure.step("Найти видимый элемент (by={by}, value={value})")
    def find_visible_element(self, by, value):
        return self.wait.until(EC.visibility_of_element_located((by, value)))

    @allure.step("Ввести текст '{text}' в элемент")
    def send_keys_to_element(self, element, text):
        element.clear()
        element.send_keys(text)

    @allure.step("Найти все элементы (by={by}, value={value})")
    def find_all_elements(self, by, value):
        return self.wait.until(EC.presence_of_all_elements_located((by, value)))
    
    @allure.step("Проскроллить страницу до элемента")
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Пролистать страницу на {x}px по X и {y}px по Y")
    def scroll_by(self, x, y):
        self.driver.execute_script(f"window.scrollBy({x}, {y});")
    
    @allure.step("Получить текст элемента")
    def get_element_text(self, element):
        return element.text
    
    @allure.step("Выбрать из списка элемент с текстом '{text}'")
    def select_from_list_by_text(self, elements, text):
        for element in elements:
            if text in element.text:
                self.click_element(element)
                return
        raise ValueError(f"Option with text '{text}' not found")

    @allure.step("Кликнуть по элементу с индексом {index} из списка")
    def click_element_by_index(self, elements, index):
        if 0 <= index < len(elements):
            self.click_element(elements[index])
        else:
            raise IndexError(f"Index {index} out of range")

    @allure.step("Нажать клавишу ESC")
    def press_escape_key(self):
        body = self.find_visible_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.ESCAPE)

    @allure.step("Получить хэндл текущего окна")
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        current = self.get_current_window_handle()
        new_window = [w for w in self.driver.window_handles if w != current][0]
        self.driver.switch_to.window(new_window)
        return new_window

    @allure.step("Переключиться на окно с хэндлом {handle}")
    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)

    @allure.step("Закрыть текущее окно")
    def close_current_window(self):
        self.driver.close()

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Дождаться URL '{url}'")
    def wait_for_url(self, url):
        self.wait.until(EC.url_to_be(url))
        return self.get_current_url() == url