#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""
import cmd
import re
from shlex import split
import models
from models.base_model import BaseModel
from models.user import User


""" global constant """
CLASSES = [
    "BaseModel",
    "User"
]


def parsing(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


def check(args):
    """ checks if args is valid """
    li_arg = parsing(args)

    if len(li_arg) == 0:
        print("** class name missing **")
    elif li_arg[0] not in CLASSES:
        print("** class doesn't exist **")
    else:
        return li_arg


class HBNBCommand(cmd.Cmd):
    """Represents the command interpreter"""
    prompt = "(hbnb) "
    storage = models.storage

    def emptyline(self):
        """handles empty line + ENTER key"""
        pass

    def help_default(self, arg):
        """handles default behaviour"""
        default = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "create": self.do_create
        }

        expr = re.search(r"\.", arg)
        if expr:
            arg1 = [arg[:expr.span()[0]], arg[expr.span()[1]:]]
            expr = re.search(r"\((.*?)\)", arg1[1])
            if expr:
                command = [arg1[1][:expr.span()[0]], expr.group()[1:-1]]
                if command[0] in default:
                    call = "{} {}".format(arg1[0], command[1])
                    return default[command[0]](call)

        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_EOF(self, argv):
        """handles ctrl + D"""
        print("")
        return True

    def do_quit(self, argv):
        """exits the program"""
        return True

    def do_create(self, argv):
        """Creates a new instance of BaseModel"""
        args = check(argv)
        if args:
            print(eval(args[0])().id)
            self.storage.save()

    def do_show(self, argv):
        """Prints the string representation of
        an instance based on the class name and id
        """

        args = check(argv)
        if args:
            if len(args) != 2:
                print("** instance id missing **")
            else:
                k = "{}.{}".format(args[0], args[1])
                if k not in self.storage.all():
                    print("** no instance found **")
                else:
                    print(self.storage.all()[k])

    def do_all(self, argv):
        """Prints all string representation of all
        instances based or not on the class name.
        """

        li_arg = split(argv)
        objects = self.storage.all().values()
        if not li_arg:
            print([str(obj) for obj in ojects])
        else:
            if li_arg[0] not in CLASSES:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objects
                      if li_arg[0] in str(obj)])

    def do_destroy(self, argv):
        """Deletes an instance based on the class name and id"""
        li_arg = check(argv)
        if li_arg:
            if len(li_arg) == 1:
                print("** instance id missing **")
            else:
                k = "{}.{}".format(*li_arg)
                if k in self.storage.all():
                    del self.storage.all()[k]
                    self.storage.save()
                else:
                    print("** no instance found **")

    def do_update(self, argv):
        """ Updates an instance based on the class name and id"""
        li_arg = check(argv)
        if li_arg:
            if len(li_arg) == 1:
                print("** instance id missing **")
            else:
                in_id = "{}.{}".format(li_arg[0], li_arg[1])
                if in_id in self.storage.all():
                    if len(li_arg) == 2:
                        print("** attribute name missing **")
                    elif len(li_arg) == 3:
                        print("** value missing **")
                    else:
                        obj = self.storage.all()[in_id]
                        if li_arg[2] in type(obj).__dict__:
                            ty_val = type(obj.__class__.dict__[li_arg[2]])
                            setattr(obj, li_arg[2], ty_val(li_arg[3]))
                        else:
                            setattr(obj, li_arg[2], li_arg[3])
                else:
                    print("** no instance found **")

            self.storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
