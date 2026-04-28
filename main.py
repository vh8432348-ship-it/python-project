import json
import pickle
from typing import List, Dict


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

# Завдання 2


class Student:
    def __init__(self, name: str, specialization: str) -> None:
        self._name: str = name
        self._specialization: str = specialization
        self._grades: List[int] = []

    def add_grade(self, grade: int) -> None:
        self._grades.append(grade)

    def average_grade(self) -> float:
        if not self._grades:
            return 0.0
        return sum(self._grades) / len(self._grades)

    def show_info(self) -> None:
        print(f"Ім'я: {self._name}")
        print(f"Спеціалізація: {self._specialization}")
        print(f"Середня оцінка: {self.average_grade():.2f}")
        print("-" * 30)


def save_students_json(students: List[Dict], filename: str = "students.json") -> None:
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(students, file, ensure_ascii=False, indent=4)


def load_students_json(filename: str = "students.json") -> List[Dict]:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_students_pickle(students: List[Dict], filename: str = "students.pkl") -> None:
    with open(filename, "wb") as file:
        pickle.dump(students, file)


def load_students_pickle(filename: str = "students.pkl") -> List[Dict]:
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []


students: List[Dict] = []

s1 = Student("Іван", "Програмування")
s1.add_grade(95)
s1.add_grade(88)

students.append(
    {"name": s1._name, "specialization": s1._specialization, "grades": s1._grades}
)

s2 = Student("Марія", "Дизайн")
s2.add_grade(90)
s2.add_grade(85)

students.append(
    {"name": s2._name, "specialization": s2._specialization, "grades": s2._grades}
)

s3 = Student("Олег", "Кібербезпека")
s3.add_grade(100)
s3.add_grade(92)

students.append(
    {"name": s3._name, "specialization": s3._specialization, "grades": s3._grades}
)


save_students_json(students)
save_students_pickle(students)


json_students = load_students_json()
pickle_students = load_students_pickle()


print("=== JSON ===")
for student in json_students:
    avg = sum(student["grades"]) / len(student["grades"])
    print(f"Ім'я: {student['name']}")
    print(f"Спеціалізація: {student['specialization']}")
    print(f"Середня оцінка: {avg:.2f}")
    print("-" * 30)


print("=== Pickle ===")
for student in pickle_students:
    avg = sum(student["grades"]) / len(student["grades"])
    print(f"Ім'я: {student['name']}")
    print(f"Спеціалізація: {student['specialization']}")
    print(f"Середня оцінка: {avg:.2f}")
    print("-" * 30)

# Завдання 3


def add_friendship(friends: Dict[str, List[str]], person1: str, person2: str) -> None:
    if person1 not in friends:
        friends[person1] = []

    if person2 not in friends:
        friends[person2] = []

    if person2 not in friends[person1]:
        friends[person1].append(person2)

    if person1 not in friends[person2]:
        friends[person2].append(person1)


def save_friends_json(
    friends: Dict[str, List[str]], filename: str = "friends.json"
) -> None:
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(friends, file, ensure_ascii=False, indent=4)


def load_friends_json(filename: str = "friends.json") -> Dict[str, List[str]]:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def show_friends(friends: Dict[str, List[str]]) -> None:
    print("Список друзів:")
    for person, friends_list in friends.items():
        print(f"{person}: {', '.join(friends_list)}")


friends: Dict[str, List[str]] = {}

count: int = int(input("Скільки пар друзів ви хочете додати?: "))

for _ in range(count):
    person1: str = input("Введіть перше ім'я: ")
    person2: str = input("Введіть друге ім'я: ")

    add_friendship(friends, person1, person2)


save_friends_json(friends)


loaded_friends = load_friends_json()


show_friends(loaded_friends)
