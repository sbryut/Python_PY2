class Hobby:
    """
    Базовый класс для хобби.
    """
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Хобби: {self.name}"

    def __repr__(self):
        return f"Hobby('{self.name}')"

class Knitting(Hobby):
    """
    Класс для вязания, наследует от хобби.
    """
    def __init__(self, name: str, yarn_type: str):
        super().__init__(name)
        self.yarn_type = yarn_type

    def __str__(self):
        return f"Вязание: {self.name}, Тип пряжи: {self.yarn_type}"

    def __repr__(self):
        return f"Knitting('{self.name}', '{self.yarn_type}')"

class Painting(Hobby):
    """
    Класс для рисования, наследует от хобби.
    """
    def __init__(self, name: str, style: str):
        super().__init__(name)
        self.style = style

    def __str__(self):
        return f"Рисование: {self.name}, Стиль: {self.style}"

    def __str__(self):
        return f"Painting( '{self.name}', '{self.style}')"

class Sport:
    """
    Базовый класс для спорта.
    """
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Спорт: {self.name}"

    def __repr__(self):
        return f"Sport('{self.name}')"

class Basketball(Sport):
    """
    Класс для баскетбола, наследует от спорта.
    """
    def __init__(self, name: str, team_size: int):
        super().__init__(name)
        self.team_size = team_size

    def __str__(self):
        return f"Баскетбол: {self.name}, Размер команды: {self.team_size}"

    def __str__(self):
        return f"Basketbal('{self.name}', '{self.team_size}')"

class Swimming(Sport):
    """
    Класс для плавания, наследует от спорта.
    """
    def __init__(self, name: str, pool_length: int):
        super().__init__(name)
        self.pool_length = pool_length

    def __str__(self):
        return f"Плавание: {self.name}, Длина бассейна: {self.pool_length} м"

    def __str__(self):
        return f"Swimming('{self.name}', '{self.pool_length}')"

class Browser:
    """
    Базовый класс для браузеров.
    """
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Браузер: {self.name}"

    def __repr__(self):
        return f"Browser('{self.name}')"

class YandexBrowser(Browser):
    """
    Класс для Яндекс Браузера, наследует от Browser.
    """
    def __init__(self, name: str, version: str):
        super().__init__(name)
        self.version = version

    def __str__(self):
        return f"Яндекс Браузер: {self.name}, Версия: {self.version}"

    def __str__(self):
        return f"Yandex Browser('{self.name}', '{self.version}')"

class GoogleBrowser(Browser):
    """
    Класс для Google Браузера, наследует от Browser.
    """
    def __init__(self, name: str, version: str):
        super().__init__(name)
        self.version = version

    def __str__(self):
        return f"Google Браузер: {self.name}, Версия: {self.version}"

    def __str__(self):
        return f"Google Browser('{self.name}', '{self.version}')"
