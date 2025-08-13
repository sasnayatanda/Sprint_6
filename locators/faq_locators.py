from selenium.webdriver.common.by import By

class OrderLocators:
    
    # Кнопки заказа
    ORDER_BUTTON_TOP = (By.CSS_SELECTOR, ".Button_Button__ra12g")  # Первая кнопка "Заказать"
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[contains(text(), 'Заказать')])[2]")  # Вторая кнопка
    
    # Первая форма
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.CLASS_NAME, "select-search__input")
    METRO_OPTION = (By.CSS_SELECTOR, ".select-search__option")  # Все станции
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    # Вторая форма
    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_PERIOD = (By.CLASS_NAME, "Dropdown-placeholder")
    RENT_OPTIONS = (By.CLASS_NAME, "Dropdown-option")  # Все варианты аренды
    BLACK_CHECKBOX = (By.ID, "black")
    GREY_CHECKBOX = (By.ID, "grey")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[2]")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    
    # Подтверждение
    SUCCESS_MESSAGE = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    
    # локатор календаря
    DATE_INPUT = (By.CLASS_NAME, "react-datepicker")  
    
    #Логотипы
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")