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
    __classes_columns = {
        'User': ['username', 'email', 'password'],
        'Story': ['title', 'Country', 'City', 'story', 'user_id']
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

    def do_delete(self, arg):
        """
        deletes an onject of a class based
        on class name and id
        Ex: $ delete User 1234-1234-1234-1234
        """
        args = Command.parse(arg)
        if len(args) == 0:
            print('** class name missing **')
        else:
            if args[0] in Command.__classes.keys():
                if len(args) >= 2:
                    if f'{args[0]}.{args[1]}' in\
                            storage.all(Command.__classes[args[0]]).keys():
                        storage.delete(storage.all(Command.__classes[args[0]])\
                                [f'{args[0]}.{args[1]}'])
                        storage.save()
                        print('** Deletion Complete **')
                    else:
                        print('** no instance found **')
                else:
                    print('** instance id missing **')
            else:
                print('** class doesn\'t exist **')

    def do_create(self, arg):
        """
        creates an onbject of a class based
        on class name
        Ex: $ create User
        """
        args = Command.parse(arg)
        if len(args) == 0:
            print('** class name missing **')
        else:
            if args[0] in Command.__classes.keys():
                values = Command.__classes_columns[args[0]]
                obj = {}
                for value in values:
                    if value != 'City':
                        res = True
                        while res:
                            obj[value] = input(f'{value}: ')
                            if len(obj[value].strip()) == 0:
                                print('** can\'t be null **')
                            else:
                                res = False
                    else:
                        obj[value] = input(f'{value}: ')
                new_obj = Command.__classes[args[0]](**obj)
                new_obj.save()
            else:
                print('** class doesn\'t exist **')
            
if __name__ == '__main__':
    Command().cmdloop()
