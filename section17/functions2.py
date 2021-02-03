def square(num):
    return num ** 2

print(square(4))
print(square(8))

# Parameters - Variables that are passed to a function - think of them
# as placeholders that get assigned when you call the function

# Parameters vs Arguments

# A parameter is a variable in a method definition
# When a method is called, the arguments are the data you pass into
# the method's parameters.
# Argument is the actual value of this variable that gets passed to
# a function.

# DEFAULT PARAMETER

def exponent(num=5, power=2):
    return num ** power

print(exponent(2,3))
print(exponent(3,2))
print(exponent(3))
print(exponent())

# Why Default params?

# - Allows you to be more defensive
# - Avoids errors with incorrect parameters
# - More readable examples