from project.zones.royal_zone import RoyalZone
from project.zones.pirate_zone import PirateZone
from project.battleships.royal_battleship import RoyalBattleship
from project.battleships.pirate_battleship import PirateBattleship


class BattleManager:
    def __init__(self):
        self.zones = []
        self.ships = []

    def add_zone(self, zone_type: str, zone_code: str):
        zone_classes = {"RoyalZone": RoyalZone, "PirateZone": PirateZone}

        if zone_type not in zone_classes:
            raise Exception("Invalid zone type!")
        if any(zone.code == zone_code for zone in self.zones):
            raise Exception("Zone already exists!")

        zone = zone_classes[zone_type](zone_code)
        self.zones.append(zone)
        return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        ship_classes = {"RoyalBattleship": RoyalBattleship, "PirateBattleship": PirateBattleship}

        if ship_type not in ship_classes:
            raise Exception(f"{ship_type} is an invalid type of ship!")

        ship = ship_classes[ship_type](name, health, hit_strength)
        self.ships.append(ship)
        return f"A new {ship_type} was successfully added."

    @staticmethod
    def add_ship_to_zone(zone: 'BaseZone', ship: 'BaseBattleship'):
        if zone.volume <= 0:
            return f"Zone {zone.code} does not allow more participants!"
        if ship.health <= 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"
        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        if (ship.ship_type.startswith('Royal') and zone.zone_type.startswith('Royal')) \
                or (ship.ship_type.startswith('Pirate') and zone.zone_type.startswith('Pirate')):
            ship.is_attacking = True
        else:
            ship.is_attacking = False

        zone.ships.append(ship)
        ship.is_available = False
        zone.volume -= 1

        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):
        ship = next((s for s in self.ships if s.name == ship_name), None)
        if ship is None:
            return "No ship with this name!"
        if not ship.is_available:
            return "The ship participates in zone battles! Removal is impossible!"

        self.ships.remove(ship)
        return f"Successfully removed ship {ship_name}."

    def start_battle(self, zone: 'BaseZone'):
        attacker = max((ship for ship in zone.ships if ship.is_attacking), key=lambda s: s.hit_strength, default=None)
        enemy = max((ship for ship in zone.ships if not ship.is_attacking), key=lambda s: s.health, default=None)

        if not attacker or not enemy:
            return "Not enough participants. The battle is canceled."

        attacker.attack()
        enemy.take_damage(attacker)

        if enemy.health <= 0:
            zone.ships.remove(enemy)
            self.ships.remove(enemy)
            return f"{enemy.name} lost the battle and was sunk."

        if attacker.ammunition <= 0:
            zone.ships.remove(attacker)
            self.ships.remove(attacker)
            return f"{attacker.name} ran out of ammunition and leaves."

        return "Both ships survived the battle."

    def get_statistics(self):
        available_ships = [ship for ship in self.ships if ship.is_available]
        available_ships_str = ', '.join(ship.name for ship in available_ships) if available_ships else ''

        zones_info = '\n'.join(zone.zone_info() for zone in sorted(self.zones, key=lambda z: z.code))

        result = f"Available Battleships: {len(available_ships)}\n"
        result += f"#{available_ships_str}#\n" if available_ships else ''
        result += (f"***Zones Statistics:***\n"
                   f"Total Zones: {len(self.zones)}"
                   f"\n{zones_info}")
        return result.strip()
