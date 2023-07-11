#!/usr/bin/python3
"""import commands"""

import cmd
""" console"""


class HBNBCommand(cmd.Cmd):
    """
    Command-line interface for the HBNB program.
    """

    prompt = "(hbnb)"

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_help(self, arg):
        """
        Help command to display help messages.
        """
        if arg == 'quit':
            print("Quit command to exit the program")
            print()
        else:
            print()
            print("Documented commands (type help <topic>):")
            print("========================================")
            print("EOF  help  quit")
            print()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
