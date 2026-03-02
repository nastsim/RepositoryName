class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        """Геттер для названия книги (только для чтения)."""
        return self._name

    @property
    def author(self):
        """Геттер для автора книги (только для чтения)."""
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс для бумажной книги."""

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # Используем сеттер для проверки

    @property
    def pages(self):
        """Геттер для количества страниц."""
        return self._pages

    @pages.setter
    def pages(self, value):
        """Сеттер с проверкой для количества страниц."""
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self._pages = value

    def __repr__(self):
        return (f"{self.__class__.__name__}(name={self.name!r}, "
                f"author={self.author!r}, pages={self.pages!r})")


class AudioBook(Book):
    """Класс для аудиокниги."""

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # Используем сеттер для проверки

    @property
    def duration(self):
        """Геттер для длительности."""
        return self._duration

    @duration.setter
    def duration(self, value):
        """Сеттер с проверкой для длительности."""
        if not isinstance(value, (int, float)):
            raise TypeError("Длительность должна быть числом")
        if value <= 0:
            raise ValueError("Длительность должна быть положительной")
        self._duration = float(value)

    def __repr__(self):
        return (f"{self.__class__.__name__}(name={self.name!r}, "
                f"author={self.author!r}, duration={self.duration!r})")


# Пример использования:
if __name__ == "__main__":
    # Создание объектов
    paper_book = PaperBook("Война и мир", "Лев Толстой", 1300)
    audio_book = AudioBook("1984", "Джордж Оруэлл", 11.5)

    # Демонстрация работы методов
    print(paper_book)  # __str__ унаследован от Book
    print(audio_book)  # __str__ унаследован от Book

    print(repr(paper_book))  # __repr__ переопределён в PaperBook
    print(repr(audio_book))  # __repr__ переопределён в AudioBook

    # Проверка защиты атрибутов name и author
    # paper_book.name = "Новое название"  # Ошибка! AttributeError

    # Проверка валидации
    try:
        paper_book.pages = -100  # Ошибка! ValueError
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        audio_book.duration = "десять"  # Ошибка! TypeError
    except TypeError as e:
        print(f"Ошибка: {e}")