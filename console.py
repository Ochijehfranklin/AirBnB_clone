#!/usr/bin/python3
"""
This would hold my console
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    This would hold the command prompt
    """

    prompt = "(hbnb): "

    def do_quit(self, arg):
        """
        This quits the console
        """
        return True

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
