# Завдання 1


class Pet:
    def __init__(self, name: str, satiety: int = 50, energy: int = 50):
        self.__name = name
        self.__satiety = satiety
        self.__energy = energy

    def get_name(self):
        return self.__name

    def get_satiety(self):
        return self.__satiety

    def get_energy(self):
        return self.__energy

    def set_satiety(self, value):
        self.__satiety = max(0, min(100, value))

    def set_energy(self, value):
        self.__energy = max(0, min(100, value))

    def sleep(self):
        self.__energy = 100

    def eat(self, food_amount: int):
        self.set_satiety(self.__satiety + food_amount)

    def play(self, activity_level: int):
        pass

    def make_sound(self):
        pass


class Cat(Pet):
    def play(self, activity_level: int):
        if self.get_satiety() > 60:
            self.set_energy(self.get_energy() - 2 * activity_level)
            self.set_satiety(self.get_satiety() - activity_level)

    def make_sound(self):
        print("Мяу")

    def catch_mouse(self):
        if self.get_energy() > 30:
            if self.get_satiety() > 40:
                print(f"{self.get_name()} грається з мишею 🐭")
            else:
                print(f"{self.get_name()} з’їв мишу 🐭")
                self.set_satiety(self.get_satiety() + 20)


class Dog(Pet):
    def play(self, activity_level: int):
        if self.get_satiety() > 15:
            self.set_energy(self.get_energy() - activity_level // 2)
            self.set_satiety(self.get_satiety() - activity_level // 2)

    def make_sound(self):
        print("Гав")

    def fetch_ball(self):
        if self.get_satiety() > 10:
            print(f"{self.get_name()} приніс м’яч 🎾")
            self.set_energy(self.get_energy() - 5)


cat = Cat("Барсик")
dog = Dog("Рекс")

cat.play(10)
cat.catch_mouse()
cat.make_sound()

dog.play(10)
dog.fetch_ball()
dog.make_sound()

print(f"{cat.get_name()}: ситість={cat.get_satiety()}, енергія={cat.get_energy()}")
print(f"{dog.get_name()}: ситість={dog.get_satiety()}, енергія={dog.get_energy()}")
