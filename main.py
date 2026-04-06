from typing import List

# Завдання 1


class Cart:
    def __init__(self, client: str):
        self._client = client
        self._items: List[str] = []

    def add_item(self, item: str) -> None:
        self._items.append(item)

    def remove_item(self, item: str) -> None:
        if item in self._items:
            self._items.remove(item)
        else:
            print("Товар не знайдено у кошику")

    def display_info(self) -> None:
        print(f"Клієнт: {self._client}")
        print("Товари в кошику:")
        for item in self._items:
            print(f"- {item}")


# Завдання 2


class Phone:
    def __init__(self, number: str, battery_level: float):
        self._number = number
        self._battery_level = battery_level

    def decrease_battery(self, percent: float) -> None:
        self._battery_level -= percent
        if self._battery_level < 0:
            self._battery_level = 0

        if self._battery_level < 20:
            print("Низький рівень заряду!")

    def display_info(self) -> None:
        print(f"Номер: {self._number}")
        print(f"Заряд батареї: {self._battery_level}%")
