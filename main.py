from datetime import datetime


# Завдання 1


class Message:
    def __init__(self, user, text, time_str):
        self.user = user
        self.text = text
        self.time = datetime.strptime(time_str, "%H:%M")

    def __str__(self):
        return f"{self.user}: {self.text} ({self.time.strftime('%H:%M')})"

    def __len__(self):
        return len(self.text)

    def __gt__(self, other):
        return self.time > other.time


messages = [
    Message("Ivan", "Привіт", "10:23"),
    Message("Oleg", "Як справи?", "09:15"),
    Message("Anna", "Все добре!", "11:05"),
]

print("До сортування:")
for mess in messages:
    print(mess)

messages.sort()

print("Після сортування:")
for mess in messages:
    print(mess)


# Завдання 2


class Song:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __eq__(self, other):
        if not isinstance(other, Song):
            return False
        return self.name == other.name and self.author == other.author

    def __str__(self):
        return f"{self.name} - {self.author}"


class Playlist:
    def __init__(self):
        self.songs = []

    def __len__(self):
        return len(self.songs)

    def __contains__(self, item):
        if not isinstance(item, Song):
            return False
        return item in self.songs

    def __iter__(self):
        return iter(self.songs)

    def add_song(self, song):
        if not isinstance(song, Song):
            raise TypeError("Можна додавати тільки об'єкти Song")
        self.songs.append(song)

    def remove_song(self, song):
        if not isinstance(song, Song):
            raise TypeError("Можна видаляти тільки об'єкти Song")
        if song in self.songs:
            self.songs.remove(song)


playlist = Playlist()

song1 = Song("Imagine", "John Lennon")
song2 = Song("Bohemian Rhapsody", "Queen")
song3 = Song("Shape of You", "Ed Sheeran")

playlist.add_song(song1)
playlist.add_song(song2)
playlist.add_song(song3)

for song in playlist:
    print(song)


# Завдання 3


class Cart:
    def __init__(self):
        self.items = []
        self.total = 0

    def __str__(self):
        return f"Товари: {', '.join(self.items)} | Сума: {self.total}"

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        if not isinstance(other, Cart):
            raise TypeError("Можна об'єднувати тільки Cart")

        new_cart = Cart()
        new_cart.items = self.items + other.items
        new_cart.total = self.total + other.total
        return new_cart

    def add_item(self, item, price):
        self.items.append(item)
        self.total += price


cart1 = Cart()
cart2 = Cart()

cart1.add_item("Хліб", 20)
cart1.add_item("Молоко", 30)

cart2.add_item("Сир", 50)
cart2.add_item("Яблука", 40)

print(len(cart1))
print(len(cart2))

print(cart1)
print(cart2)

cart3 = cart1 + cart2

print(len(cart3))
print(cart3)
