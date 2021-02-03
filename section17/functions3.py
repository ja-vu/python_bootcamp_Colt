def full_name(first,last):
    """ SOME DOC STRING """
    return f"Your name is {first} {last}"

# KEYWORD ARGUMENT
print(full_name(first="James", last="Vu"))
print(full_name(last="Vu",first="James"))

# Why use keyword argument?
# More flexibility
# Useful when passing a dictionary to a function
# and unpacking its values


# Scope - Where our variables can be accessed
# variables created in functions are scoped in that function!

# global scope
# default scope
# local scope

print(full_name.__doc__)

