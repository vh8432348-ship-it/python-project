from typing import List, Dict, Optional

# Завдання 1


class Project:
    def __init__(
        self,
        name: str,
        budget: float,
        total_cost: float = 0,
        is_completed: bool = False,
        duration: int = 0,
        tasks: Optional[List[Dict]] = None,
    ) -> None:
        self.name: str = name
        self.budget: float = budget
        self.total_cost: float = total_cost
        self.is_completed: bool = is_completed
        self.duration: int = duration
        self.tasks: List[Dict] = tasks if tasks is not None else []

    def show_info(self) -> None:
        print(
            f"Назва: {self.name}\n"
            f"Час виконання: {self.duration}\n"
            f"Витрати: {self.total_cost}\n"
            f"Задачі: {self.tasks}"
        )

    def add_task(self, task: Dict) -> None:
        self.tasks.append(task)

    def split_task(self, task_name: str, subtasks: List[str]) -> None:
        for task in self.tasks:
            if task["name"] == task_name:
                task["subtasks"] = subtasks
                return
        print("Задачу не знайдено")

    def complete_task(self, task_name: str, time_spent: int, cost: float) -> None:
        for task in self.tasks:
            if task["name"] == task_name:
                task["completed"] = True
                task["time"] = time_spent
                task["cost"] = cost

                self.duration += time_spent
                self.total_cost += cost
                return
        print("Задачу не знайдено")


# Завдання 2


class Phone:
    def __init__(self, max_memory=1000, used_memory=0, is_on=False, apps=None):
        self.max_memory = max_memory
        self.used_memory = used_memory
        self.is_on = is_on
        self.apps = apps if apps is not None else {}

    def memory_info(self):
        free_memory = self.max_memory - self.used_memory
        print(f"Зайнято: {self.used_memory}")
        print(f"Всього: {self.max_memory}")
        print(f"Вільно: {free_memory}")

    def delete_app(self, app_name):
        if app_name in self.apps:
            self.used_memory -= self.apps[app_name]
            del self.apps[app_name]
            print("Додаток видалено")
        else:
            print("Додаток не знайдено")

    def add_app(self, app_name, app_memory):
        free_memory = self.max_memory - self.used_memory
        if app_memory <= free_memory:
            self.apps[app_name] = app_memory
            self.used_memory += app_memory
        else:
            print(f"Недостатньо пам'яті. Вільної пам'яті {free_memory}")

    def update_app(self, app_name, new_app_memory):
        if app_name in self.apps:
            free_memory = self.max_memory - self.used_memory
            if new_app_memory <= free_memory:
                self.apps[app_name] = new_app_memory
            else:
                print("Недостатньо пам'яті для оновлення")

        else:
            print(f"Додатку за назвую {app_name} не існує(")

    def run_app(self, app_name):
        if not self.is_on:
            print("Телефон вимкнений")
            return

        if app_name in self.apps:
            print(f"Запуск додатку {app_name}...")
        else:
            print("Додаток не встановлений")

    def turn_on(self):
        self.is_on = True
        print("Телефон увімкнено")

    def turn_off(self):
        self.is_on = False
        print("Телефон вимкнено")
