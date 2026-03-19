import random
# Завдання 1

users_balance = {'Влад': 123}


def ask_value(balance, message):

    while True:
        value = int(input(message))
        if value < 1:
            print('Сума повинна будти більшою за 0')

        elif value > balance:
            print('Недостатньо коштів на вашому рахунку')
        else:
            return value


def add_balance(balance):
    user_name = input("Введіть ім'я користувача")

    if user_name in users_balance:
        value = ask_value(balance,'Введіть суму для поповнення: ')
        balance -= value
        users_balance[user_name] += value

    else:
        print('Доданий новий користувач')
        value = ask_value(balance)
        balance -= value
        users_balance[user_name] = value

    print(f'Рахунок користувача {user_name} поповненно на {value} ваш балан {balance}')
    return balance


def reduce_balance(balance):
    user_name = input("Введіть ім'я користувача")
    if user_name not in users_balance:
        print('Такого користувача не існує')
    else:
        value = ask_value(balance, 'Введіть суму для зняття: ')
        balance += value
        users_balance[user_name] -= value

    print(f'Ви зняли з рахунку {user_name} суму {value} ваш баланс {balance}')
    return balance


def main():
    balance = int(input('Введіть ваш баланс'))
    operation = input('Виберіть операцію: 1 Поповнити баланс. 2 Зняти гроші')

    if operation == '1':
        balance = add_balance(balance)

    elif operation == '2':
        balance = reduce_balance(balance)
    print('Дякую що скористалися нашим банком)')
    return balance


result = main()
print(result, users_balance)