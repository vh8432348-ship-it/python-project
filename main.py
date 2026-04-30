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

# Завдання 3


def write_even_numbers(numbers: list[int], result: dict[str, int]):
    even_numbers = [num for num in numbers if num % 2 == 0]

    with open("even_numbers.txt", "w", encoding="utf-8") as file:
        for num in even_numbers:
            file.write(f"{num}\n")

    result["even_count"] = len(even_numbers)


def write_odd_numbers(numbers: list[int], result: dict[str, int]):
    odd_numbers = [num for num in numbers if num % 2 != 0]

    with open("odd_numbers.txt", "w", encoding="utf-8") as file:
        for num in odd_numbers:
            file.write(f"{num}\n")

    result["odd_count"] = len(odd_numbers)


file_path = input("Введіть шлях до файлу з числами: ")

with open(file_path, "r", encoding="utf-8") as file:
    numbers = list(map(int, file.read().split()))

result0: dict[str, int] = {}

thread_even = threading.Thread(
    target=write_even_numbers,
    args=(numbers, result0),
)

thread_odd = threading.Thread(
    target=write_odd_numbers,
    args=(numbers, result0),
)

thread_even.start()
thread_odd.start()

thread_even.join()
thread_odd.join()

print(f"Кількість парних чисел: {result0['even_count']}")
print(f"Кількість непарних чисел: {result0['odd_count']}")

# Завдання 4


def search_word_in_file(file_path: str, search_word: str, result: dict[str, int]):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    count = text.lower().split().count(search_word.lower())

    result["count"] = count


file_path = input("Введіть шлях до файлу: ")
search_word = input("Введіть слово для пошуку: ")

result1: dict[str, int] = {}

search_thread = threading.Thread(
    target=search_word_in_file,
    args=(file_path, search_word, result1),
)

search_thread.start()

search_thread.join()

if result["count"] > 0:
    print(f"Слово '{search_word}' знайдено {result1['count']} раз(ів).")
else:
    print(f"Слово '{search_word}' не знайдено.")
