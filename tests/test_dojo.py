import unittest
import os
import sys  # System-specific parameters and functions
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)


sys.path.insert(0, parentdir)

from src.room import *
from src.person import *
from src.dojo import Dojo


class DojoTestCases(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()
        self.args = {'<room_type>': 'office', '<room_name>': ['blue']}
        self.red_args = {'<room_type>': 'office', '<room_name>': ['red']}
        self.person_args = {'<wants_accomodation>': 'Y',
                            '<person_type>': 'staff',
                            '<F_name>': 'Eva',
                            '<L_name>': 'Maina'}

    def test_create_room_successfully(self):
        initial_office_count = len(self.dojo.rooms["offices"])
        self.dojo.create_room(self.args)
        new_office_count = len(self.dojo.rooms["offices"])
        self.assertEqual(new_office_count - initial_office_count, 1)

    def test_add_person_successfully(self):
        """Test add person"""
        self.dojo.create_room(self.red_args)
        self.dojo.add_person(self.person_args)
        self.assertEqual(len(self.dojo.people["staff"]), 1)

    def test_allocated_room_successfully(self):
        """Test add person"""
        self.dojo.create_room(self.red_args)
        self.dojo.add_person(self.person_args)
        self.assertEqual(len(self.dojo.people["with_offices"]), 1)

    def test_unallocated_room_successfully(self):
        """Test add person"""
        self.dojo.add_person(self.person_args)
        self.assertEqual(len(self.dojo.people["without_offices"]), 1)

    def test_reallocate_person(self):
        self.dojo.create_room(self.args)
        self.dojo.add_person(self.person_args)
        self.assertEqual(self.dojo.rooms["offices"][0].room_name, 'blue')
        self.assertEqual(len(self.dojo.people["staff"]), 1)
        self.dojo.create_room(self.red_args)
        self.assertEqual(len(self.dojo.rooms), 2)
        person_id = self.dojo.people["staff"][0].person_id
        new_room = 'red'
        # Relocation
        self.dojo.reallocate_person(person_id, new_room)
        self.assertEqual(self.dojo.rooms["offices"][1].room_name, 'red')


if __name__ == '__main__':
    unittest.main()
