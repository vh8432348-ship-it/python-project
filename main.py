# Завдання 1
"""

Є словник з курсами валют, де ключ – назва валюти,
значення – курс до гривні. Користувач вводить назву валюти,
суму та назву нової валюти, в яку треба перевести суму
"""

rates = {"гривня": 1, "долар": 40, "євро": 43, "злотий": 10}

from_currency = input("Введіть валюту: ").lower()
amount = float(input("Введіть суму: "))
to_currency = input("У яку валюту перевести: ").lower()

amount_uah = amount * rates[from_currency]

result = amount_uah / rates[to_currency]

print("Результат:", result)

# Завдання 2

"""
Напишіть функцію, яка отримує 2 множини з іменами
працівників, які працюють в офісі та віддалено. Виведіть на
екран:
 Імена усіх працівників
 Імена працівників, які працюють і в офісі, і віддалено
 Відсоток працівників, які працюють і в офісі, і
віддалено
"""


def workers_info(office, remote):
    all_workers = office | remote
    print("Усі працівники:", all_workers)

    both = office & remote
    print("Працюють і в офісі і віддалено:", both)

    percent = len(both) / len(all_workers) * 100
    print("Відсоток:", round(percent, 2), "%")


office = {"Іван", "Оля", "Петро", "Марія"}
remote = {"Оля", "Марія", "Сергій"}

workers_info(office, remote)
