# Завдання 1
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Ім’я: {self.name}, вік: {self.age}")


students = []

for i in range(3):
    name = input("Введіть ім’я: ")
    age = int(input("Введіть вік: "))

    s = Student(name, age)
    students.append(s)

print("Інформація про студентів:")

for student in students:
    student.show_info()
