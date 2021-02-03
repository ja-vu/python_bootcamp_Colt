# Why modules
# - Keep python files small
# - reuse code across multiple files by importing
# - a module is just a python file

# Built-in modules
#

# import random as rand
# print(rand.choice(["apple","banana","cherry", "durian"]))
# print(rand.shuffle(["apple","banana","cherry", "durian"]))


# import partts of a module
# the from keyword lets you imports parts of a module
# Handy rule, only import what you need

from random import choice, randint
print(choice(["apple","banana","cherry", "durian"]))
print(randint(1,200))
