#!/usr/bin/python3
"""Testing Amenity"""

import models
from models.amenity import Amenity
import unittest


class Test_Amenity_instantiation(unittest.TestCase):
    """test for amenity instantiation"""

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_name_is_public_class_attribute(self):
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))


if __name__ == "__main__":
    unittest.main()