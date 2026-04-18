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
        self._apps = {}  # {name: size}

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

    # 🔹 Запустити додаток
    def run_app(self, name):
        if not self._is_on:
            print("Телефон вимкнено")
            return

        if name in self._apps:
            print(f"Запуск {name}...")
        else:
            print("Додаток не встановлено")
