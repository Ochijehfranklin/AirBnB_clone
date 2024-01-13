#!/usr/bin/python3
"""
This would hold my console
"""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    This would hold the command prompt
    """

    prompt = "(hbnb): "
    right_classes = ["BaseModel"]

    def emptyline(self):
        """
        Empty line gets nothing
        """
        pass

    def do_create(self, arg):
        """This would create a new instance

        Args:
            str : instance to create
        """
        order = shlex.split(arg)

        if len(order) == 0:
            print("** class name missing**")
        elif order[0] not in self.right_classes:
            print("**class doesn't exist **")
        else:
            newInstance = eval(f"{order[0]}()")
            storage.save()
            print(newInstance.id)

    def do_show(self, arg):
        """
        Shows string rep of instance
        Usage: show <class_name> <id>
        """
        order = shlex.split(arg)

        if len(order) == 0:
            print("** class name missing **")
        elif order[0] not in self.right_classes:
            print("** class doesn't exist**")
        elif len(order) < 2:
            print("**instance id missing **")
        else:
            object = storage.all()

            key = "{}.{}".format(order[0], order[1])
            if key in object:
                print(object[key])
            else:
                print("** no instance found**")

    def do_quit(self, arg):
        """
        This quits the console
        """
        return True

    def do_destroy(self, arg):
        """
        This would help to delete instances
        based on class name and id

        Args:
            instance : instance to destroy
        """

        order = shlex.split(arg)

        if len(order) == 0:
            print("***class name missing*")
        elif order[0] not in self.right_classes:
            print("**class doesn't exist**")
        elif len(order) < 2:
            print("**instance id is missing**")
        else:
            object = storage.all()
            key = f"{order[0]}.{order[1]}"
            if key in object:
                del object[key]
                storage.save()
            else:
                print("**No Instance found**")

    def do_all(self, arg):
        """
        This would print all objects in the class
        """
        object = storage.all()
        order = shlex.split(arg)

        if len(order) == 0:
            for key, value in object.items():
                print(str(value))
        elif order[0] not in self.right_classes:
            print("**class doesn't exist**")
        else:
            for key, value in object.items():
                if key.split('.')[0] == order[0]:
                    print(str(value))

    def do_update(self, arg):
        """
        updates instance based on attribute given
        Args:
            class_name: class to add
            id: unique id of class
        """
        order = shlex.split(arg)

        if len(order) == 0:
            print("**class name missing**")
        elif order[0] not in self.right_classes:
            print("**class doesn't exist**")
        elif len(order) < 2:
            print("**instance id is missing**")
        else:
            object = storage.all()

            key = f"{order[0]}.{order[1]}"

            if key not in object:
                print("**no instance found**")
            elif len(order) < 3:
                print("**attribute name is missing**")
            elif len(order) < 4:
                print("**value missing**")
            else:
                obj = object[key]

                attrName = order[2]
                attrVal = order[3]

                try:
                    attrVal = eval(attrVal)
                except Exception:
                    pass
                setattr(obj, attrName, attrVal)

                obj.save()

    def help_quit(self, arg):
        """
        Brief on how to quit
        """
        print("Quit command to exit console")

    def do_EOF(self, arg):
        """
        This shows EOF
        """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
