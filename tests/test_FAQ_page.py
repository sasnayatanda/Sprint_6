import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_locators import BaseLocators
from pages.FAQ_page import FAQPAGE

@allure.feature("FAQ Section")
class TestFAQ:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.faq_page = FAQPAGE(driver)
        with allure.step("Открываем главную страницу"):
            driver.get(BaseLocators.BASE_URL)
        with allure.step("Прокручиваем к разделу FAQ"):
            faq_header = self.faq_page._wait_for_element(FAQPageLocators.FAQ_HEADER)
            driver.execute_script("arguments[0].scrollIntoView();", faq_header)

    @pytest.mark.parametrize("question_locator, expected_text", [
        (FAQPageLocators.QUESTION_1_COST, "Сколько это стоит? И как оплатить?"),
        (FAQPageLocators.QUESTION_2_MULTIPLE_SCOOTERS, "Хочу сразу несколько самокатов! Так можно?"),
        (FAQPageLocators.QUESTION_3_RENT_TIME, "Как рассчитывается время аренды?"),
        (FAQPageLocators.QUESTION_4_TODAY_ORDER, "Можно ли заказать самокат прямо на сегодня?"),
        (FAQPageLocators.QUESTION_5_EXTEND_ORDER, "Можно ли продлить заказ или вернуть самокат раньше?"),
        (FAQPageLocators.QUESTION_6_CHARGER, "Вы привозите зарядку вместе с самокатом?"),
        (FAQPageLocators.QUESTION_7_CANCEL_ORDER, "Можно ли отменить заказ?"),
        (FAQPageLocators.QUESTION_8_OUTSIDE_MKAD, "Я живу за МКАДом, привезёте?")
    ], ids=[
        "Cost question", "Multiple scooters", "Rent time", 
        "Today order", "Extend order", "Charger", 
        "Cancel order", "Outside MKAD"
    ])
    @allure.title("Проверка текста вопроса: {expected_text}")
    def test_question_text(self, question_locator, expected_text):
        actual_text = self.faq_page.get_question_text(question_locator)
        assert actual_text == expected_text, f"Текст вопроса не совпадает. Ожидалось: {expected_text}, Фактически: {actual_text}"

    @pytest.mark.parametrize("question_locator, answer_index, expected_keywords", [
        (FAQPageLocators.QUESTION_1_COST, 0, ["400 рублей", "Оплата курьеру"]),
        (FAQPageLocators.QUESTION_2_MULTIPLE_SCOOTERS, 1, ["один заказ — один самокат"]),
        (FAQPageLocators.QUESTION_3_RENT_TIME, 2, ["Допустим, вы оформляете заказ", "Отсчёт времени аренды"]),
        (FAQPageLocators.QUESTION_4_TODAY_ORDER, 3, ["Только начиная с завтрашнего дня"]),
        (FAQPageLocators.QUESTION_5_EXTEND_ORDER, 4, ["позвонить в поддержку"]),
        (FAQPageLocators.QUESTION_6_CHARGER, 5, ["с полной зарядкой", "восемь суток"]),
        (FAQPageLocators.QUESTION_7_CANCEL_ORDER, 6, ["пока самокат не привезли"]),
        (FAQPageLocators.QUESTION_8_OUTSIDE_MKAD, 7, ["Московской области"])
    ])
    @allure.title("Проверка ответа на вопрос {question_locator}")
    def test_answer_content(self, question_locator, answer_index, expected_keywords):
        with allure.step(f"Кликаем на вопрос {question_locator}"):
            self.faq_page.click_question(question_locator)
        
        with allure.step("Проверяем видимость ответа"):
            answer = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(FAQPageLocators.answer_panel(answer_index))
            )
            assert answer.is_displayed(), "Ответ не отобразился"
        
        with allure.step("Проверяем содержание ответа"):
            answer_text = answer.text
            for keyword in expected_keywords:
                assert keyword in answer_text, f"Ключевое слово '{keyword}' не найдено в ответе"