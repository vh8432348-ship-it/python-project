import json
import pickle


def add_product(products):
    product = input("Введіть назву товару: ")
    products.append(product)
    print("Товар додано!")


def show_products(products):
    if not products:
        print("Список товарів порожній.")
    else:
        print("Список товарів:")
        for i, product in enumerate(products, start=1):
            print(f"{i}. {product}")


def save_json(products, filename="products.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(products, file, ensure_ascii=False, indent=4)
    print("Дані збережено у JSON!")


def load_json(filename="products.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            products = json.load(file)
        print("Дані завантажено з JSON!")
        return products
    except FileNotFoundError:
        print("Файл JSON не знайдено.")
        return []


def save_pickle(products, filename="products.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(products, file)
    print("Дані збережено у Pickle!")


def load_pickle(filename="products.pkl"):
    try:
        with open(filename, "rb") as file:
            products = pickle.load(file)
        print("Дані завантажено з Pickle!")
        return products
    except FileNotFoundError:
        print("Файл Pickle не знайдено.")
        return []


def menu():
    products = []

    while True:
        print("Меню:")
        print("1. Додати товар")
        print("2. Вивести список товарів")
        print("3. Зберегти у JSON")
        print("4. Зберегти у Pickle")
        print("5. Завантажити з JSON")
        print("6. Завантажити з Pickle")
        print("7. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            add_product(products)

        elif choice == "2":
            show_products(products)

        elif choice == "3":
            save_json(products)

        elif choice == "4":
            save_pickle(products)

        elif choice == "5":
            products = load_json()

        elif choice == "6":
            products = load_pickle()

        elif choice == "7":
            print("Програму завершено.")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")


menu()
