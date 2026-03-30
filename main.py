# Завдання 1


def ask_password():
    password = input("Введіть пароль: ")

    if len(password) < 8:
        raise ValueError("Пароль має містити не менше 8 символів")

    if len(set(password)) == 1:
        raise ValueError("Пароль не може складатися з однакових символів")

    return password


try:
    user_password = ask_password()
    print("Пароль прийнято:", user_password)
except ValueError as e:
    print("Помилка:", e)


# Завдання 2
users_info = {"user1": "password123", "admin": "qwerty456", "guest": "guest000"}


def ask_login_password():
    user_login = input("Введіть логін")

    if user_login not in users_info:
        raise ValueError("Такого логіну не існує")

    user_password = input("Введіть пароль")

    if user_password != users_info[user_login]:
        raise ValueError("Такого паролю не існує")

    return user_password, user_login


try:
    result = ask_login_password()
    print("Логін та пароль прийнято:", result)
except ValueError as e:
    print("Помилка:", e)
