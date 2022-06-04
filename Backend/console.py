#!/usr/bin/python3
"""console program for managing backends using python"""

import cmd
from models.basemodel import BaseModel
from models.user import User
from models.story import Story
from models import storage

class Command(cmd.Cmd):
    """Console"""
    prompt = '(App) '

    def do_quit(self, arg):
        """Exit the console"""
        return True

    def emptyline(self):
        """an empty line + Enter should execute nothing"""
        pass

if __name__ == '__main__':
    Command().cmdloop()
