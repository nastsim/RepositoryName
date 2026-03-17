import doctest
from typing import List, Optional


class Book:
    def __init__(self, title: str, author: str, page_count: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param page_count: Количество страниц в книге

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1300)
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if not title.strip():
            raise ValueError("Название книги не может быть пустым")
        self.title = title.strip()

        if not isinstance(author, str):
            raise TypeError("Имя автора должно быть строкой")
        if not author.strip():
            raise ValueError("Имя автора не может быть пустым")
        self.author = author.strip()

        if not isinstance(page_count, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if page_count <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.page_count = page_count

        self.current_page = 1
        self.is_open = False

    def open_book(self, page: Optional[int] = None) -> None:
        """
        Открытие книги на определенной странице

        :param page: Страница, на которой открыть книгу (если не указана - открывается первая страница)
        :raise ValueError: Если указанная страница не существует в книге

        Примеры:
        >>> book = Book("1984", "Джордж Оруэлл", 328)
        >>> book.open_book(50)
        """
        if page is not None:
            if not isinstance(page, int):
                raise TypeError("Номер страницы должен быть целым числом")
            if page < 1 or page > self.page_count:
                raise ValueError(f"Страница должна быть от 1 до {self.page_count}")
            self.current_page = page
        else:
            self.current_page = 1
        self.is_open = True
        ...

    def turn_page(self, pages: int = 1) -> int:
        """
        Перелистывание страниц

        :param pages: Количество страниц для перелистывания (положительное - вперед, отрицательное - назад)
        :return: Номер текущей страницы после перелистывания
        :raise ValueError: Если книга закрыта или при попытке выйти за пределы книги

        Примеры:
        >>> book = Book("Мастер и Маргарита", "Михаил Булгаков", 480)
        >>> book.open_book(100)
        >>> current = book.turn_page(20)
        """
        if not self.is_open:
            raise ValueError("Книга закрыта. Сначала откройте книгу")

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")

        new_page = self.current_page + pages
        if new_page < 1 or new_page > self.page_count:
            raise ValueError(f"Нельзя выйти за пределы книги (страницы 1-{self.page_count})")

        self.current_page = new_page
        ...

    def get_reading_progress(self) -> float:
        """
        Получение прогресса чтения в процентах

        :return: Процент прочитанных страниц от общего объема

        Примеры:
        >>> book = Book("Преступление и наказание", "Федор Достоевский", 672)
        >>> book.open_book(336)
        >>> progress = book.get_reading_progress()
        """
        if not self.is_open:
            return 0.0
        ...


class MusicAlbum:
    def __init__(self, artist: str, title: str, track_count: int, duration_minutes: float):
        """
        Создание и подготовка к работе объекта "Музыкальный альбом"

        :param artist: Исполнитель
        :param title: Название альбома
        :param track_count: Количество треков
        :param duration_minutes: Общая длительность альбома в минутах

        Примеры:
        >>> album = MusicAlbum("The Beatles", "Abbey Road", 17, 47.5)
        """
        if not isinstance(artist, str):
            raise TypeError("Имя исполнителя должно быть строкой")
        if not artist.strip():
            raise ValueError("Имя исполнителя не может быть пустым")
        self.artist = artist.strip()

        if not isinstance(title, str):
            raise TypeError("Название альбома должно быть строкой")
        if not title.strip():
            raise ValueError("Название альбома не может быть пустым")
        self.title = title.strip()

        if not isinstance(track_count, int):
            raise TypeError("Количество треков должно быть целым числом")
        if track_count <= 0:
            raise ValueError("Количество треков должно быть положительным числом")
        self.track_count = track_count

        if not isinstance(duration_minutes, (int, float)):
            raise TypeError("Длительность должна быть числом")
        if duration_minutes <= 0:
            raise ValueError("Длительность должна быть положительным числом")
        self.duration_minutes = duration_minutes

        self.current_track = 1
        self.is_playing = False

    def play_track(self, track_number: int) -> None:
        """
        Воспроизведение указанного трека

        :param track_number: Номер трека для воспроизведения
        :raise ValueError: Если указан несуществующий номер трека

        Примеры:
        >>> album = MusicAlbum("Pink Floyd", "Dark Side of the Moon", 10, 42.5)
        >>> album.play_track(3)
        """
        if not isinstance(track_number, int):
            raise TypeError("Номер трека должен быть целым числом")
        if track_number < 1 or track_number > self.track_count:
            raise ValueError(f"Номер трека должен быть от 1 до {self.track_count}")

        self.current_track = track_number
        self.is_playing = True
        ...

    def get_album_info(self) -> str:
        """
        Получение информации об альбоме

        :return: Строка с информацией об альбоме

        Примеры:
        >>> album = MusicAlbum("Nirvana", "Nevermind", 13, 49.0)
        >>> info = album.get_album_info()
        """
        ...

    def calculate_average_track_duration(self) -> float:
        """
        Расчет средней длительности трека в альбоме

        :return: Средняя длительность трека в минутах

        Примеры:
        >>> album = MusicAlbum("Queen", "A Night at the Opera", 12, 43.0)
        >>> avg_duration = album.calculate_average_track_duration()
        """
        ...


class SocialMediaProfile:
    def __init__(self, username: str, email: str, age: int):
        """
        Создание и подготовка к работе объекта "Профиль в социальной сети"

        :param username: Имя пользователя
        :param email: Электронная почта
        :param age: Возраст пользователя

        Примеры:
        >>> profile = SocialMediaProfile("john_doe", "john@example.com", 25)
        """
        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно быть строкой")
        if not username.strip():
            raise ValueError("Имя пользователя не может быть пустым")
        if len(username) < 3:
            raise ValueError("Имя пользователя должно содержать минимум 3 символа")
        self.username = username.strip()

        if not isinstance(email, str):
            raise TypeError("Email должен быть строкой")
        if "@" not in email or "." not in email:
            raise ValueError("Некорректный формат email")
        self.email = email.strip()

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть целым числом")
        if age < 13:
            raise ValueError("Минимальный возраст для регистрации - 13 лет")
        if age > 120:
            raise ValueError("Указан некорректный возраст")
        self.age = age

        self.friends: List[str] = []
        self.posts_count = 0
        self.is_private = True

    def add_friend(self, friend_username: str) -> None:
        """
        Добавление друга в список друзей

        :param friend_username: Имя пользователя для добавления в друзья
        :raise ValueError: Если пытаются добавить себя или уже существующего друга

        Примеры:
        >>> profile = SocialMediaProfile("alice", "alice@mail.com", 28)
        >>> profile.add_friend("bob")
        """
        if not isinstance(friend_username, str):
            raise TypeError("Имя пользователя должно быть строкой")
        if not friend_username.strip():
            raise ValueError("Имя пользователя не может быть пустым")
        if friend_username == self.username:
            raise ValueError("Нельзя добавить самого себя в друзья")
        if friend_username in self.friends:
            raise ValueError("Этот пользователь уже в друзьях")

        self.friends.append(friend_username)
        ...

    def create_post(self, content: str) -> int:
        """
        Создание новой записи на странице

        :param content: Содержание записи
        :return: Общее количество записей после создания новой
        :raise ValueError: Если содержание записи пустое или превышает лимит символов

        Примеры:
        >>> profile = SocialMediaProfile("charlie", "charlie@domain.com", 32)
        >>> total_posts = profile.create_post("Привет, мир!")
        """
        if not isinstance(content, str):
            raise TypeError("Содержание записи должно быть строкой")
        if not content.strip():
            raise ValueError("Запись не может быть пустой")
        if len(content) > 280:
            raise ValueError("Запись не может превышать 280 символов")

        self.posts_count += 1
        ...

    def get_friends_count(self) -> int:
        """
        Получение количества друзей

        :return: Количество друзей пользователя

        Примеры:
        >>> profile = SocialMediaProfile("dave", "dave@site.com", 41)
        >>> profile.add_friend("eve")
        >>> friends_count = profile.get_friends_count()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()