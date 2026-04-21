from abc import ABC
from enum import Enum
from uuid import uuid4


# Завдання 1


class RobotStatus(Enum):
    ON = "on"
    OFF = "off"
    WORKING = "working"


class CleaningMode(Enum):
    DRY = "dry"
    WET = "wet"


class Robot(ABC):
    def __init__(self, name, battery_level=100):
        if name is None:
            name = str(uuid4())

        self._name = name
        self._battery_level = battery_level
        self._status = "off"

    def info(self):
        print(f"Name: {self._name}")
        print(f"Battery: {self._battery_level}%")
        print(f"Status: {self._status}")

    def charge(self):
        self._battery_level = 100
        print(f"{self._name} is fully charged.")

    def turn_on(self):
        self._status = "on"
        print(f"{self._name} is turned on.")

    def turn_off(self):
        self._status = "off"
        print(f"{self._name} is turned off.")


# Завдання 2


class CleaningRobot(Robot):
    def __init__(self, name, battery_level=100):
        super().__init__(name, battery_level)
        self._dust_capacity = 0
        self._water_capacity = 100
        self._cleaning_mode = CleaningMode.DRY

    def info(self):
        super().info()
        print(f"Dust: {self._dust_capacity}%")
        print(f"Water: {self._water_capacity}%")
        print(f"Mode: {self._cleaning_mode.value}")

    def turn_on(self):
        if self._dust_capacity >= 100:
            print("Cannot start: dust container is full!")
            return
        if self._water_capacity <= 0:
            print("Cannot start: water container is empty!")
            return

        super().turn_on()

    def empty_dustbin(self):
        self._dust_capacity = 0

    def fill_water(self):
        self._water_capacity = 100

    def swap_mode(self):
        if self._cleaning_mode == CleaningMode.DRY:
            self._cleaning_mode = CleaningMode.WET
        else:
            self._cleaning_mode = CleaningMode.DRY

    def clean(self, energy, dust, water=None):
        if self._battery_level < energy:
            print("Not enough battery!")
            return

        if self._cleaning_mode == CleaningMode.DRY:
            if self._dust_capacity + dust > 100:
                print("Error: dust container overflow!")
                return
            self._dust_capacity += dust

        else:
            if water is None:
                water = dust

            if self._dust_capacity + dust > 100:
                print("Error: dust container overflow!")
                return

            if self._water_capacity - water < 0:
                print("Error: not enough water!")
                return

            self._dust_capacity += dust
            self._water_capacity -= water

        self._battery_level -= energy
        self._status = RobotStatus.WORKING


# Завдання 3


class AlertLevel(Enum):
    low = "low"
    middle = "middle"
    high = "high"


class SecurityRobot(Robot):
    def __init__(self, name, battery_level=100):
        super().__init__(name, battery_level)

        self._min_speed = 5
        self._alert_level = AlertLevel.low
        self._dangerous_items = ["gun", "knife", "bat"]

    def info(self):
        super().info()
        print(f"Min speed: {self._min_speed}")
        print(f"Alert level: {self._alert_level.value}")
        print(f"Dangerous items: {self._dangerous_items}")

    def turn_off(self):
        self._alert_level = AlertLevel.low
        super().turn_off()

    def add_dangerous_item(self, item):
        if item not in self._dangerous_items:
            self._dangerous_items.append(item)

    def remove_dangerous_item(self, item):
        if item in self._dangerous_items:
            self._dangerous_items.remove(item)

    def detect(self, speed, item):
        if speed < self._min_speed:
            return

        if speed >= self._min_speed:
            if self._alert_level != AlertLevel.high:
                self._alert_level = AlertLevel.middle

        if item in self._dangerous_items:
            self._alert_level = AlertLevel.high
