# # # Завдання 1
# a = int(input("Введіть перше число"))
#
# b = int(input("Введіть друге число"))
# result = 0
# for i in range(a,b):
#     result += i
# print(f"Сума діапазону чисел: {result}")
#
# # Завдання 2
# result = 0
# for a in range(1,100):
#     if a % 2 == 0:
#
#         result += a
# print(f"Сума всіх парних чисел від 1 до 100: {result}")
#
# # Завдання 3
#
# word = input("Введіть рядок")
#
# for a in word:
#     print(a)
#
# # Завдання 4
#
# numbers = [1, 2, 3, 4, 5]
# result = []
#
# for num in numbers:
#     if num % 2 == 0:
#         result.append(num)
#
# print(f"Cписок який містить лише парні числа: {result}")

# Завдання 5
words = [
    "Hello",
    "world",
    "Python",
    "java",
    "ChatGPT",
    "code",
    "Apple",
    "banana",
    "Moscow",
    "street",
]


def filter_capitalized_words(list):
    result = []
    for a in list:
        if a[0].isupper():
            result.append(a)

    return result


result = filter_capitalized_words(words)
print(result)

# Завдання 6

words = [
    "Hello",
    "world",
    "Python",
    "java",
    "ChatGPT",
    "codePython",
    "Apple",
    "banana PyThon",
    "Moscow",
    "street",
]


def get_python_words(list):
    result = []

    for a in list:
        if "python" in a.lower():
            result.append(a)

    return result


result = get_python_words(words)
print(result)

# Завдання 7

dictionary = {
    "Python": "високорівнева мова програмування",
    "змінна": "ім’я, яке зберігає значення в пам’яті",
    "функція": "блок коду, який виконує певну задачу",
    "цикл": "конструкція для повторення дій",
    "список": "структура даних для зберігання кількох елементів",
    "словник": "структура даних у вигляді пар ключ-значення",
}

while True:
    operations = input(
        "1:  додати, 2: видаляти, 3: шукати слова у цьому словнику 4: Вихід"
    )

    if operations == "2":
        delete = input("Введіть слово для видалення")
        if delete in dictionary:
            dictionary.pop(delete)
        else:
            print("Такого слова не існує")

    elif operations == "1":
        word_name = input("Введіть слово для додавання його до словника")
        word_description = input("Введіть опис цього слова")
        dictionary[word_name] = word_description

    elif operations == "3":
        search_word = input("Введіть слово як хочете знайти").lower()

        if search_word in dictionary:
            print(f"Таке слово існує, ось его опис:{dictionary[search_word]}")

        else:
            print("Такого слова не існує")

    elif operations == "4":
        break
    else:
        print("Такої операції не існує, спробуйте ще раз")

# Частина 2: Об'єктно-орієнтоване програмування (ООП)


class WebPage:
    def __init__(self, title, content, date):
        self.title = title
        self.content = content
        self.date = date

    def show_details(self):
        print("Заголовок:", self.title)
        print("Вміст:", self.content)
        print("Дата:", self.date)


class WebSite:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.pages = []

    def add_page(self, page):
        self.pages.append(page)

    def remove_page(self, title):
        for page in self.pages:
            if page.title == title:
                self.pages.remove(page)
                print("Сторінку видалено")
                return
        print("Сторінку не знайдено")

    def show_info(self):
        print("Назва:", self.name)
        print("URL:", self.url)
        print("Кількість сторінок:", len(self.pages))

        print("СТОРІНКИ ")
        for page in self.pages:
            print("-", page.title)


site = None

while True:
    print("1 - Створити сайт")
    print("2 - Додати сторінку")
    print("3 - Видалити сторінку")
    print("4 - Показати сайт")
    print("5 - Вийти")

    choice = input("Вибір: ")

    if choice == "1":
        name = input("Назва сайту: ")
        url = input("URL сайту: ")
        site = WebSite(name, url)
        print("Сайт створено!")

    elif choice == "2":
        if site is None:
            print("Спочатку створіть сайт!")
            continue

        title = input("Заголовок сторінки: ")
        content = input("Вміст: ")
        date = input("Дата: ")

        page = WebPage(title, content, date)
        site.add_page(page)
        print("Сторінку додано!")

    elif choice == "3":
        if site is None:
            print("Спочатку створіть сайт!")
            continue

        title = input("Введіть назву сторінки для видалення: ")
        site.remove_page(title)

    elif choice == "4":
        if site is None:
            print("Спочатку створіть сайт!")
            continue

        site.show_info()

    elif choice == "5":
        break

    else:
        print("Невірна операція")
