from selenium.webdriver.common.by import By


    

class FAQPageLocators:
    # Заголовок раздела
    FAQ_HEADER = (By.XPATH, '//div[@class="Home_SubHeader__zwi_E" and text()="Вопросы о важном"]')
    
    # Кнопки вопросов
    QUESTION_1_COST = (By.XPATH, '//div[@data-accordion-component="AccordionItemButton" and text()="Сколько это стоит? И как оплатить?"]')
    QUESTION_2_MULTIPLE_SCOOTERS = (By.XPATH, '//div[@data-accordion-component="AccordionItemButton" and contains(text(), "Хочу сразу несколько самокатов")]')
    QUESTION_3_RENT_TIME = (By.XPATH, '//div[@data-accordion-component="AccordionItemButton" and text()="Как рассчитывается время аренды?"]')
    QUESTION_4_TODAY_ORDER = (By.XPATH, '//div[@data-accordion-component="AccordionItemButton" and text()="Можно ли заказать самокат прямо на сегодня?"]')
    QUESTION_5_EXTEND_ORDER = (By.XPATH, '//div[@data-accordion-component="AccordionItemButton" and contains(text(), "Можно ли продлить заказ")]')
    QUESTION_6_CHARGER = (By.XPATH, '//div[@data-accordion-component="AccordionItemButton" and text()="Вы привозите зарядку вместе с самокатом?"]')
    QUESTION_7_CANCEL_ORDER = (By.XPATH, '//div[@data-accordion-component="AccordionItemButton" and text()="Можно ли отменить заказ?"]')
    QUESTION_8_OUTSIDE_MKAD = (By.XPATH, '//div[@data-accordion-component="AccordionItemButton" and contains(text(), "за МКАДом")]')
    
    BASE_URL = "https://qa-scooter.praktikum-services.ru/"
    
    # Панели ответов (шаблон)
    @staticmethod
    def answer_panel(index):
        return (By.XPATH, f'//div[@id="accordion__panel-{index}" and not(@hidden)]')