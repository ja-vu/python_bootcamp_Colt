# add() - Adds an element to a set. If the element is already in the set,
# the set doesn't change

s = set ([1,2,3])
s.add(4)
print(s)
s.add(4)
print(s)

# remove() - removes a value from the set - returns a KeyError if the values is
# not found

cities = ["Los Angeles", "Boulder", "Kyoto", "Florence", "Shanghai"]

# discard() -
# copy() - Creates a copy of the set
# clear() - Removes all contents of the set
# Set Math - Sets have quite a few other mathematical methods including
# intersection, symmetric_difference, union

math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
bio_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}

# | means union
# & means intersection