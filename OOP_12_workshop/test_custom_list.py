from unittest import TestCase, main

from OOP_12_workshop.custom_list import CustomList



class CustomListTests(TestCase):
    def setUp(self):
        self.custom_list = CustomList(100,2, -5, 15, 2)
    def test_init(self):
        cl = CustomList(1, 2, 3)
        self.assertEqual([1, 2, 3], cl._CustomList__data)

    def test_add(self):
        self.assertEqual([100,2, -5, 15, 2], self.custom_list._CustomList__data)

        result = self.custom_list.append(5)

        self.assertEqual([100,2, -5, 15, 2, 5], self.custom_list._CustomList__data)
        self.assertEqual([100,2, -5, 15, 2, 5], result)

    def test_get_elements(self):
        self.assertEqual([100,2, -5, 15, 2], self.custom_list.get_elements())

    def test_remove(self):
        self.assertEqual([100, 2, -5, 15, 2], self.custom_list.get_elements())

        result = self.custom_list.remove(1)
        self.assertEqual([100, -5, 15, 2], self.custom_list.get_elements())
        self.assertEqual(2, result)

    def test_get(self):
        self.assertEqual([100, 2, -5, 15, 2], self.custom_list.get_elements())

        result = self.custom_list.get(1)
        self.assertEqual([100, 2, -5, 15, 2], self.custom_list.get_elements())
        self.assertEqual(2, result)

    def test_extend(self):
        self.assertEqual([100, 2, -5, 15, 2], self.custom_list.get_elements())

        result = self.custom_list.extend([8, 9, 10, 11])
        self.assertEqual([100, 2, -5, 15, 2, 8, 9, 10, 11], self.custom_list.get_elements())
        self.assertEqual([100, 2, -5, 15, 2, 8, 9, 10, 11], result)

    def test_insert(self):
        self.assertEqual([100, 2, -5, 15, 2], self.custom_list.get_elements())

        result = self.custom_list.insert(2, 15)

        self.assertEqual([100, 2, 15, -5, 15, 2], self.custom_list.get_elements())
        self.assertEqual([100, 2, 15, -5, 15, 2], result)

    def test_pop(self):
        self.assertEqual([100, 2, -5, 15, 2], self.custom_list.get_elements())

        result = self.custom_list.pop()

        self.assertEqual([100, 2, -5, 15], self.custom_list.get_elements())

        self.assertEqual(2, result)

    def test_clear(self):
        self.assertEqual([100, 2, -5, 15, 2], self.custom_list.get_elements())

        result = self.custom_list.clear()
        self.assertEqual([], self.custom_list.get_elements())
        self.assertEqual([], self.custom_list._CustomList__data)
        self.assertIsNone(result)

    def test_index(self):
        self.assertEqual([100, 2, -5, 15, 2], self.custom_list.get_elements())

        result = self.custom_list.index(2)
        self.assertEqual([100, 2, -5, 15, 2], self.custom_list.get_elements())
        self.assertEqual(1, result)

    def test_count(self):
        self.assertEqual([100, 2, -5, 15, 2], self.custom_list.get_elements())

        result = self.custom_list.count(2)
        self.assertEqual([100, 2, -5, 15, 2], self.custom_list.get_elements())
        self.assertEqual(2, result)

    def test_reverse(self):
        self.assertEqual([100, 2, -5, 15, 2], self.custom_list.get_elements())

        result = self.custom_list.reverse()

        self.assertEqual([100, 2, -5, 15, 2], self.custom_list.get_elements())
        self.assertEqual([2, 15, -5, 2, 100], result)

    def test_copy(self):
        self.assertEqual([100, 2, -5, 15, 2], self.custom_list.get_elements())

        result = self.custom_list.copy()
        self.assertEqual([100, 2, -5, 15, 2], self.custom_list.get_elements())
        self.assertEqual([100, 2, -5, 15, 2], result)

        self.assertNotEqual(id(self.custom_list.get_elements()), id(result))

    def test_size(self):
        self.assertEqual([100, 2, -5, 15, 2], self.custom_list.get_elements())

        result = self.custom_list.size()

        self.assertEqual([100, 2, -5, 15, 2], self.custom_list.get_elements())
        self.assertEqual(5, result)

    def test_add_first(self):
        self.assertEqual([100, 2, -5, 15, 2], self.custom_list.get_elements())
        result = self.custom_list.add_first(2)
        self.assertEqual([2, 100, 2, -5, 15, 2], self.custom_list.get_elements())
        self.assertIsNone(result)

    def test_dictionize(self):
        self.assertEqual([100, 2, -5, 15, 2], self.custom_list.get_elements())

        result = self.custom_list.dictionize()
        self.assertEqual([100, 2, -5, 15, 2], self.custom_list.get_elements())
        self.assertEqual({100: 2, -5: 15, 2: " "}, result)

        cl = CustomList(1, 2, 3, 4)
        result = cl.dictionize()
        self.assertEqual({1: 2, 3: 4}, result)

    def test_move(self):
        self.assertEqual([100, 2, -5, 15, 2], self.custom_list.get_elements())

        result = self.custom_list.move(2)
        self.assertEqual([100, 2, -5, 15, 2], self.custom_list.get_elements())
        self.assertEqual([-5, 15, 2, 100, 2], result)

    def test_sum(self):
        cl = CustomList(1, [1, 2], "asd", 100)

        result = cl.sum()

        self.assertEqual(106, result)

    def test_overbound(self):
        cl = CustomList(1, "asd", [1, 2])

        result = cl.overbound()
        self.assertEqual(1, result)

    def test_underbound(self):
        cl = CustomList( "asdc", 2, [1, 2, 3])
        result = cl.underbound()
        self.assertEqual(1, result)


if __name__ == '__main__':
    main()