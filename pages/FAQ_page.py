from selenium.webdriver.support import expected_conditions as EC
from locators.faq_locators import FAQPageLocators
from pages.base_page import BasePage
from config import Urls

class FAQPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, base_url=Urls.BASE)

    def open_and_initialize(self):
        self.open()
        self.scroll_to_faq()
        self.accept_cookies()

    def scroll_to_faq(self):
        header = self.find_element(FAQPageLocators.FAQ_HEADER)
        self.driver.execute_script("arguments[0].scrollIntoView();", header)

    def accept_cookies(self):
        try:
            self.click_element(FAQPageLocators.COOKIE_BANNER)
        except:
            pass

    def get_question_text(self, question_num):
        locator = getattr(FAQPageLocators, f"QUESTION_{question_num}")
        return self.find_element(locator).text

    def get_answer_text(self, question_num):
        self.click_question(question_num)
        panel_locator = FAQPageLocators.answer_panel(question_num-1)
        return self.find_element(panel_locator).text

    def click_question(self, question_num):
        locator = getattr(FAQPageLocators, f"QUESTION_{question_num}")
        for _ in range(3):
            try:
                return self.click_element(locator)
            except:
                self.driver.execute_script("window.scrollBy(0, 100);")
        raise Exception(f"Failed to click question {question_num}")

    def answer_contains_keywords(self, answer_text, keywords):
        lower_text = answer_text.lower()
        missing = [kw for kw in keywords if kw.lower() not in lower_text]
        if missing:
            raise AssertionError(f"Missing keywords: {', '.join(missing)}")
        return True