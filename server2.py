import json
import random

DATA_FILE = "books.json"

wins = 0
losses = 0


def new_game():
    global wins, losses

    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nКомп'ютер загадав число від 1 до 100")

    while True:
        user_number = int(input("Введіть число: "))
        attempts += 1

        if user_number < secret_number:
            print("Більше")

        elif user_number > secret_number:
            print("Менше")

        else:
            print(f"Ви вгадали число за {attempts} спроб!")

            if attempts < 5:
                print("Переміг користувач!")
                wins += 1
            else:
                print("Переміг комп'ютер!")
                losses += 1

            break


def show_results():
    print("\nРезультати:")
    print(f"Перемоги: {wins}")
    print(f"Поразки: {losses}")


def save_data():
    data = {"wins": wins, "losses": losses}

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("Дані збережено")


def load_data():
    global wins, losses

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

            wins = data["wins"]
            losses = data["losses"]

        print("Дані завантажено")

    except FileNotFoundError:
        print("Файл не знайдено")


def menu():
    while True:
        print("\nМеню")
        print("1 - Нова гра")
        print("2 - Показати результати")
        print("3 - Зберегти дані")
        print("4 - Завантажити дані")
        print("0 - Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            new_game()

        elif choice == "2":
            show_results()

        elif choice == "3":
            save_data()

        elif choice == "4":
            load_data()

        elif choice == "0":
            print("До побачення!")
            break

        else:
            print("Невірний вибір")


menu()
