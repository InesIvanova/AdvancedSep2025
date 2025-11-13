class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


from unittest import TestCase, main

class CarTests(TestCase):
    def test_init(self):
        c = Car("test make", 'test model', 20, 100)
        self.assertEqual("test make", c.make)
        self.assertEqual("test model", c.model)
        self.assertEqual(20, c.fuel_consumption)
        self.assertEqual(100, c.fuel_capacity)
        self.assertEqual(0, c.fuel_amount)

        c.fuel_amount = 20
        self.assertEqual(20, c.fuel_amount)

    def test_make_empty_raises(self):
        with self.assertRaises(Exception) as ex:
            Car(None, "test model", 20, 100)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            Car("", "test model", 20, 100)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_empty_raises(self):
        with self.assertRaises(Exception) as ex:
            Car("test make", None, 20, 100)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            Car("test make", "", 20, 100)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_zero_or_less_raises(self):
        with self.assertRaises(Exception) as ex:
            Car("test make", "test model", -1, 100)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            Car("test make", "test model", 0, 100)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_zero_or_less_raises(self):
        with self.assertRaises(Exception) as ex:
            Car("test make", "test model", 20, -1)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            Car("test make", "test model", 20, 0)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_less_thn_zero_raises(self):
        c = Car("test make", "test model", 20, 100)
        self.assertEqual(0, c.fuel_amount)
        with self.assertRaises(Exception) as ex:
            c.fuel_amount = -10
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))
        self.assertEqual(0, c.fuel_amount)

    def test_refuel_fuel_zero_or_less_raises(self):
        c = Car("test make", "test model", 20, 100)

        with self.assertRaises(Exception) as ex:
            c.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            c.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_within_capcity(self):
        c = Car("test make", "test model", 20, 100)
        c.fuel_amount = 20
        self.assertEqual(20, c.fuel_amount)

        c.refuel(20)

        self.assertEqual(40, c.fuel_amount)

    def test_refuel_above_capacity(self):
        c = Car("test make", "test model", 20, 100)
        c.fuel_amount = 20
        self.assertEqual(20, c.fuel_amount)

        c.refuel(81)

        self.assertEqual(100, c.fuel_amount)

    def test_drive_above_available_fuel_raises(self):
        c = Car("test make", "test model", 20, 100)
        c.fuel_amount = 199
        self.assertEqual(199, c.fuel_amount)
        with self.assertRaises(Exception) as ex:
            c.drive(1000)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))
        self.assertEqual(199, c.fuel_amount)

    def test_drive_exact_fuel_amount(self):
        c = Car("test make", "test model", 20, 100)
        c.fuel_amount = 200
        self.assertEqual(200, c.fuel_amount)
        c.drive(1000)
        self.assertEqual(0, c.fuel_amount)

        c.fuel_amount = 201
        self.assertEqual(201, c.fuel_amount)
        c.drive(1000)
        self.assertEqual(1, c.fuel_amount)


if __name__ == '__main__':
    main()