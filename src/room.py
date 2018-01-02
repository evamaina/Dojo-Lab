class Room(object):
    """A class to create room objects whereby the other sub-classes
    like office and living room inherit properties from."""

    def __init__(self, room_name=None,
                 room_type=None, room_capacity=None):

        self.room_name = room_name
        self.room_type = room_type
        self.room_capacity = room_capacity
        self.room_occupants = []

    def add_person(self, person):
        """This method will add a person to a room and
         reduce capacity by one"""

        self.room_occupants.append(person)
        self.room_capacity -= 1
        return self.room_capacity


class Living_Space(Room):
    """Class to create an office.This class will inherit its
    properties and methods from the superclass Room. Method
    overriding will also take place on properties such as capacity
    since once we call the super function class and the room is occupied,
    the capacity reduces by one and takes in the new value"""
    def __init__(self, room_name):
        super(Living_Space, self).__init__(
            room_name, room_type='Living_Space', room_capacity=4)


class Office(Room):
    """ Class to create a living space.This class will inherit properties
     and methods from the super class Room.Method overriding also takes place
      on capacity once we call the super class function."""
    def __init__(self, room_name):
        super(Office, self).__init__(
            room_name, room_type='office', room_capacity=6)

        """super() lets you avoid referring to the base class
        explicitly. But the main advantage comes with multiple
         inheritance,where all sorts of fun stuff can happen."""
