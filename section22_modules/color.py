# ASII ART EXERCISE

from pyfiglet import figlet_format
from termcolor import colored
from colorama import init

init()


def print_art(msg, color):
    valid_colors = ("red", "green", "yellow", "blue",
                    "magenta", "cyan", "white")
    if color not in valid_colors:
        color = "magenta"
    result = colored(figlet_format(msg), color=color)
    return result


msg = input("What do you want to print?")
color = input("What color?")
print(print_art(msg, color))
