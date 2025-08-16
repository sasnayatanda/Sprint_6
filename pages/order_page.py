from locators.order_locators import OrderLocators
from pages.base_page import BasePage
import allure


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.accept_cookies()  # Автоматически принимаем куки при инициализации страницы

    @allure.step("Принять cookies")
    def accept_cookies(self):
        try:
            cookie_btn = self.find_clickable_element(*OrderLocators.COOKIE_BUTTON, timeout=3)
            self.click_element(cookie_btn)
            allure.attach("Куки успешно приняты", name="Cookie Acceptance")
        except:
            allure.attach("Кнопка принятия куки не найдена или не требуется", name="Cookie Notice")
            pass

    @allure.step("Нажать на кнопку 'Заказать' (верхнюю/нижнюю)")
    def click_order_button(self, top=True):
        locator = OrderLocators.ORDER_BUTTON_TOP if top else OrderLocators.ORDER_BUTTON_BOTTOM
        element = self.find_visible_element(*locator)
        self.click_element(element)

    @allure.step("Заполнить первую страницу заказа")
    def fill_first_page(self, name, last_name, address, metro_station, phone):
        with allure.step(f"Ввести имя: {name}"):
            name_field = self.find_visible_element(*OrderLocators.NAME)
            self.send_keys_to_element(name_field, name)
    
        with allure.step(f"Ввести фамилию: {last_name}"):
            last_name_field = self.find_visible_element(*OrderLocators.LAST_NAME)
            self.send_keys_to_element(last_name_field, last_name)
    
        with allure.step(f"Ввести адрес: {address}"):
            address_field = self.find_visible_element(*OrderLocators.ADDRESS)
            self.send_keys_to_element(address_field, address)
    
        with allure.step(f"Выбрать станцию метро: {metro_station}"):
            self.click_element(*OrderLocators.METRO_STATION)
            stations = self.find_all_elements(*OrderLocators.METRO_OPTION)
            for station in stations:
                if metro_station in station.text:
                    station.click()
                    break
    
        with allure.step(f"Ввести телефон: {phone}"):
            phone_field = self.find_visible_element(*OrderLocators.PHONE)
            self.send_keys_to_element(phone_field, phone)
    
        with allure.step("Нажать кнопку 'Далее'"):
            next_btn = self.find_visible_element(*OrderLocators.NEXT_BUTTON)
            self.click_element(next_btn)

    @allure.step("Заполнить вторую страницу заказа")
    def fill_second_page(self, date, period_index, color, comment=""):
        with allure.step("Выбрать дату аренды"):
            date_field = self.find_visible_element(*OrderLocators.DATE)
            self.click_element(date_field)
            self.press_escape_key()
    
        with allure.step(f"Выбрать период аренды (индекс {period_index})"):
            period_field = self.find_visible_element(*OrderLocators.RENT_PERIOD)
            self.click_element(period_field)
        
            periods = self.find_all_elements(*OrderLocators.RENT_OPTIONS)
            self.click_element_by_index(periods, period_index)
    
        with allure.step(f"Выбрать цвет: {color}"):
            checkbox_locator = OrderLocators.BLACK_CHECKBOX if color == "black" else OrderLocators.GREY_CHECKBOX
            checkbox = self.find_visible_element(*checkbox_locator)
            self.click_element(checkbox)
    
        if comment:
            with allure.step(f"Добавить комментарий: {comment}"):
                comment_field = self.find_visible_element(*OrderLocators.COMMENT)
                self.send_keys_to_element(comment_field, comment)
    
        with allure.step("Подтвердить заказ"):
            order_btn = self.find_visible_element(*OrderLocators.ORDER_BUTTON)
            self.click_element(order_btn)
        
            confirm_btn = self.find_visible_element(*OrderLocators.CONFIRM_BUTTON)
            self.click_element(confirm_btn)
    
        with allure.step("Получить сообщение об успешном создании заказа"):
            success_msg = self.find_visible_element(*OrderLocators.SUCCESS_MESSAGE)
            return self.get_element_text(success_msg)

    @allure.step("Проверить переход по логотипу Самоката")
    def check_scooter_logo(self):
        with allure.step("Нажать на логотип Самоката"):
            logo = self.find_visible_element(*OrderLocators.SCOOTER_LOGO)
            self.click_element(logo)
    
        with allure.step("Дождаться перехода на главную страницу"):
            return self.wait_for_url("https://qa-scooter.praktikum-services.ru/")

    @allure.step("Проверить переход по логотипу Яндекса")
    def check_yandex_logo(self):
        with allure.step("Запомнить текущее окно браузера"):
            main_window = self.get_current_window_handle()
    
        with allure.step("Нажать на логотип Яндекса"):
            logo = self.find_visible_element(*OrderLocators.YANDEX_LOGO)
            self.click_element(logo)
    
        with allure.step("Переключиться на новое окно"):
            new_window = self.switch_to_new_window()
    
        with allure.step("Проверить URL в новом окне"):
            current_url = self.get_current_url()
            is_dzen = "dzen.ru" in current_url
    
        with allure.step("Закрыть новое окно и вернуться обратно"):
            self.close_current_window()
            self.switch_to_window(main_window)
    
        return is_dzen