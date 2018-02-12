""" cmlineclick.py

Author: Anthony Panisales

-Prints messages, in different languages, that can utilize a command line argument 

-Prints the integer file descriptor of a file

"""

from __future__ import print_function
from future.utils import python_2_unicode_compatible
import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

def hello(greeting, **kwargs):
    print('{0} {1}!'.format(greeting, kwargs['name']))

def filefunc(**kwargs):
    print("fileObject.fileno() == {0}".format(kwargs['file'].fileno()))

@click.group(context_settings=CONTEXT_SETTINGS)
def greet():
    pass

@greet.command()
@click.argument('name', default='world')
def english(**kwargs):
    """Prints a message in English"""
    hello("Hello", **kwargs)

@greet.command()
@click.argument('name', default='mundo')
def spanish(**kwargs):
    """Prints a message in Spanish"""
    hello("Hola", **kwargs)

@greet.command()
@click.argument('name', default='le monde')
def french(**kwargs):
    """Prints a message in French"""
    hello("Bonjour", **kwargs)

@greet.command()
@click.argument('name', default='welt')
def german(**kwargs):
    """Prints a message in German"""
    hello("Hallo", **kwargs)

@greet.command()
@click.argument('name', default='sekai')
def japanese(**kwargs):
    """Prints a message in Japanese"""
    hello("Kon'nichiwa", **kwargs)

@greet.command()
@click.argument('name', default='mir')
def russian(**kwargs):
    """Prints a message in Russian"""
    hello("Privet", **kwargs)

@greet.command()
@click.argument('name', default='mondo')
def italian(**kwargs):
    """Prints a message in Italian"""
    hello("Ciao", **kwargs)

@greet.command()
@click.argument('file', type=click.File('r'))
def file(**kwargs):
    """Prints a File object's integer file descriptor"""
    filefunc(**kwargs)   

if __name__ == '__main__':
    greet()