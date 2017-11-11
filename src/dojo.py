from src.room import *
from src.person import *


class Dojo(object):
    """
    {'<room_name>': ['blue', 'gree', 'red'],
     '<room_type>': 'office'}

    """
    def create_room(self, args):
        """ create room """
        if args["<room_type>"] == "office":
            for room in args["<room_name>"]:
                new_room = Office(room)
                print("An office called {} has been successfully created!".format(new_room.room_name))
                """checks whether the room given is livingspace"""
        elif args["<room_type>"] == "livingspace":
            for room in args["<room_name>"]:
                new_room = Living_Space(room)
                print("Living_Space called {} has been successfully created!".format(new_room.room_name))
        else:
            print(
                "Confirm if u entered the correct room type and try again")
    """
    args = {'--wants_accomodation': True,
     '<person_name>': 'eva',
     '<person_type>': 'fellow'}
    """
    def add_person(self, args):
        if args['<person_type>'] == 'fellow':
            new_person = Fellow(args['<person_name>'], args['<person_type>'])
            print(new_person.person_name)
        elif args['<person_type>'] == 'staff':
            new_person = Staff(args['<person_name>'], args['<person_type>'])
            print(new_person.person_name)



























































