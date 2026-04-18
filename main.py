import random

# Завдання 1


class Project:
    def __init__(self, name, budget):
        self._name = name
        self._budget = budget
        self._total_cost = 0
        self._completed = False
        self._time = 0
        self._tasks = []

    def show_info(self):
        print(f"Назва: {self._name}")
        print(f"Час виконання: {self._time} місяців")
        print("Задачі:", self._tasks)

    def add_task(self, task_name):
        self._tasks.append(task_name)

    def split_task(self, task_name, subtasks):
        if task_name in self._tasks:
            self._tasks.remove(task_name)
            self._tasks.extend(subtasks)
        else:
            print("Такої задачі немає")

    def complete_task(self, task_name, time_spent, cost):
        if task_name in self._tasks:
            self._tasks.remove(task_name)
            self._time += time_spent
            self._total_cost += cost

            if self._total_cost > self._budget:
                print("Перевищено кошторис!")

            if not self._tasks:
                self._completed = True
        else:
            print("Такої задачі немає")

    def add_budget(self, amount):
        self._budget += amount


# Завдання 2
class Phone:
    def __init__(self, max_memory):
        self._max_memory = max_memory
        self._used_memory = 0
        self._is_on = False
        self._apps = {}

    def show_memory_info(self):
        print(f"Максимальна пам'ять: {self._max_memory}")
        print(f"Зайнята пам'ять: {self._used_memory}")
        print(f"Вільна пам'ять: {self._max_memory - self._used_memory}")
        print(f"Додатки: {self._apps}")

    def turn_on(self):
        self._is_on = True
        print("Телефон увімкнено")

    def turn_off(self):
        self._is_on = False
        print("Телефон вимкнено")

    def install_app(self, name, size):
        if self._used_memory + size <= self._max_memory:
            self._apps[name] = size
            self._used_memory += size
            print(f"Встановлено {name}")
        else:
            print("Недостатньо пам’яті")

    def delete_app(self, name):
        if name in self._apps:
            self._used_memory -= self._apps[name]
            del self._apps[name]
            print(f"Видалено {name}")
        else:
            print("Такого додатку немає")

    def update_app(self, name, new_size):
        if name in self._apps:
            old_size = self._apps[name]
            difference = new_size - old_size

            if self._used_memory + difference <= self._max_memory:
                self._apps[name] = new_size
                self._used_memory += difference
                print(f"{name} оновлено")
            else:
                print("Недостатньо пам’яті для оновлення")
        else:
            print("Такого додатку немає")

    def run_app(self, name):
        if not self._is_on:
            print("Телефон вимкнено")
            return

        if name in self._apps:
            print(f"Запуск {name}...")
        else:
            print("Додаток не встановлено")


# Завдання 3


class Car:
    def __init__(self, brand, fuel, consumption):
        self._brand = brand
        self._mileage = 0
        self._fuel = fuel
        self._consumption = consumption  # л/км
        self._is_ok = True

    def drive(self, distance):
        if not self._is_ok:
            print("Авто зламане")
            return

        needed_fuel = distance * self._consumption

        if needed_fuel > self._fuel:
            print("Недостатньо пального")
            return

        self._fuel -= needed_fuel
        self._mileage += distance

        if random.random() < 0.4:
            self._is_ok = False
            print("Авто зламалось під час поїздки!")
        else:
            print("Поїздка успішна")

    def repair(self):
        self._is_ok = True
        print("Авто відремонтовано")

    def refuel(self, fuel):
        self._fuel += fuel


# Завдання 4


class Student:
    def __init__(self, name):
        self._name = name
        self._subjects = {}

    def add_subject(self, subject):
        self._subjects[subject] = []

    def remove_subject(self, subject):
        if subject in self._subjects:
            del self._subjects[subject]

    def study(self, subject, grade):
        if subject in self._subjects:
            self._subjects[subject].append(grade)

    def average(self, subject):
        if subject in self._subjects and self._subjects[subject]:
            return sum(self._subjects[subject]) / len(self._subjects[subject])
        return 0

    def show_info(self):
        print(f"Студент: {self._name}")
        for subject, grades in self._subjects.items():
            avg = sum(grades) / len(grades) if grades else 0
            print(f"{subject}: {avg}")


# Завдання 5


class Shop:
    def __init__(self, name):
        self._name = name
        self._profit = 0
        self._stock = {}
        self._prices = {}

    def show_info(self):
        print(f"Магазин: {self._name}")
        print("Товари:", self._stock)

    def add_product(self, name, quantity, price):
        self._stock[name] = self._stock.get(name, 0) + quantity
        self._prices[name] = price

    def order(self, name, quantity):
        if name not in self._stock:
            print("Нема товару")
            return

        if self._stock[name] < quantity:
            print("Недостатньо товару")
            return

        self._stock[name] -= quantity
        self._profit += self._prices[name] * quantity
        print("Замовлення оформлено")
