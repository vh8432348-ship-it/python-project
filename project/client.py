import requests

BASE_URL = "http://127.0.0.1:8000"


def get_movie():
    movie_id = input("Введіть ID фільму: ")

    response = requests.get(f"{BASE_URL}/movies/{movie_id}")

    if response.status_code == 200:
        print("Дані фільму:")
        print(response.json())
    else:
        print("Помилка:", response.json())


def add_movie():
    movie = {
        "id": int(input("ID: ")),
        "title": input("Назва: "),
        "director": input("Режисер: "),
        "year": int(input("Рік: ")),
    }

    response = requests.post(f"{BASE_URL}/movies", json=movie)

    print(response.json())


def delete_movie():
    movie_id = input("Введіть ID фільму для видалення: ")

    response = requests.delete(f"{BASE_URL}/movies/{movie_id}")

    print(response.json())


while True:
    print("\n1 - Отримати фільм")
    print("2 - Додати фільм")
    print("3 - Видалити фільм")
    print("0 - Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        get_movie()

    elif choice == "2":
        add_movie()

    elif choice == "3":
        delete_movie()

    elif choice == "0":
        break

    else:
        print("Невірний вибір")
