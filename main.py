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
