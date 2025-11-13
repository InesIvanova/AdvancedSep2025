class Cat:

  def __init__(self, name):
    self.name = name
    self.fed = False
    self.sleepy = False
    self.size = 0

  def eat(self):
    if self.fed:
      raise Exception('Already fed.')

    self.fed = True
    self.sleepy = True
    self.size += 1

  def sleep(self):
    if not self.fed:
      raise Exception('Cannot sleep while hungry')

    self.sleepy = False


from unittest import TestCase, main

class CatTests(TestCase):
    def test_init(self):
        c = Cat("Lady")
        self.assertEqual("Lady", c.name)
        self.assertFalse(c.fed)
        self.assertFalse(c.sleepy)
        self.assertEqual(0, c.size)

    def test_eat(self):
        c = Cat("Lady")

        self.assertFalse(c.fed)
        self.assertFalse(c.sleepy)
        self.assertEqual(0, c.size)

        c.eat()

        self.assertTrue(c.fed)
        self.assertTrue(c.sleepy)
        self.assertEqual(1, c.size)

    def test_cat_is_fet_raises(self):
        c = Cat("Lady")
        c.fed = True
        self.assertTrue(c.fed)
        self.assertEqual(0, c.size)

        with self.assertRaises(Exception) as ex:
            c.eat()
        self.assertEqual("Already fed.", str(ex.exception))

        self.assertTrue(c.fed)
        self.assertEqual(0, c.size)

    def test_cat_is_hungry_sleep_raises(self):
        c = Cat("Lady")
        self.assertFalse(c.fed)
        self.assertFalse(c.sleepy)
        self.assertEqual(0, c.size)

        with self.assertRaises(Exception) as ex:
            c.sleep()
        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

        self.assertFalse(c.fed)
        self.assertFalse(c.sleepy)
        self.assertEqual(0, c.size)

    def test_cat_is_fed(self):
        c = Cat("Lady")
        c.eat()

        self.assertTrue(c.sleepy)

        c.sleep()

        self.assertFalse(c.sleepy)



if __name__ == '__main__':
    main()