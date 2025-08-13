class Urls:
    BASE = "https://qa-scooter.praktikum-services.ru/"
    DZEN = "https://dzen.ru/"
    ORDER = "/order"
    
    # Эндпоинты
    ORDER = "/order"
    FAQ = "#faq"
    
    @staticmethod
    def get_full_url(path):
        return f"{Urls.BASE}{path.lstrip('/')}"
    
class TestData:
    DEFAULT_NAME = "Тест"
    DEFAULT_PHONE = "89991112233"