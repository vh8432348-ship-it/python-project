# Завдання 1
"""
    Є текстовий файл. Запишіть в інший файл таку
статистику:
 Кількість символів
 Кількість рядків
 Кількість цифр
 Кількість голосних літер(aeuio)
"""

numbers = "1234567890"
numbers_count = 0
vowel_letter = 0
litters = "aeuio"
with open("test.txt", "r") as file:
    content = file.read()
    count_sym = len(content)
    count_of_lines = len(content.splitlines())

    for a in content:
        if a in numbers:
            numbers_count += 1
        if a in litters:
            vowel_letter += 1
print(
    f"Кількість символів: {count_sym} Кількість рядків: {count_of_lines} "
    f"Кількість цифр: {numbers_count} Кількість голосних літер: {vowel_letter}"
)
# Завдання 2
"""
    Користувач вводить слово та назву файлу. Виведіть
кількість цього слова у файлі.
"""
name_of_file = input("Введіть назву файлу: ")
target = input("Ввеідть слово яке потрібной знайти: ")

try:
    with open(name_of_file, "r", encoding="utf-8") as file:
        content = file.read()

except FileNotFoundError:
    print("Файл не знайдено, використовується test.txt")
    with open("test.txt", "r", encoding="utf-8") as file:
        content = file.read()
        name_of_file = "test.txt"

words = content.split()
result = words.count(target)

print(f"Кількість цього слова {target} у файлі: {name_of_file} = {result}")
# Завдання 3
"""
    Є текстовий файл. Видаліть з нього останній рядок
"""
with open("test.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()


lines = lines[:-1]

with open("test.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)
