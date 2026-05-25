import threading

numbers = []


def input_numbers():
    print("Вводьте числа. Для завершення натисніть Enter на порожньому рядку.")

    while True:
        user_input = input("Число: ")

        if user_input == "":
            break

        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Помилка! Введіть коректне число.")


def calculate_sum():
    total = sum(numbers)
    print(f"Список чисел: {numbers}")
    print(f"Сума чисел: {total}")


def calculate_average():
    if len(numbers) > 0:
        average = sum(numbers) / len(numbers)
    else:
        average = 0

    print(f"Середнє арифметичне: {average}")


thread_input = threading.Thread(target=input_numbers)

thread_input.start()

thread_input.join()

thread_sum = threading.Thread(target=calculate_sum)
thread_average = threading.Thread(target=calculate_average)

thread_sum.start()
thread_average.start()

thread_sum.join()
thread_average.join()

print("Програма завершена.")
