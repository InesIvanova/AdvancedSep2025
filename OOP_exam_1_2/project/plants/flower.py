from project.plants.base_plant import BasePlant


class Flower(BasePlant):
    SEASONS = ["Spring", "Summer", "Fall", "Winter"]

    def __init__(self, name: str, price: float, water_needed: int, blooming_season: str):
        super().__init__(name, price, water_needed)
        self.blooming_season = blooming_season

    @property
    def blooming_season(self):
        return self.__blooming_season

    @blooming_season.setter
    def blooming_season(self, value):
        if value not in self.SEASONS:
            raise ValueError(f"Blooming season must be a valid one!")
        self.__blooming_season = value

    def plant_details(self):
        result = super().plant_details()
        return f"Flower: {result} Blooming Season: {self.blooming_season}"