from project.battleships.base_battleship import BaseBattleship


class RoyalBattleship(BaseBattleship):
    INITIAL_AMMUNITION = 100
    DECREASE_AMMUNITION = 25

    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, self.INITIAL_AMMUNITION)

        # add a custom property to avoid type checking
        self.ship_type = 'RoyalBattleship'

    def attack(self):
        self.ammunition = max(0, (self.ammunition - self.DECREASE_AMMUNITION))
