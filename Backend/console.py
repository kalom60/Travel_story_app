#!/usr/bin/python3
"""console program for managing backends using python"""

import cmd

class Command(cmd.Cmd):
    """Console"""
    prompt = '(App) '


if __name__ == '__main__':
    Command().cmdloop()
