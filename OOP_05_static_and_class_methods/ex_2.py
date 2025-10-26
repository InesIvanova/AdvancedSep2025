


class Shop:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name, type):
        return cls(name, type, 10)

    def add_item(self, item_name):
        if sum(self.items.values()) < self.capacity:
            if item_name not in self.items:
                self.items[item_name] = 0
            self.items[item_name] += 1
            return f"{item_name} added to the shop"
        return "Not enough capacity in the shop"

    def remove_item(self, item_name, amount):
        if item_name not in self.items:
            return f"Cannot remove {amount} {item_name}"

        if amount > self.items[item_name]:
            return f"Cannot remove {amount} {item_name}"

        self.items[item_name] -= amount

        if self.items[item_name] == 0:
            del self.items[item_name]
        return f"{amount} {item_name} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"



import unittest

class ShopTests(unittest.TestCase):
    def test_add_item_unsuccessfully(self):
        shop = Shop("Little Candy", 'Candy Shop', 2)
        shop.add_item('Candy')
        shop.add_item('Candy')
        expected = shop.add_item('Candy')
        actual = 'Not enough capacity in the shop'
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()



