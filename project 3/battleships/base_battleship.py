from abc import ABC, abstractmethod


class BaseBattleship(ABC):
    def __init__(self, name: str, health: int, hit_strength: int, ammunition: int):
        self.name = name
        self.health = health
        self.hit_strength = hit_strength
        self.ammunition = ammunition
        self.is_attacking = False
        self.is_available = True

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value.isalpha():
            raise ValueError("Ship name must contain only letters!")
        self._name = value

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int):
        self._health = max(value, 0)

    @abstractmethod
    def attack(self):
        pass

    def take_damage(self, enemy_battleship: 'BaseBattleship'):
        self.health -= enemy_battleship.hit_strength
