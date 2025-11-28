from project.clients.base_client import BaseClient
from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient
from project.plants.base_plant import BasePlant
from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant


flower_mapper = {"Flower": Flower, "LeafPlant": LeafPlant}
client_mapper = {"RegularClient": RegularClient, "BusinessClient": BusinessClient}


class FlowerShopManager:
    def __init__(self):
        self.income = 0.0
        self.plants: list[BasePlant] = []
        self.clients: list[BaseClient] = []

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str):
        if plant_type not in flower_mapper:
            raise ValueError(f"Unknown plant type!")
        plant = flower_mapper[plant_type](plant_name, plant_price, plant_water_needed, plant_extra_data)
        self.plants.append(plant)
        return f"{plant_name} is added to the shop as {plant_type}."

    def filter_client(self, phone_numer) -> BaseClient:
        return next((client for client in self.clients if client.phone_number == phone_numer), None)

    def filter_plants(self, name):
        return [plant for plant in self.plants if plant.name == name]

    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        if client_type not in client_mapper:
            raise ValueError(f"Unknown client type!")
        client = self.filter_client(client_phone_number)
        if client is not None:
            raise ValueError("This phone number has been used!")
        client = client_mapper[client_type](client_name, client_phone_number)
        self.clients.append(client)
        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        client = self.filter_client(client_phone_number)
        if client is None:
            raise ValueError("Client not found!")
        plants = self.filter_plants(plant_name)
        if not plants:
            raise ValueError("Plants not found!")

        if len(plants) < plant_quantity:
            return "Not enough plant quantity."

        current_sale = 0.0
        for index in range(plant_quantity):
            current_plant= plants[index]
            self.plants.remove(current_plant)
            discount = client.discount / 100
            current_sale += (current_plant.price - current_plant.price * discount)

        self.income += current_sale
        client.update_total_orders()
        client.update_discount()

        return f"{plant_quantity}pcs. of {plant_name} plant sold for {current_sale:.2f}"



    def remove_plant(self, plant_name: str):
        plants = self.filter_plants(plant_name)
        if not plants:
            return "No such plant name."
        plant_to_remove = plants[0]
        self.plants.remove(plant_to_remove)
        return f"Removed {plant_to_remove.plant_details()}"

    def remove_clients(self):
        no_orders_clients = [client for client in self.clients if client.total_orders == 0]

        for index in range(len(no_orders_clients)):
            self.clients.remove(no_orders_clients[index])
        return f"{len(no_orders_clients)} client/s removed."

    def shop_report(self):
        result = []
        flowers_count = {}
        for flower in self.plants:
            flowers_count[flower.name] =  len(self.filter_plants(flower.name))
        sorted_flowers_count = sorted(flowers_count.items(), key=lambda kvp: (-kvp[1], kvp[0]))
        sorted_clients = sorted(self.clients, key=lambda client: (-client.total_orders, client.phone_number))

        all_orders = sum([client.total_orders for client in self.clients])
        result.append(f"~Flower Shop Report~\nIncome: {self.income:.2f}\nCount of orders: {all_orders}\n~~Unsold plants: {len(self.plants)}~~")
        for plant_name, plant_count in sorted_flowers_count:
            result.append(f"{plant_name}: {plant_count}")

        result.append(f"~~Clients number: {len(self.clients)}~~")
        for client in sorted_clients:
            result.append(client.client_details())

        return "\n".join(result)
