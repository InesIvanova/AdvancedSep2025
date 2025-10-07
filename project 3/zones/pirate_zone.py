from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    INITIAL_VOLUME = 8

    def __init__(self, code: str):
        super().__init__(code, self.INITIAL_VOLUME)

        # add a custom property to avoid type checking
        self.zone_type = 'PirateZone'

    def zone_info(self):
        ship_list = self.get_ships()
        total_ships = len(ship_list)
        royal_ships = sum(1 for ship in ship_list if ship.ship_type == 'RoyalBattleship')
        ship_names = ', '.join(ship.name for ship in ship_list) if ship_list else ''

        result = (f"@Pirate Zone Statistics@\n"
                  f"Code: {self.code}; Volume: {self.volume}\n"
                  f"Battleships currently in the Pirate Zone: {total_ships}, "
                  f"{royal_ships} out of them are Royal Battleships.")

        return result + f"\n#{ship_names}#" if ship_names else result
