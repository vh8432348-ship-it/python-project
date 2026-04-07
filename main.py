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
