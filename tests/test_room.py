import unittest
import sys
from os import path
from room import Room, Office, Living_Space
from person import Fellow, Staff
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


class RoomTestCases(unittest.TestCase):
    """
    Tests for the  room objects and their attributes
    """
    def setUp(self):
        # set up the objects
        self.new_office = Office("Blue")
        self.new_living_Space = Living_Space("Mag")
        self.new_fellow = Fellow("Eva Johnson", "Y")
        self.new_staff = Staff("Evet Maina", "N")

    def test_office_object(self):
        """
        Tests for the class office and its attributes
        """
        self.assertTrue(self.new_office, "Blue")
        self.assertEqual(self.new_office.room_name, "Blue")
        self.assertTrue(self.new_office.room_type, "office")
        self.assertEqual(self.new_office.room_capacity, 6)
        self.assertEqual(self.new_office.room_occupant, [])
        self.assertTrue(isinstance(self.new_office, Office))

    def test_livingspace_object(self):
        """
        Tests for the class living space and its attributes
        """
        self.assertTrue(self.new_living_Space, "Mag")
        self.assertEqual(self.new_living_Space.room_name, "Mag")
        self.assertTrue(self.new_living_Space.room_type, "living_Space")
        self.assertEqual(self.new_living_Space.room_capacity, 4)
        self.assertEqual(self.new_living_Space.room_occupant, [])
        self.assertTrue(isinstance(self.new_living_Space, Living_Space))

    def test_add_person(self):
        """calling add_person method to add a new person to the office
        thus reducing the capacity of office to 5"""
        Room.add_person(self.new_office, self.new_staff)
        self.assertEqual(self.new_office.room_capacity, 5)
        """calling add_person method to add a new person to the living
        space thus reducing the capacity of theliving space to 3"""

        Room.add_person(self.new_living_Space, self.new_fellow)
        self.assertEqual(self.new_living_Space.room_capacity, 3)


if __name__ == "__main__":
    unittest.main()
