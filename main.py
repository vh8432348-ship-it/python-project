# Завдання 1
class Project:
    def __init__(
        self, name, budget, total_cost=0, is_completed=False, duration=0, tasks=None
    ):
        self.name = name
        self.budget = budget
        self.total_cost = total_cost
        self.is_completed = is_completed
        self.duration = duration
        self.tasks = tasks if tasks is not None else []

    def show_info(self):
        print(
            f"Назва: {self.name} Час виконання: {self.duration} Необхідні задачі: {self.tasks}"
        )

    def add_task(self, task):
        self.tasks.append(task)

    def split_task(self, task_name, subtasks):
        for task in self.tasks:
            if task["name"] == task_name:
                task["subtasks"] = subtasks
                return
        print("Задачу не знайдено")

    def complete_task(self, task_name, time_spent, cost):
        for task in self.tasks:
            if task["name"] == task_name:
                task["completed"] = True
                task["time"] = time_spent
                task["cost"] = cost

                self.duration += time_spent
                self.total_cost += cost
                return
        print("Задачу не знайдено")
