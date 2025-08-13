from locators.order_locators import OrderLocators
from pages.base_page import BasePage
from config import Urls
from selenium.webdriver.common.by import By

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, base_url=Urls.BASE)

    def click_order_button(self, top=True):
        locator = OrderLocators.ORDER_BUTTON_TOP if top else OrderLocators.ORDER_BUTTON_BOTTOM
        self.click_element(locator)

    def fill_first_page(self, name, last_name, address, metro_station, phone):
        self.send_keys(OrderLocators.NAME, name)
        self.send_keys(OrderLocators.LAST_NAME, last_name)
        self.send_keys(OrderLocators.ADDRESS, address)
        
        self.click_element(OrderLocators.METRO_STATION)
        stations = self.find_elements(OrderLocators.METRO_OPTION)
        for station in stations:
            if metro_station in station.text:
                station.click()
                break
                
        self.send_keys(OrderLocators.PHONE, phone)
        self.click_element(OrderLocators.NEXT_BUTTON)

    def fill_second_page(self, date, period_index, color, comment=""):
        self.click_element(OrderLocators.DATE)
        self.find_element(By.TAG_NAME, 'body').click()
        
        self.click_element(OrderLocators.RENT_PERIOD)
        periods = self.find_elements(OrderLocators.RENT_OPTIONS)
        periods[period_index].click()
        
        checkbox = OrderLocators.BLACK_CHECKBOX if color == "black" else OrderLocators.GREY_CHECKBOX
        self.click_element(checkbox)
        
        if comment:
            self.send_keys(OrderLocators.COMMENT, comment)
        
        self.click_element(OrderLocators.ORDER_BUTTON)
        self.click_element(OrderLocators.CONFIRM_BUTTON)
        return self.find_element(OrderLocators.SUCCESS_MESSAGE).text
    
    def check_scooter_logo(self):
        self.click_element(OrderLocators.SCOOTER_LOGO)
        self.wait.until(lambda d: d.current_url == Urls.BASE)
        return self.driver.current_url == Urls.BASE

    def check_yandex_logo(self):
        main_window = self.driver.current_window_handle
        self.click_element(OrderLocators.YANDEX_LOGO)
        
        self.wait.until(lambda d: len(d.window_handles) > 1)
        new_window = [w for w in self.driver.window_handles if w != main_window][0]
        self.driver.switch_to.window(new_window)
        
        is_dzen = "dzen.ru" in self.driver.current_url
        self.driver.close()
        self.driver.switch_to.window(main_window)
        return is_dzen