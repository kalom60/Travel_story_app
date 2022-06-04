#!/opt/homebrew/bin/python3
"""console program for managing backends using python"""

import cmd
from models.user import User
from models.story import Story
from models import storage


class Command(cmd.Cmd):
    """Console"""
    prompt = '(App) '
    __classes = {
        User.__name__: User,
        Story.__name__: Story
    }

    def do_quit(self, arg):
        """Exit the console"""
        return True

    def emptyline(self):
        """
        an empty line + Enter should execute nothing
        """
        pass

    @staticmethod
    def parse(line):
        """
        split all args and return list
        """
        if len(line) == 0:
            return []
        return line.split(' ')

    def do_all(self, arg):
        """
        prints all object of a class
        Ex: $ all User
        """
        args = Command.parse(arg)
        if len(args) == 0:
            print('** class name missing **')
        else:
            if args[0] in Command.__classes.keys():
                print(storage.all(Command.__classes[args[0]]))
            else:
                print('** class doesn\'t exist **')

    def do_show(self, arg):
        """
        prints an object of a class based
        on class name and id
        Ex: $ show User 1234-1234-1234 
        """
        args = Command.parse(arg)
        if len(args) == 0:
            print('** class name missing **')
        else:
            if args[0] in Command.__classes.keys():
                if len(args) >= 2:
                    if f'{args[0]}.{args[1]}' in\
                            storage.all(Command.__classes[args[0]]).keys():
                        print(storage.all(Command.__classes[args[0]])\
                                [f'{args[0]}.{args[1]}'].to_dict())
                    else:
                        print('** no instance found **')
                else:
                    print('** instance id missing **')
            else:
                print('** class doesn\'t exist **')
            
if __name__ == '__main__':
    Command().cmdloop()
