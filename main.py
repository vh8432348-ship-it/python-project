import json

FILE_NAME = "users.json"


def load_users():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


# Змінив save_users
def save_users(users):
    with open("users.json", "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4, ensure_ascii=False)


def add_user(users):
    login = input("Логін: ")

    if login in users:
        print("Користувач вже існує!")
        return

    password = input("Пароль: ")
    users[login] = password
    print("Користувача додано")


def delete_user(users):
    login = input("Логін: ")

    if login in users:
        del users[login]
        print("Користувача видалено")
    else:
        print("Не знайдено")


def change_password(users):
    login = input("Логін: ")

    if login in users:
        users[login] = input("Новий пароль: ")
        print("Пароль змінено")
    else:
        print("Не знайдено")


def login(users):
    login = input("Логін: ")
    password = input("Пароль: ")

    if users.get(login) == password:
        print("Вхід успішний!")
    else:
        print("Невірний логін або пароль")


def menu():
    users = load_users()

    while True:
        print("\n1. Додати користувача")
        print("2. Видалити користувача")
        print("3. Змінити пароль")
        print("4. Вхід")
        print("5. Зберегти і вийти")

        choice = input("Вибір: ")

        if choice == "1":
            add_user(users)

        elif choice == "2":
            delete_user(users)

        elif choice == "3":
            change_password(users)

        elif choice == "4":
            login(users)

        elif choice == "5":
            save_users(users)
            print("Збережено. Вихід...")
            break

        else:
            print("Невірний вибір")


menu()

# Завдання 2


class Cart:
    def __init__(self, user):
        self._user = user
        self._items = []
        self._total = 0

    def add(self, item, price):
        self._items.append({"item": item, "price": price})
        self._total += price

    def delete(self, item, price):
        for i in self._items:
            if i["item"] == item and i["price"] == price:
                self._items.remove(i)
                self._total -= price
                break

    def info(self):
        print(f"User: {self._user}")
        print("Items:")
        for i in self._items:
            print(f"- {i['item']} : {i['price']}")
        print(f"Total: {self._total}")

    def save(self, filename="cart.json"):
        data = {"user": self._user, "items": self._items, "total": self._total}

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def load(self, filename="cart.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)

                self._user = data.get("user")
                self._items = data.get("items", [])
                self._total = data.get("total", 0)

        except FileNotFoundError:
            print("Файл не знайдено")


# Завдання 3

with open("settings.json", "r", encoding="utf-8") as file:
    settings = json.load(file)

size = settings.get("size")
background_color = settings.get("background_color")
button_color = settings.get("button_color")
button_position = settings.get("button_position")
instruction = settings.get("instruction")

print(size)
print(background_color)
print(button_color)
print(button_position)
print(instruction)
