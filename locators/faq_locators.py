from selenium.webdriver.common.by import By

class FAQPageLocators:
    FAQ_HEADER = (By.XPATH, '//div[@class="Home_SubHeader__zwi_E" and text()="Вопросы о важном"]')
    
    # Вопросы
    QUESTION_1 = (By.XPATH, '//div[@data-accordion-component="AccordionItemButton" and text()="Сколько это стоит? И как оплатить?"]')
    QUESTION_2 = (By.XPATH, '//div[@data-accordion-component="AccordionItemButton" and contains(text(), "Хочу сразу несколько самокатов")]')
    QUESTION_3 = (By.XPATH, '//div[@data-accordion-component="AccordionItemButton" and text()="Как рассчитывается время аренды?"]')
    QUESTION_4 = (By.XPATH, '//div[@data-accordion-component="AccordionItemButton" and text()="Можно ли заказать самокат прямо на сегодня?"]')
    QUESTION_5 = (By.XPATH, '//div[@data-accordion-component="AccordionItemButton" and contains(text(), "Можно ли продлить заказ")]')
    QUESTION_6 = (By.XPATH, '//div[@data-accordion-component="AccordionItemButton" and text()="Вы привозите зарядку вместе с самокатом?"]')
    QUESTION_7 = (By.XPATH, '//div[@data-accordion-component="AccordionItemButton" and text()="Можно ли отменить заказ?"]')
    QUESTION_8 = (By.XPATH, '//div[@data-accordion-component="AccordionItemButton" and contains(text(), "за МКАДом")]')
    
    @staticmethod
    def answer_panel(index):
        return (By.XPATH, f'//div[@id="accordion__panel-{index}" and not(@hidden)]')