# Завдання 1
class Passenger:
    def __init__(self, name, destination):
        self.__name = name
        self.__destination = destination

    def get_name(self):
        return self.__name

    def get_destination(self):
        return self.__destination


# Завдання 2
class Transport:
    def __init__(self, speed):
        self.__speed = speed

    def get_speed(self):
        return self.__speed

    def move(self, destination, distance):
        time = distance / self.__speed
        print(f"Транспорт рухається до {destination}.")
        print(f"Час у дорозі: {time:.2f} год.")


# Завдання 3
class Bus(Transport):
    def __init__(self, speed, capacity):
        super().__init__(speed)
        self.__capacity = capacity
        self.__passengers = []

    def get_capacity(self):
        return self.__capacity

    def get_passengers(self):
        return self.__passengers

    def board_passenger(self, passenger):
        if len(self.__passengers) < self.__capacity:
            self.__passengers.append(passenger)
            print(f"{passenger.get_name()} сів(ла) в автобус.")
        else:
            print("Автобус заповнений!")

    def move(self, destination, distance):
        leaving_passengers = []

        for passenger in self.__passengers:
            if passenger.get_destination() == destination:
                leaving_passengers.append(passenger)

        for passenger in leaving_passengers:
            self.__passengers.remove(passenger)

        print(
            f"На зупинці '{destination}' вийшло "
            f"{len(leaving_passengers)} пасажир(ів)."
        )

        super().move(destination, distance)


p1 = Passenger("Іван", "Львів")
p2 = Passenger("Марія", "Київ")
p3 = Passenger("Олег", "Львів")

bus = Bus(speed=60, capacity=2)

bus.board_passenger(p1)
bus.board_passenger(p2)
bus.board_passenger(p3)

bus.move("Львів", 120)
