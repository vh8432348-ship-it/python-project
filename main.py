import math

# Завдання 1


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Ім’я: {self.name}, вік: {self.age}")


students = []

for i in range(3):
    name = input("Введіть ім’я: ")
    age = int(input("Введіть вік: "))

    s = Student(name, age)
    students.append(s)

print("Інформація про студентів:")

for student in students:
    student.show_info()
# Завдання 3


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = math.pi * self.radius**2
        return area


c1 = Circle(5)

print(c1.get_area())
# Завдання 4


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Зняття успішне")
        else:
            print("Недостатньо коштів")

    def info(self):
        print(f"На рахунку {self.owner}: {self.balance}грн")


acc = BankAccount("Іван", 1000)

acc.deposit(500)
acc.withdraw(200)

acc.info()

# Завдання 5


class Car:
    def __init__(self, brand, year, is_ready=False):
        self.brand = brand
        self.year = year
        self.is_ready = is_ready

    def start_engine(self):
        self.is_ready = True

    def info(self):
        print(
            f"Марка: {self.brand} Рік випуску: {self.year}"
            f"Чи готовий до поїздки: {'Так' if self.is_ready else 'Ні'}"
        )


car = Car("BMW", 2020)

car.info()

car.start_engine()
car.info()
