"""
Using ** as an Argument:
Dictionary unpacking
"""

def display_names(first,second):
    print(f"{first} says hello to {second}")

names = {"first": "Colt", "second": "Rusty"}

# display_names(names) # NOPE
display_names(**names)
#display_names(first="Charlie", second="Sue")


def add_and_multiply_numbers(a,b,c, **kwargs):
    print(a + b * c)
    print("OTHER STUFF...")
    print(kwargs)

data = dict(a=1,b=2,c=3, d=55, name="Tony")

#print(add_and_multiply_numbers(data)) # TypeError
print(add_and_multiply_numbers(**data, cat="blue")) # 7