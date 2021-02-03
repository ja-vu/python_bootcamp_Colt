# Use the * and ** operator as parameters to a function and outside of a function
# leverage dictionary and tuple unpacking to create more flexible functions

# *args - A special operator we can pass to functions
# -Gathers remaining arguments as a tuple
# This is just a parameter - you can call it whatever you want!

def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all_nums(4,6,9,77,55,33,22,11))
