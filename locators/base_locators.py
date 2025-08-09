from selenium.webdriver.common.by import By

class BaseLocators:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/"
    COOKIE_BANNER = (By.ID, "rcc-confirm-button")  # Добавляем локатор кнопки принятия cookie