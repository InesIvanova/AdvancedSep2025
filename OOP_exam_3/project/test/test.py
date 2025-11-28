from project.gallery import Gallery
from unittest import TestCase, main

class TestGallery(TestCase):
    def setUp(self):
        self.gallery = Gallery("Valid", "Sofia", 20, False)

    def test_init(self):
        self.assertEqual("Valid", self.gallery.gallery_name)
        self.assertEqual("Sofia", self.gallery.city)
        self.assertEqual(20, self.gallery.area_sq_m)
        self.assertFalse(self.gallery.open_to_public)
        self.assertEqual({}, self.gallery.exhibitions)

    def test_invalid_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            Gallery("", "Sofia", 20, False)
        self.assertEqual("Gallery name can contain letters and digits only!", str(ex.exception))


        with self.assertRaises(ValueError) as ex:
            Gallery("S16!ha", "Sofia", 20, False)
        self.assertEqual("Gallery name can contain letters and digits only!", str(ex.exception))

    def test_invalid_city_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            Gallery("Valid", "4Sofia", 20, False)
        self.assertEqual("City name must start with a letter!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            Gallery("Valid", "!Sofia", 20, False)
        self.assertEqual("City name must start with a letter!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            Gallery("Valid", "", 20, False)
        self.assertEqual("City name must start with a letter!", str(ex.exception))

    def test_invalid_sq_m_raises(self):
        with self.assertRaises(ValueError) as ex:
            Gallery("Valid", "Sofia", 0.0, False)
        self.assertEqual("Gallery area must be a positive number!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            Gallery("Valid", "Sofia", -1, False)
        self.assertEqual("Gallery area must be a positive number!", str(ex.exception))

    def test_add_exhibition_name_exist(self):
        self.gallery.exhibitions = {"a": 2023}
        result = self.gallery.add_exhibition("a", 2002)
        self.assertEqual(f'Exhibition "a" already exists.', result)
        self.assertEqual(2023, self.gallery.exhibitions["a"])

    def test_add_exhibition_name_not_exist(self):
        self.gallery.exhibitions = {"a": 2023}
        result = self.gallery.add_exhibition("b", 2002)
        self.assertEqual(f'Exhibition "b" added for the year 2002.', result)
        self.assertEqual({"a": 2023, "b": 2002}, self.gallery.exhibitions)

    def test_remove_exhibition_does_not_exist(self):
        self.gallery.exhibitions = {"a": 2023}
        result = self.gallery.remove_exhibition("b")
        self.assertEqual(f'Exhibition "b" not found.', result)

    def test_remove_exhibition(self):
        self.gallery.exhibitions = {"a": 2023, "b": 2002}
        result = self.gallery.remove_exhibition("a")
        self.assertEqual(f'Exhibition "a" removed.', result)
        self.assertEqual({"b": 2002}, self.gallery.exhibitions)

    def test_list_exhibitions_open(self):
        self.gallery.open_to_public = True
        self.gallery.exhibitions = {"a": 2023, "b": 2002}
        result = self.gallery.list_exhibitions()
        self.assertEqual(f"a: 2023\nb: 2002", result)

    def test_list_exhibitions_closed(self):
        self.gallery.exhibitions = {"a": 2023, "b": 2002}
        result = self.gallery.list_exhibitions()
        self.assertEqual(f"Gallery {self.gallery.gallery_name} is currently closed for public! Check for updates later on.", result)

if __name__ == '__main__':
    main()
