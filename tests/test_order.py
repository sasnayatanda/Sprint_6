import pytest
import allure
from data.order_data import OrderTestData
from pages.order_page import OrderPage

@allure.feature("Оформление заказа самоката")
class TestOrderScooter:
    @allure.title("Полный процесс заказа (кнопка: {top_button}, цвет: {color})")
    @pytest.mark.parametrize("top_button, color", [
        (True, "black"),
        (False, "grey")
    ])
    def test_complete_order_flow(self, browser, top_button, color):
        order_page = OrderPage(browser)
        
        # Шаг 1: Начало оформления
        with allure.step("Нажать кнопку 'Заказать'"):
            order_page.click_order_button(top=top_button)
            
        # Шаг 2: Заполнение контактных данных
        with allure.step("Заполнить данные пользователя"):
            order_page.fill_first_page(
                NAME=OrderTestData.NAME,
                LAST_NAME=OrderTestData.LAST_NAME,
                ADRESS=OrderTestData.ADDRESS,
                METRO_STATION=OrderTestData.METRO_STATION,
                PHONE=OrderTestData.PHONE
            )
            
        # Шаг 3: Заполнение данных аренды
        with allure.step("Заполнить данные аренды"):
            order_page.fill_second_page(
                date=OrderTestData.DATE,
                period_index=1,  # Сутки
                color=color,
                comment=OrderTestData.COMMENT
            )
            
        # Шаг 4: Подтверждение заказа
        with allure.step("Подтвердить заказ"):
            order_page.confirm_order()
            
        # Шаг 5: Проверка успешного оформления
        with allure.step("Проверить сообщение об успехе"):
            success_text = order_page.get_success_message()
            assert "Заказ оформлен" in success_text, \
                f"Не получено подтверждение заказа. Текст: {success_text}"
                
            allure.attach(
                success_text,
                name="Сообщение об успешном заказе",
                attachment_type=allure.attachment_type.TEXT
            )