import pytest
import allure
from data.faq_data import FAQ_EXPECTED_DATA
from pages.main_page import MainPage

@allure.feature("Раздел 'Вопросы о важном'")
class TestFAQ:
    @allure.title("Проверка текстов вопросов и ответов")
    @pytest.mark.parametrize("question_id", FAQ_EXPECTED_DATA.keys())
    def test_question_answer(self, browser, question_id):
        main_page = MainPage(browser)
        expected_data = FAQ_EXPECTED_DATA[question_id]
        
        with allure.step(f"Открыть главную страницу"):
            main_page.open()
            main_page.accept_cookies()
        
        with allure.step(f"Пролистать к вопросу №{question_id}"):
            main_page.scroll_to_question(question_id)
            
        with allure.step(f"Нажать на вопрос №{question_id}"):
            main_page.click_question(question_id)
            
        with allure.step("Проверить текст вопроса"):
            actual_question = main_page.get_question_text(question_id)
            assert actual_question == expected_data['question'], \
                f"Текст вопроса не совпадает. Ожидалось: {expected_data['question']}, Фактически: {actual_question}"
            
        with allure.step("Проверить текст ответа"):
            actual_answer = main_page.get_answer_text(question_id)
            assert actual_answer == expected_data['answer'], \
                f"Текст ответа не совпадает. Ожидалось: {expected_data['answer']}, Фактически: {actual_answer}"
            
        allure.attach(
            f"Вопрос: {actual_question}\nОтвет: {actual_answer}",
            name=f"Вопрос №{question_id}",
            attachment_type=allure.attachment_type.TEXT
        )