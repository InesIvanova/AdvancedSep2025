from project.battleships.base_battleship import BaseBattleship


class PirateBattleship(BaseBattleship):
    INITIAL_AMMUNITION = 80
    DECREASE_AMMUNITION = 10

    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, self.INITIAL_AMMUNITION)

        # add a custom property to avoid type checking
        self.ship_type = 'PirateBattleship'

    def attack(self):
        self.ammunition = max(0, (self.ammunition - self.DECREASE_AMMUNITION))
