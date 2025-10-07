from abc import ABC, abstractmethod


class BaseZone(ABC):
    def __init__(self, code: str, volume: int):
        self.code = code
        self.volume = volume
        self.ships = []

    @property
    def code(self) -> str:
        return self._code

    @code.setter
    def code(self, value: str):
        if not value.isdigit():
            raise ValueError("Zone code must contain digits only!")
        self._code = value

    def get_ships(self):
        return sorted(self.ships, key=lambda ship: (-ship.hit_strength, ship.name))

    @abstractmethod
    def zone_info(self):
        pass
