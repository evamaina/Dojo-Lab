import random
import os
import sys  # System-specific parameters and functions
import inspect

from src.room import Room, Office, Living_Space
from src.person import Person, Staff, Fellow



class Dojo(object):

    """Class Dojo that creates rooms, 
    adds people to rooms and saves the state
    of the rooms and people.
    """
    def __init__(self):
        self.people = {
            "fellows": [],
            "staff": [],
            "with_offices": [],
            "without_offices": [],
            "with_livingspaces": [],
            "without_livingspaces": []
        }
        self.rooms = {
            "offices": [],
            "livingspaces": []
        }

    def get_random_room(self, room_type):
        """
         returns an office or living space that has space.
        """
        # Get a random office
        if room_type == "office":
            if [room for room in self.rooms["offices"]
               if len(room.room_occupants) < room.room_capacity]:
                random_office = random.choice(
                    [room for room in self.rooms["offices"]
                    if len(room.room_occupants) < room.room_capacity])
                return random_office
        # Get a random living space
        elif room_type == "livingspace":
            if [room for room in self.rooms["livingspaces"]
               if len(room.room_occupants) < room.room_capacity]:
                random_livingspace = random.choice(
                    [room for room in self.rooms["livingspaces"] if
                     len(room.room_occupants) < room.room_capacity])

                return random_livingspace

    def room_exist(self, room_name, list):
        """Function to check if a romm with same name exist
        room_status can have 0 and 1. 0-does not exist while
         1-room with same name exist"""
        room_status = 0
        for i in list:
                if(i.room_name in room_name):
                    room_status = 1
                    break
        return room_status

    def create_room(self, args):
        """ create room """
        if args["<room_type>"] == "office":
            for room in args["<room_name>"]:
                new_room = Office(room)
                if(self.room_exist(new_room.room_name,
                   self.rooms["offices"]) == 1):
                     print("Sorry. A room called {} already exists."+
                           " Please try again another name".format(new_room.room_name))                  
                else:
                    new_office = Office(room)
                    self.rooms["offices"].append(new_office)
                    print("An office called {} has been successfully created!".format(new_office.room_name))

                """checks whether the room given is livingspace"""
        elif args["<room_type>"] == "livingspace":
            #for room in args["<room_name>"]:
            for room_name in args["<room_name>"]:
                if (self.room_exist(room_name,self.rooms["livingspaces"])==1):
                    print("Sorry. A room called {} already exists. "
                       "Please try again another name".format(room_name))
                else:
                    new_livingspace = Living_Space(room_name)
                    self.rooms["livingspaces"].append(new_livingspace)
                    print("A living space called {} has been successfully created"
                       .format(new_livingspace.room_name))

    def print_room(self, args):
        room_name = args['<room_name>'][0]
        rooms = self.rooms["offices"] + self.rooms["livingspaces"]
        if room_name not in [room.room_name for room in rooms]:
            print("\nRoom does not exist\n")

        else:
            print("\nRoom "+room_name)
            print("------------------------------------\n")
            for room in rooms:
                if room.room_name == room_name:
                    if room.room_occupants:
                        for person in room.room_occupants:
                            print(person.person_name +" "+ person.person_type + " " + person.wants_accomodation)
            print("\n")
        
   

    def add_person(self, args):
        person_name=args['<F_name>']+" "+args['<L_name>']
        if args['<person_type>'] == 'fellow':
            wants_accommodation=args['<wants_accomodation>']
            new_fellow = Fellow(person_name, args['<wants_accomodation>'])
            self.people["fellows"].append(new_fellow)
            print("A person called {} has been added to the room!".format(new_fellow.person_name))
            if wants_accommodation =='y' or wants_accommodation =='Y':
                """ Checks if there is available living space and if none
                  the fellow is added to without living spaces list
                """
                fellow_livingspace = self.get_random_room("livingspace")
                if fellow_livingspace is not None:
                    fellow_livingspace.room_occupants.append(new_fellow)
                    self.people["with_livingspaces"].append(new_fellow)
                    print(
                        "{0} has been allocated the living space {1}.".format(
                            new_fellow.person_name,
                            fellow_livingspace.room_name))
                else:
                    self.people["without_livingspaces"].append(new_fellow)
                    print("Sorry."
                           "No living space is currently available for {}."
                           "Please add a new livingpace, then add ".format(new_fellow.person_name))

            elif wants_accommodation =='n' or wants_accommodation =='N':
                self.people["without_livingspaces"].append(new_fellow)
                            # Check if there is a vacant office, if none, add the fellow to
            # the without offices list
            fellow_office = self.get_random_room("office")
            if fellow_office is not None:
                fellow_office.room_occupants.append(new_fellow)
                self.people["with_offices"].append(new_fellow)
                print("{0} has been allocated the office {1}."
                       .format(new_fellow.person_name, fellow_office.room_name))

            else:
                self.people["without_offices"].append(new_fellow)
                print("Sorry. No office is currently available for {}."
                       "Please try again later".format(new_fellow.person_name))

            return new_fellow

        elif args['<person_type>'] == 'staff':
            new_staff = Staff(person_name, args['<person_type>'])
            print("A person called {} has been added to the dojo!".format(new_staff.person_name))
            """ Checks if there is a vacant office and if none the staff is added to 
             without offices list
            """
            staff_office = self.get_random_room("office")
            if staff_office is not None:
                staff_office.room_occupants.append(new_staff)
                self.people["with_offices"].append(new_staff)
                print("{0} has been allocated the office {1}.".
                       format(new_staff.person_name, staff_office.room_name))
            else:
                self.people["without_offices"].append(new_staff)
                print("Sorry. No office is currently available for {},Please create another office room"
                       .format(new_staff.person_name))

            return new_staff

    def print_allocations(self,args):
        rooms = self.rooms["offices"] + self.rooms["livingspaces"]
        filename=args['<o>'] 
    
        if(filename):
            
            file = open(filename + ".txt","w") 
            members=""
            for room in rooms:
                if room.room_occupants:
                    members+="Room " +room.room_name+"\n"
                    members+="-------------------------------\n"
                    for person in room.room_occupants:
                        members = members + person.person_name + ", "
                    members+="\n\n"
            file.write(members) 
            file.close() 
        print("\n")
        for room in rooms:
            if room.room_occupants:
                print("Room " +room.room_name)
                print("-------------------------------")
                members=""
                for person in room.room_occupants:
                    members = members + person.person_name + ", "
                print(members)
                print("\n")
        print("\n")

    def print_unallocated(self,args):
        filename=args['<o>']
        if(filename):
            members="\nUnallocated members\n--------------------------\n"
            peoples = self.people["without_offices"] + self.people["without_livingspaces"]
            for people in peoples:
                members = members + people.person_name + ", "

            file = open(filename + ".txt","w") 
            members+="\n"
            file.write(members) 
            file.close() 

        peoples = self.people["without_offices"] + self.people["without_livingspaces"]
        print("Unallocated Member\n----------------------------\n")
        members=""
        for people in peoples:
            members = members + people.person_name + ", "
        print(members + "\n")
        print("\n")

















































