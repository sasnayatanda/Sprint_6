import pytest
from pages.order_page import OrderPage
import time
import allure
from pages.base_page import BasePage

@allure.feature("Order Section")
class TestOrder:   
    @allure.title("Проверка заказа самоката")
    def test_order_scooter(self, driver, top_button, period_index, color):
        order_page = OrderPage(driver)
        order_page.open()  # Здесь уже есть неявное ожидание в базовых методах
    
        # 1. Начало заказа (внутри уже есть ожидания)
        order_page.click_order_button(top=top_button)

        # 2. Заполнение первой страницы
        order_page.fill_first_page(
            name="Иван",
            last_name="Иванов",
            address="ул. Пушкина, 10",
            metro_station="Сокольники",
            phone="89991112233"
        )
    
        # 3. Заполнение второй страницы
        result = order_page.fill_second_page(
            date="12.12.2023",
            period_index=period_index,
            color=color,
            comment="Тестовый заказ"
        )
    
    # 4. Проверка результата
    assert "Заказ оформлен" in result
    
    @allure.title("Проверка клик по логотипу самоката")    
    def test_scooter_logo(self, driver):
        order_page = OrderPage(driver)
        order_page.open()
        
        result = order_page.check_scooter_logo()
        assert result, "Логотип Самоката не ведет на главную страницу"
    
    @allure.title("Проверка клик по логотипу Яндекс")    
    def test_yandex_logo(self, driver):
        order_page = OrderPage(driver)
        order_page.open()
        
        result = order_page.check_yandex_logo()
        assert result, "Логотип Яндекса не ведет на Дзен"