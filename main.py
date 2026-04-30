import threading


# Завдання 1


numbers = []
count = int(input("Enter count of numbers: "))

for _ in range(count):
    number = int(input("Enter number: "))
    numbers.append(number)


def find_max(numbers: list[int], result: dict[str, int]):
    result["max"] = max(numbers)


def find_min(numbers: list[int], result: dict[str, int]):
    result["min"] = min(numbers)


result: dict[str, int] = {}

thread_max = threading.Thread(
    target=find_max,
    args=(numbers, result),
)

thread_min = threading.Thread(
    target=find_min,
    args=(numbers, result),
)

thread_max.start()
thread_min.start()

thread_max.join()
thread_min.join()

print(f"Max = {result['max']}")
print(f"Min = {result['min']}")

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
