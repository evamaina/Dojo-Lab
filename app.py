"""
Dojo App. pick a command below
Usage:
    create_room <room_type> <room_name> ...
    add_person <person_name> <person_type> [--wants_accomodation]
    print_room <room_name>

    get_rooms
    q
    (-i | --interactive)
    Options:
    -h --help Show this screen.
    -i --interactive Interactive mode.
    -v --version
"""
import cmd
from docopt import docopt, DocoptExit
# from pyfiglet import figlet_format
# from termcolor import cprint
from src.dojo import Dojo
from src.room import Room, Office, Living_Space


def app_exec(func):
    """
    Decorator definition for the app.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)
        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            msg = "Invalid command! See help."
            print(msg)
            print(e)
            return

        except SystemExit:
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)

    return fn


class DojoCli(cmd.Cmd):

    prompt = "DojoApp=>"

    dojo = Dojo()

    @app_exec
    def do_create_room(self, arg):
        """Creates a new room
        Usage: create_room <room_type> <room_name> ...
        """
        self.dojo.create_room(arg)

    @app_exec
    def do_add_person(self, arg):
        """adds a new person
        Usage: add_person <F_name> <L_name>
        <person_type> [<wants_accomodation>]
        """
        self.dojo.add_person(arg)

    @app_exec
    def do_print_room(self, args):
        """Print a room
        Usage: print_room <room_name>...
        """
        self.dojo.print_room(args)

    @app_exec
    def do_print_allocations(self, arg):
        """Print a room
        Usage: print_allocation [<o>]
        """
        self.dojo.print_allocations(arg)

    @app_exec
    def do_print_unallocated(self, args):
        """prints unallocted rooms
         Usage: print_unallocated [<o>]
         """
        self.dojo.print_unallocated(args)

    @app_exec
    def do_reallocate_person(self, args):
        """
        Usage: reallocate_person <person_id> <room_name>
        """
        p_id = int(args["<person_id>"])
        r_name = args["<room_name>"]
        self.dojo.reallocate_person(p_id, r_name)

    @app_exec
    def do_load_people(self, args):
        """ loads people
        Usage: load_people
        """
        self.dojo.load_people(args)

    @app_exec
    def do_quit(self, arg):
        """usage: Exits the app"""


if __name__ == '__main__':
    DojoCli().cmdloop()
