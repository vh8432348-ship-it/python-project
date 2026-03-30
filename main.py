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
