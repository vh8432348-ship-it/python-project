import threading


# Завдання 1
def find_max(numbers):
    maximum = max(numbers)
    print(f"Максимум у списку: {maximum}")


def find_min(numbers):
    minimum = min(numbers)
    print(f"Мінімум у списку: {minimum}")


numbers = list(map(int, input("Введіть числа через пробіл: ").split()))

thread_max = threading.Thread(target=find_max, args=(numbers,))
thread_min = threading.Thread(target=find_min, args=(numbers,))

thread_max.start()
thread_min.start()

thread_max.join()
thread_min.join()
