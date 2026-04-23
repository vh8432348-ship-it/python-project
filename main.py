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


def save_users(users):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)


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
