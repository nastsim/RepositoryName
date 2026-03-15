class Vehicle:
    """Базовый класс для всех транспортных средств."""

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Конструктор базового класса Vehicle.

        Args:
            brand (str): марка транспортного средства
            model (str): модель транспортного средства
            year (int): год выпуска
        """
        self.brand: str = brand
        self.model: str = model
        self.year: int = year
        self._current_speed: int = 0
        # Непубличный (protected) атрибут _current_speed:
        # причина инкапсуляции — внутреннее состояние объекта,
        # которое не должно изменяться напрямую извне класса.
        # Подклассы могут обращаться к нему, но внешний код — нет.

    def __str__(self) -> str:
        """
        Возвращает человекочитаемое строковое представление объекта.
        """
        return f"{self.year} {self.brand} {self.model}"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление для отладки.
        """
        return f"Vehicle(brand='{self.brand}', model='{self.model}', year={self.year})"

    def start_engine(self) -> str:
        """
        Запускает двигатель (унаследованный метод).

        Returns:
            str: сообщение о результате
        """
        return "Двигатель успешно запущен."

    def accelerate(self, increment: int) -> None:
        """
        Увеличивает текущую скорость на заданное значение.

        Args:
            increment (int): приращение скорости (км/ч)
        """
        self._current_speed += increment

    def get_speed(self) -> int:
        """
        Возвращает текущую скорость.

        Returns:
            int: текущая скорость в км/ч
        """
        return self._current_speed

class Car(Vehicle):
    """Дочерний класс Легковой автомобиль."""

    def __init__(self, brand: str, model: str, year: int, num_doors: int) -> None:
        """
        Конструктор дочернего класса Car.
        Расширяет конструктор базового класса Vehicle, добавляя атрибут num_doors.

        Args:
            brand (str): марка
            model (str): модель
            year (int): год выпуска
            num_doors (int): количество дверей
        """
        super().__init__(brand, model, year)
        self.num_doors: int = num_doors

    def __str__(self) -> str:
        """
        Перегружает магический метод __str__ базового класса.
        Добавляет информацию о количестве дверей для более точного описания.
        """
        return f"{super().__str__()} (легковой автомобиль, {self.num_doors} дверей)"

    def __repr__(self) -> str:
        """
        Перегружает магический метод __repr__ базового класса.
        Включает все атрибуты дочернего класса.
        """
        return (f"Car(brand='{self.brand}', model='{self.model}', "
                f"year={self.year}, num_doors={self.num_doors})")

    def accelerate(self, increment: int) -> None:
        """
        Перегруженный метод accelerate (перегрузка помимо магических методов).

        Причина перегрузки: легковые автомобили имеют ограничение по максимальной
        скорости (180 км/ч) для безопасности пассажиров и комфорта. В базовом
        классе Vehicle такой проверки нет — там скорость может расти неограниченно.
        Это демонстрирует специфическое поведение подкласса (полиморфизм).

        Args:
            increment (int): приращение скорости
        """
        max_speed = 180
        if self._current_speed + increment > max_speed:
            increment = max_speed - self._current_speed
        super().accelerate(increment)  # вызываем унаследованную логику базового класса

if __name__ == "__main__":
    # Демонстрация работы классов
    print("=== Базовый класс Vehicle ===")
    vehicle = Vehicle("Toyota", "Corolla", 2020)
    print(vehicle)                    # использует __str__
    print(repr(vehicle))              # использует __repr__
    print(vehicle.start_engine())     # унаследованный метод
    vehicle.accelerate(60)
    print(f"Скорость: {vehicle.get_speed()} км/ч")


nt("\n=== Дочерний класс Car ===")
    car = Car("BMW", "X5", 2022, 4)
    print(car)                        # перегруженный __str__
    print(repr(car))                  # перегруженный __repr__
    print(car.start_engine())         # унаследованный метод (не перегружен)
    car.accelerate(150)               # перегруженный метод
    print(f"Скорость: {car.get_speed()} км/ч")  # унаследованный get_speed pri