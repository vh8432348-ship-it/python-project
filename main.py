import threading


# Завдання 1


def find_max(numbers, res_max):
    res_max["max"] = max(numbers)


def find_min(numbers, res_min):
    res_min["min"] = min(numbers)


numbers = list(map(int, input("Введіть числа через пробіл: ").split()))

res_max: dict[str, int] = {}
res_min: dict[str, int] = {}

thread_max = threading.Thread(target=find_max, args=(numbers, res_max))
thread_min = threading.Thread(target=find_min, args=(numbers, res_min))

thread_max.start()
thread_min.start()

thread_max.join()
thread_min.join()

print(f"Максимум у списку: {res_max['max']}")
print(f"Мінімум у списку: {res_min['min']}")

# Завдання 2


def find_sum(numbers):
    total = sum(numbers)
    print(f"Сума елементів списку: {total}")


def find_average(numbers):
    average = sum(numbers) / len(numbers)
    print(f"Середнє арифметичне: {average}")


numbers = list(map(int, input("Введіть числа через пробіл: ").split()))

thread_sum = threading.Thread(target=find_sum, args=(numbers,))
thread_average = threading.Thread(target=find_average, args=(numbers,))

thread_sum.start()
thread_average.start()

thread_sum.join()
thread_average.join()
