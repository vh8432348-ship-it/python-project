import math

# Завдання 1


class Rectangle:
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    def get_perimeter(self) -> float:
        return 2 * (self._width + self._height)

    def display_info(self) -> None:
        print(
            f"Rectangle: width={self._width}, height={self._height}, perimeter={self.get_perimeter()}"
        )


class Circle:
    def __init__(self, radius: float):
        self._radius = radius

    def get_perimeter(self) -> float:
        return 2 * math.pi * self._radius

    def display_info(self) -> None:
        print(f"Circle: radius={self._radius}, perimeter={self.get_perimeter()}")


class Triangle:
    def __init__(self, a: float, b: float, c: float):
        self._a = a
        self._b = b
        self._c = c

    def get_perimeter(self) -> float:
        return self._a + self._b + self._c

    def display_info(self) -> None:
        print(
            f"Triangle: a={self._a}, b={self._b}, c={self._c}, perimeter={self.get_perimeter()}"
        )


def create_figure():
    figure_type = input("Введіть тип фігури (rectangle/circle/triangle): ").lower()

    if figure_type == "rectangle":
        width = float(input("Введіть ширину: "))
        height = float(input("Введіть висоту: "))
        return Rectangle(width, height)

    elif figure_type == "circle":
        radius = float(input("Введіть радіус: "))
        return Circle(radius)

    elif figure_type == "triangle":
        a = float(input("Введіть сторону a: "))
        b = float(input("Введіть сторону b: "))
        c = float(input("Введіть сторону c: "))
        return Triangle(a, b, c)

    else:
        print("Невідомий тип фігури")
        return None


figures = []

for _ in range(3):
    fig = create_figure()
    if fig:
        figures.append(fig)

for fig in figures:
    fig.display_info()

# Завдання 2


class Employee:
    def __init__(self, name: str, base_salary: float):
        self._name = name
        self._base_salary = base_salary

    def get_salary(self) -> float:
        raise NotImplementedError


class Manager(Employee):
    def __init__(self, name: str, base_salary: float):
        super().__init__(name, base_salary)

    def get_salary(self) -> float:
        return self._base_salary


class Developer(Employee):
    def __init__(self, name: str, base_salary: float, work_experience: int):
        super().__init__(name, base_salary)
        self._work_experience = work_experience

    def get_salary(self) -> float:
        if self._work_experience > 4:
            return self._base_salary * 1.2
        return self._base_salary


class Intern(Employee):
    def __init__(self, name: str, base_salary: float):
        super().__init__(name, base_salary)

    def get_salary(self) -> float:
        return self._base_salary * 0.5


def create_worker():
    worker_type = input("Введіть тип працівника (manager/developer/intern): ").lower()

    name = input("Введіть ім'я: ")
    base_salary = float(input("Введіть базову зарплату: "))

    if worker_type == "manager":
        return Manager(name, base_salary)

    elif worker_type == "developer":
        work_experience = int(input("Введіть стаж роботи (років): "))
        return Developer(name, base_salary, work_experience)

    elif worker_type == "intern":
        return Intern(name, base_salary)

    else:
        print("Невідомий тип працівника")
        return None


workers = []

for _ in range(3):
    worker = create_worker()
    if worker:
        workers.append(worker)

for worker in workers:
    print(f"{worker._name}: {worker.get_salary()}")


# Завдання 3
class Vehicle:
    def __init__(self, speed: float):
        self.check_speed(speed)
        self._speed = speed

    def check_speed(self, speed: float):
        raise NotImplementedError

    def move(self):
        raise NotImplementedError


class Car(Vehicle):
    def check_speed(self, speed: float):
        if not (20 <= speed <= 200):
            raise ValueError("Швидкість для Car має бути від 20 до 200")

    def move(self):
        print(f"Car їде по шосе зі швидкістю {self._speed}")


class Bicycle(Vehicle):
    def check_speed(self, speed: float):
        if not (10 <= speed <= 30):
            raise ValueError("Швидкість для Bicycle має бути від 10 до 30")

    def move(self):
        print(f"Bicycle їде по дорозі зі швидкістю {self._speed}")


class Boat(Vehicle):
    def check_speed(self, speed: float):
        if not (0 <= speed <= 50):
            raise ValueError("Швидкість для Boat має бути від 0 до 50")

    def move(self):
        print(f"Boat пливе по воді зі швидкістю {self._speed}")


def create_vehicle():
    vehicle_type = input("Введіть тип транспорту (car/bicycle/boat): ").lower()
    speed = float(input("Введіть швидкість: "))

    if vehicle_type == "car":
        return Car(speed)

    elif vehicle_type == "bicycle":
        return Bicycle(speed)

    elif vehicle_type == "boat":
        return Boat(speed)

    else:
        print("Невідомий тип транспорту")
        return None


vehicles = []

for _ in range(3):
    try:
        vehicle = create_vehicle()
        if vehicle:
            vehicles.append(vehicle)
    except ValueError as e:
        print(e)

for v in vehicles:
    v.move()
