from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("occupied_volume должен быть int или float")
        if occupied_volume < 0:
            raise ValueError("occupied_volume не может быть отрицательным")
        self.occupied_volume = occupied_volume

    def init_capacity_volume(self, capacity_volume: Union[int, float]) -> None:
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("capacity_volume должен быть int или float")
        if capacity_volume <= 0:
            raise ValueError("capacity_volume должен быть положительным")
        self.capacity_volume = capacity_volume


if __name__ == "__main__":
    glass = Glass(200, 100)  # инициализируем экземпляр класса Glass
    print(glass.capacity_volume)  # распечатать атрибут capacity_volume
    print(glass.occupied_volume)  # распечатать атрибут occupied_volume