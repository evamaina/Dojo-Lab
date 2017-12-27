import unittest

import os
import sys  # System-specific parameters and functions
import inspect
from person import Fellow, Staff
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)


sys.path.insert(0, parentdir)

# import sys  # System-specific parameters and functions
# from os import path
from person import Fellow, Staff

# sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


class PersonTestCases(unittest.TestCase):
    """
    Tests for the person class
    """
    def setUp(self):

        self.new_fellow = Fellow("Eva Johnson", 'Y')
        self.new_staff = Staff("Evet Maina", 'N')

        self.new_fellow = Fellow("Eva Johnson", "Y")
        self.new_staff = Staff("Evet Maina", "N")


    def test_staff_object(self):
        """
        Tests for the class person and their attributes
        """
        self.assertTrue(self.new_staff, "Evet Maina")
        self.assertEqual(self.new_staff.person_name, "Evet Maina")

        self.assertEqual(self.new_staff.wants_accomodation, 'N')

        self.assertEqual(self.new_staff.wants_accomodation, "N")

        self.assertEqual(self.new_staff.person_type, "Staff")
        self.assertTrue(isinstance(self.new_staff.person_id, int))
        self.assertTrue(isinstance(self.new_staff, Staff))

    def test_fellow_object(self):
        """
        Tests for the class person and their attributes
        """
        self.assertTrue(self.new_fellow, "Eva Johnson")
        self.assertEqual(self.new_fellow.person_name, "Eva Johnson")

        self.assertEqual(self.new_fellow.wants_accomodation, 'Y')

        self.assertEqual(self.new_fellow.wants_accomodation, "Y")

        self.assertEqual(self.new_fellow.person_type, "Fellow")
        self.assertTrue(isinstance(self.new_fellow.person_id, int))
        self.assertTrue(isinstance(self.new_fellow, Fellow))


if __name__ == "__main__":
    unittest.main()
