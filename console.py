#!/usr/bin/python3
"""import commands"""

from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
import json
import re
import cmd
""" console"""


class HBNBCommand(cmd.Cmd):
    """
    Command-line interface for the HBNB program.
    """

    prompt = "(hbnb)"
    valid_classes = [
            "BaseModel",
            "User",
            "Amenity",
            "City",
            "Place",
            "Review",
            "State"
            ]

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

    def do_create(self, arg):
        """
            The Method Creates a new instance of BaseModel
            and saves it to a json file and prints its id
        """
        if arg == "" or arg is None:
            print("** class name missing **")

        elif arg not in storage.classes():
            print("** class doesn't exist **")

        else:
            my_arg = storage.classes()[arg]()
            my_arg.save()
            print(my_arg.id)

    def do_show(self, myline):
        """
            This Method Prints the String Representation
            of an Instance based on the class name and id
        """
        if myline == "" or myline is None:
            print("** class name missing **")
        else:
            mywords = myline.split(' ')
            if mywords[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(mywords) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(mywords[0], mywords[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, my_line):
        """
            This Method performs the task of deleting an
            Instance.
            Parameters:
                my_line - A String representing the
                    command to be executed
        """
        if my_line == "" or my_line is None:
            print("** class name missing **")
        else:
            mywords = my_line.split(' ')
            if mywords[0] not in storage.classes():
                print("** class doesn't exist")
            elif len(mywords) < 2:
                print("** instance id missing **")
            else:
                mykey = "{}.{}".format(mywords[0], mywords[1])
                if mykey not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[mykey]
                    storage.save()

    def do_all(self, arg):
        """
        prints all strings representation based on classname or not
        """
        valid_classes = ["BaseModel", "User"]
        class_name = arg.strip() if arg else None
        if class_name and class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        obj = storage.all()
        if class_name:
            obj = {
                    key: val for key, val in obj.items()
                    if key.split(".")[0] == class_name
                    }

        print([str(val) for val in obj.values()])

    def do_update(self, args):
        valid_classes = ["BaseModel", "User"]
        arg = args.strip().split()
        if not arg:
            print("** class name missing **")
        elif arg[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        elif len(arg) < 3:
            print("** attribute name missing **")
        elif len(arg) < 4:
            print("** value missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            if key in objects:
                instance = objects[key]
                attribute_name = arg[2]
                attribute_val = arg[3].strip('"')
                setattr(instance, attribute_name, attribute_val)
                instance.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
