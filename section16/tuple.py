numbers = (1,2,3,4)

# immutable (CANNOT BE CHANGED)
# tuples are faster than lists
# it makes your code safer (from bugs)
# valid keys in dict

# Tuples can be used as keys in dictionaries:
# locations = {
#     (36.7, 39.7): "Tokyo Office",
#     (40.7, 74.0): "New York Office",
#     (37.8, 122.4): "San Francisco Office"
# }

names = ('Colt', 'Blue', 'Rusty', 'Lassie')

for name in names:
    print(name)

# count()

names.count('blue')

# index() - Returns the index at which a value is found in a tuple