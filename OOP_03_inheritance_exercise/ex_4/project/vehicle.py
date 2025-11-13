class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, km):
        needed_fuel = (km * self.fuel_consumption)

        if self.fuel >= needed_fuel:
            self.fuel -= needed_fuel

rm = Vehicle(100, 2)