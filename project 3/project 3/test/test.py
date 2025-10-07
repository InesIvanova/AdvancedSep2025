from project.furniture import Furniture
import unittest


class TestFurniture(unittest.TestCase):

    def test_valid_initialization__default_values(self):
        furniture = Furniture("Table", 199.99, (80, 120, 60))
        self.assertEqual(furniture.model, "Table")
        self.assertEqual(furniture.price, 199.99)
        self.assertEqual(furniture.dimensions, (80, 120, 60))
        self.assertTrue(furniture.in_stock)
        self.assertIsNone(furniture.weight)

    def test_valid_initialization__with_passed_values(self):
        furniture = Furniture("T" * 50, 0.00, (80, 120, 60), False, 15.5)
        self.assertEqual(furniture.model, "T" * 50)
        self.assertEqual(furniture.price, 0.00)
        self.assertEqual(furniture.dimensions, (80, 120, 60))
        self.assertFalse(furniture.in_stock)
        self.assertEqual(furniture.weight, 15.5)

    def test_invalid_model__empty_string(self):
        with self.assertRaises(ValueError) as err:
            Furniture("", 199.99, (80, 120, 60))
        self.assertEqual(str(err.exception), "Model must be a non-empty string with a maximum length of 50 characters.")

        with self.assertRaises(ValueError) as err:
            Furniture(" " * 50, 199.99, (80, 120, 60))
        self.assertEqual(str(err.exception), "Model must be a non-empty string with a maximum length of 50 characters.")

    def test_invalid_model__more_than_50(self):
        with self.assertRaises(ValueError) as err:
            Furniture("A" * 51, 199.99, (80, 120, 60))
        self.assertEqual(str(err.exception), "Model must be a non-empty string with a maximum length of 50 characters.")

    def test_invalid_price(self):
        with self.assertRaises(ValueError) as err:
            Furniture("Chair", -0.01, (80, 120, 60))
        self.assertEqual(str(err.exception), "Price must be a non-negative number.")

    def test_invalid_dimensions__less_than_3_elements(self):
        with self.assertRaises(ValueError) as err:
            Furniture("Chair", 199.99, (80, 120))
        self.assertEqual(str(err.exception), "Dimensions tuple must contain 3 integers.")

    def test_invalid_dimensions__negative_value_elements(self):
        with self.assertRaises(ValueError) as err:
            Furniture("Chair", 199.99, (80, 120, -1))
        self.assertEqual(str(err.exception), "Dimensions tuple must contain integers greater than zero.")

    def test_invalid_dimensions__zero_value_elements(self):
        with self.assertRaises(ValueError) as err:
            Furniture("Chair", 199.99, (80, 0, 60))
        self.assertEqual(str(err.exception), "Dimensions tuple must contain integers greater than zero.")

        with self.assertRaises(ValueError) as err:
            Furniture("Chair", 199.99, (0, 0, 0))
        self.assertEqual(str(err.exception), "Dimensions tuple must contain integers greater than zero.")

    def test_invalid_weight__negative(self):
        furniture = Furniture("Chair", 199.99, (80, 120, 60))
        with self.assertRaises(ValueError) as err:
            furniture.weight = -0.01
        self.assertEqual(str(err.exception), "Weight must be greater than zero.")

    def test_invalid_weight__zero(self):
        furniture = Furniture("Chair", 199.99, (80, 120, 60))
        with self.assertRaises(ValueError) as err:
            furniture.weight = 0.00
        self.assertEqual(str(err.exception), "Weight must be greater than zero.")

    def test_valid_weight__passing_None(self):
        furniture = Furniture("Chair", 199.99, (80, 120, 60), in_stock=True, weight=None)
        self.assertIsNone(furniture.weight)

    def test_valid_get_available_status__available(self):
        furniture = Furniture("Chair", 199.99, (80, 120, 60))
        self.assertEqual(furniture.get_available_status(), "Model: Chair is currently in stock.")

    def test_valid_get_available_status__unavailable(self):
        furniture = Furniture("Chair", 199.99, (80, 120, 60), in_stock=False)
        self.assertEqual(furniture.get_available_status(), "Model: Chair is currently unavailable.")

    def test_valid_get_specifications__with_weight(self):
        furniture = Furniture("Chair", 199.99, (80, 120, 60), True, 15.5)
        self.assertEqual(furniture.get_specifications(),
                         "Model: Chair has the following dimensions: 80mm x 120mm x 60mm and weighs: 15.5")

    def test_valid_get_specifications__no_weight(self):
        furniture = Furniture("Chair", 199.99, (80, 120, 60), True, weight=None)
        self.assertEqual(furniture.get_specifications(),
                         "Model: Chair has the following dimensions: 80mm x 120mm x 60mm and weighs: N/A")


if __name__ == '__main__':
    unittest.main()

