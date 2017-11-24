import random
import os
import sys  # System-specific parameters and functions
import inspect


from room import Room, Office, Living_Space
from person import Person, Staff, Fellow



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
                    [room for room in self.rooms["offices"] if
                     len(room.room_occupants) < room.room_capacity])

                return random_office

                 # Get a random living space
        elif room_type == "livingspace":
            if [room for room in self.rooms["livingspaces"]
               if len(room.room_occupants) < room.room_capacity]:
                random_livingspace = random.choice(
                    [room for room in self.rooms["livingspaces"] if
                     len(room.room_occupants) < room.room_capacity])

                return random_livingspace



   

    """
    {'<room_name>': ['blue', 'gree', 'red'],
     '<room_type>': 'office'}

    """
    def create_room(self, args):
        """ create room """

        all_rooms = self.rooms["offices"] + self.rooms["livingspaces"]
        if args["<room_type>"] == "office":
            for room_name in args["<room_name>"]:
                
                if room_name in [room_name for room_name in self.rooms["offices"]]:
                    print(
                    "Sorry. A room called {} already exists. Please try again"
                    .format(room_name))
                else:
                    new_office = Office(room_name)
                    self.rooms["offices"].append(new_office)
                    print("An office called {} has been successfully created!"
                       .format(new_office.room_name))
                return new_office
                
                """checks whether the room given is livingspace"""
        elif args["<room_type>"] == "livingspace":
            #for room in args["<room_name>"]:
            for room_name in args["<room_name>"]:
                if room_name in [room_name for livingspace in
                             self.rooms["livingspaces"]]:
                    print("Sorry. A room called {} already exists. "
                       "Please try again".format(room_name))
            else:
                new_livingspace = Living_Space(room_name)
                self.rooms["livingspaces"].append(new_livingspace)
                print("A living space called {} has been successfully created"
                       .format(new_livingspace.room_name))
                return new_livingspace
                
            
    """
    args = {'--wants_accomodation': True,
     '<person_name>': 'eva',
     '<person_type>': 'fellow'}
    """
    def add_person(self, args):
        if args['<person_type>'] == 'fellow':
            new_fellow = Fellow(args['<person_name>'], args['<person_type>'])
            self.people["fellows"].append(new_fellow)
            print("A person called {} has been added to the room!".format(new_fellow.person_name))
            if wants_accommodation is True:
                """ Checks if there is available living space and if none
                  the fellow is added to without living spaces list
                """
                fellow_livingspace = self.get_random_room("livingspace")
                if fellow_livingspace is not None:
                    fellow_livingspace.room_occupants.append(new_fellow)
                    self.people["with_livingspaces"].append(new_fellow)
                    print(
                        "{0} has been allocated the living space {1}.".format(
                            person_name,
                            fellow_livingspace.room_name))
                else:
                    self.people["without_livingspaces"].append(new_fellow)
                    print("Sorry."
                           "No living space is currently available for {}."
                           "Please try again later".format(new_fellow))

            elif wants_accommodation is False:
                self.people["without_livingspaces"].append(new_fellow)
                            # Check if there is a vacant office, if none, add the fellow to
            # the without offices list
            fellow_office = self.get_random_room("office")
            if fellow_office is not None:
                fellow_office.room_occupants.append(new_fellow)
                self.people["with_offices"].append(new_fellow)
                print("{0} has been allocated the office {1}."
                       .format(person_name, fellow_office.room_name))

            else:
                self.people["without_offices"].append(new_fellow)
                print("Sorry. No office is currently available for {}."
                       "Please try again later".format(new_fellow))

            return new_fellow

        elif args['<person_type>'] == 'staff':
            new_staff = Staff(args['<person_name>'], args['<person_type>'])
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
                print("Sorry. No office is currently available for {},Please try again later"
                       .format(new_staff))

            return new_staff




























































"""Usage: add_person <person_name>  (fellow,staff)
        [<wants_accommodation>]
        if args["<person_name>"]:
            person_name = args["<person_name>"]

        if args["<person_type>"] == "Fellow":
        if args["<wants_accommodation>"] == "Y" or\
           args["<wants_accommodation>"] == "y":
                    wants_accommodation = True
                    person_type = "Fellow"
                    dojo.add_person(person_name, person_type,\
                                    wants_accommodation)
                    print("")

        elif args["<wants_accommodation>"] is None:
                    wants_accommodation = False
                    person_type = "Fellow"
                    dojo.add_person(person_name, person_type,\
                                    wants_accommodation)
                    print("")

        elif args["<person_type>"] == "Staff":
                person_type = "Staff"
                dojo.add_person(person_name, person_type)
                print("")

        if args["<wants_accommodation>"] == "Y" or args[
                "<wants_accommodation>"] == "y":
                    cprint(
                        " Staff cannot be allocated to a living space")

        else:
                cprint(
                    "Confirm if u entered the correct person type\
                        and try again")

        @docopt_cmd
    def do_print_room(self, args):
        ""Usage: print_room <room_name>""
        room_name = args["<room_name>"]
        print("")
        dojo.print_room(room_name)



        @docopt_cmd
    def do_print_allocations(self, args):
        ""Usage: print_allocations [--file=text_file]""
        if args["--file"]:
            print(args["--file"])
            print(dojo.print_allocations(args["--file"]))
        dojo.print_allocations()


    @docopt_cmd
    def do_print_unallocated(self, args):
        "Usage: print_unallocated [--file=text_file]""
        if args["--file"]:
            print(args["--file"])
            dojo.print_unallocated(args["--file"])
        dojo.print_unallocated()

         @docopt_cmd
    def do_allocate(self, args):
        ""Usage: allocate""
        dojo.allocate()

            @docopt_cmd
    def do_get_person_id(self, args):
        "Usage: get_person_id <person_name> ""
        person_name = args["<person_name>"] 
        dojo.get_person_id(person_name)

    @docopt_cmd
    def do_reallocate_person(self, args):
        ""Usage: reallocate_person <person_id> <new_room>""
        if args["<person_id>"].isstring():
            print("person id cannot be string")
            return
        else:
            (dojo.reallocate_person(int(args['<person_id>']),
                                     args['<new_room>']))

    @docopt_cmd
    def do_save_state(self, args):
        "Usage: save_state [--db=sqlite_database]""
        # print(args['--db'])
        dojo.save_state(args['--db'])

    @docopt_cmd
    def do_load_state(self, args):
        "Usage: load_state <db>""
        db_name = args["<db>"]
        dojo.load_state(db_name)

    @docopt_cmd
    def do_load_people(self, args):
        "Usage: load_people <text_file>""
        dojo.load_people(args["<text_file>"])

    @docopt_cmd
    def do_print_person_id(self, args):
        " Usage: print_person_id ""
        dojo.print_person_id()

    def do_quit(self, args):
        "Quits out of Interactive Mode.""

        print('Ciao Adios!!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    Dojo().cmdloop()

print(opt)

"""


    

    




    


