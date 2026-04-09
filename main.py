# Завдання 1


class Character:
    def __init__(
        self,
        name,
        max_hp,
        intelligence,
        strength,
        dexterity,
        mana,
        defense,
        level=1,
    ):
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp
        self._level = level
        self._intelligence = intelligence
        self._strength = strength
        self._dexterity = dexterity
        self._mana = mana
        self._defense = defense

    def attack(self):
        raise NotImplementedError("Метод attack потрібно перевизначити")

    def take_damage(self, damage):
        real_damage = damage - self._defense
        if real_damage < 0:
            real_damage = 0

        self._hp -= real_damage

        if self._hp < 0:
            self._hp = 0

    def level_up(self):
        if self._level < 20:
            self._level += 1

    def increase_stat(self, stat):
        if stat == "strength":
            self._strength += 1
        elif stat == "intelligence":
            self._intelligence += 1
        elif stat == "dexterity":
            self._dexterity += 1
        elif stat == "mana":
            self._mana += 1
        elif stat == "defense":
            self._defense += 1

    def rest(self):
        self._hp = self._max_hp

    def heal(self, heal_hp):
        self._hp += heal_hp
        if self._hp > self._max_hp:
            self._hp = self._max_hp

    def get_info(self):
        return f"{self._name} | HP: {self._hp}/{self._max_hp} | Level: {self._level}"


# Завдання 2


class Paladin(Character):
    def attack(self):
        if self._mana > 4:
            self._mana -= 5
            return self._strength * 4

        else:
            return self._strength

    def shield(self):
        self._defense += 4 + self._level

    def unshield(self):
        self._defense -= 4 + self._level

    def heal_ally(self, ally):
        heal_hp = 5 + 2 * self._level + 0.5 * self._mana
        ally.heal(heal_hp)
