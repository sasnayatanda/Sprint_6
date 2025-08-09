from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from locators.FAQLocators import FAQPageLocators


class FAQPAGE:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
    
    
    
    def get_question_text(self, question_locator):
        """Возвращает текст вопроса"""
        element = self._wait_for_element(question_locator)
        return element.text

    def click_question(self, question_locator):
        """Клик вопроса с повторными попытками"""
        for attempt in range(3):  # 3 попытки
            element = self.driver.find_element(*question_locator)
            try:
                element.click()
                return element.text
            except:
                self.driver.execute_script("window.scrollBy(0, 100)")
        return element.text  

    def get_answer_text(self, index):
        """Возвращает текст ответа по индексу"""
        locator = FAQPageLocators.answer_panel(index)
        element = self._wait_for_element(locator)
        return element.text
    
    def _wait_for_element(self, locator, timeout=None):
        
    # Базовое ожидание элемента с правильной обработкой исключений
    
        timeout = timeout or self.timeout
        end_time = time.time() + timeout
        last_exception = None
    
        while time.time() < end_time:
            try:
                element = self.driver.find_element(*locator)
                if element.is_displayed():
                    return element
            except Exception as e:
                last_exception = e
                time.sleep(0.5)
    
            raise TimeoutError(f"Element not found: {locator}. Last exception: {str(last_exception)}")
