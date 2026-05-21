import json
import pickle

music_groups = {}


def add_group():
    group_name = input("Введіть назву гурту: ")

    if group_name in music_groups:
        print("Гурт вже існує!")
    else:
        music_groups[group_name] = []
        print("Гурт додано!")


def add_album():
    group_name = input("Введіть назву гурту: ")

    if group_name not in music_groups:
        print("Гурт не знайдено!")
        return

    album_name = input("Введіть назву альбому: ")
    music_groups[group_name].append(album_name)

    print("Альбом додано!")


def save_json():
    with open("groups.json", "w", encoding="utf-8") as file:
        json.dump(music_groups, file, ensure_ascii=False, indent=4)

    print("Дані збережено у JSON!")


def load_json():
    global music_groups

    try:
        with open("groups.json", "r", encoding="utf-8") as file:
            music_groups = json.load(file)

        print("Дані завантажено з JSON!")

    except FileNotFoundError:
        print("Файл JSON не знайдено!")


def save_pickle():
    with open("groups.pkl", "wb") as file:
        pickle.dump(music_groups, file)

    print("Дані збережено у Pickle!")


def load_pickle():
    global music_groups

    try:
        with open("groups.pkl", "rb") as file:
            music_groups = pickle.load(file)

        print("Дані завантажено з Pickle!")

    except FileNotFoundError:
        print("Файл Pickle не знайдено!")


def show_data():
    if not music_groups:
        print("Даних немає!")
        return

    for group, albums in music_groups.items():
        print(f"\nГурт: {group}")

        if albums:
            for album in albums:
                print(f" - {album}")
        else:
            print(" Альбомів немає")


while True:
    print("\n--- МЕНЮ ---")
    print("1 - Додати гурт")
    print("2 - Додати альбом")
    print("3 - Зберегти у JSON")
    print("4 - Завантажити з JSON")
    print("5 - Зберегти у Pickle")
    print("6 - Завантажити з Pickle")
    print("7 - Показати дані")
    print("0 - Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        add_group()

    elif choice == "2":
        add_album()

    elif choice == "3":
        save_json()

    elif choice == "4":
        load_json()

    elif choice == "5":
        save_pickle()

    elif choice == "6":
        load_pickle()

    elif choice == "7":
        show_data()

    elif choice == "0":
        print("Програма завершена!")
        break

    else:
        print("Невірний вибір!")
