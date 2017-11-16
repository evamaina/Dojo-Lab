import random
from src.room import *
from src.person import *


class Dojo(object):

    """Class Dojo that creates rooms, 
    adds people to rooms and saves the state
    of the rooms and people.
    """
    unallocated_people = []

    def __init__(self):
        self.room_list = []
        self.people = []
        self.livingspace_with_occupants = {}
        self.office_with_occupants = {}
    """
    {'<room_name>': ['blue', 'gree', 'red'],
     '<room_type>': 'office'}

    """
    def create_room(self, args):
        """ create room """
        if args["<room_type>"] == "office":
            for room in args["<room_name>"]:
                new_room = Office(room)
                self.room_list.append(new_room)

                self.office_with_occupants[new_room] = []
                print("An office called {} has been successfully created!".format(new_room.room_name))
                """checks whether the room given is livingspace"""
        elif args["<room_type>"] == "livingspace":
            for room in args["<room_name>"]:
                new_room = Living_Space(room)
                #self.room_list.append(new_room)
                self.livingspace_with_occupants[new_room] = []
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
        """Adds a person to the dojo and allocates the person to a random room
        """
        if args['<person_type>'] == 'fellow':

            new_person = Fellow(args['<person_name>'], args['<person_type>'])
            #self.people.append(new_person)
            print("A person called {} has been successfully added!".format(new_person.person_name))
            #pirnt("Fellow {} has been allocated the office Blue".format(new_person.person_name))
        elif args['<person_type>'] == 'staff':
            new_person = Staff(args['<person_name>'], args['<person_type>'] )
            #self.people.append(new_person)
            print("A person called {} has been successfully added !".format(new_person.person_name))
            #pirnt("Staff {} has been allocated the office Blue".format(new_person.person_name))
            #self.allocate_random_room(new_person, wants_accomodation)
        else:
            print"Confirm if you have added the person to the correct room and try again"

    def print_room(self, room_name):
        room_name = args["<room_name>"]
        room_list.append(room_name)
        print(room_list)




























































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


    

    




    


