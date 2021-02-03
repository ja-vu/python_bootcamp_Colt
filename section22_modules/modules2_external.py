#python3 - m pip install NAME_OF_PACKAGE
from termcolor import colored
from colorama import init

# print(dir(termcolor))
# help(termcolor)
init()

text=colored("HI THERE", "mga", 'on_red')
print(text)