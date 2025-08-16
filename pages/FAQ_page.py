from locators.faq_locators import FAQPageLocators
from locators.base_locators import BaseLocators
from pages.base_page import BasePage
import allure

class FAQPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открыть и инициализировать страницу (принять куки)")
    def open_and_initialize(self):
        self.open_url("https://qa-scooter.praktikum-services.ru/")
        self.scroll_to_faq()
        self.accept_cookies()

    @allure.step("Пролистать до раздела FAQ")
    def scroll_to_faq(self):
        header = self.find_visible_element(*FAQPageLocators.FAQ_HEADER)
        self.scroll_to_element(header)

    @allure.step("Принять куки, если отображается баннер")
    def accept_cookies(self):
        try:
            cookie_banner = self.find_visible_element(*BaseLocators.COOKIE_BANNER)
            self.click_element(cookie_banner)
        except:
            allure.attach("Cookie banner not found", name="Cookie acceptance")
            pass
    
    @allure.step("Получить текст вопроса {question_num}")
    def get_question_text(self, question_num):
        locator = getattr(FAQPageLocators, f"QUESTION_{question_num}")
        question_element = self.find_visible_element(*locator)
        return self.get_element_text(question_element)

    @allure.step("Получить текст ответа на вопрос {question_num}")
    def get_answer_text(self, question_num):
        self.click_question(question_num)
        panel_locator = FAQPageLocators.answer_panel(question_num-1)
        panel_element = self.find_visible_element(*panel_locator)
        return self.get_element_text(panel_element)

    @allure.step("Кликнуть по вопросу {question_num}")
    def click_question(self, question_num):
        locator = getattr(FAQPageLocators, f"QUESTION_{question_num}")
        question_element = self.find_visible_element(*locator)
        
        for attempt in range(3):
            try:
                self.click_element(question_element)
                return
            except Exception as e:
                if attempt == 2:
                    raise Exception(f"Failed to click question {question_num} after 3 attempts") from e
                self.scroll_by(0, 100)
                allure.attach(f"Attempt {attempt + 1}: Scrolled down and retrying", name="Retry click")