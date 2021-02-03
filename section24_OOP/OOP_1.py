class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

# Classes in Python can have a special __init__ method, which gets
# called every time you create an instance of the class (instantiate)
# self refers to the current class instance

# user1 = User("Helen")
user2 = User("Joe", "B", 29)
print(user2.first, user2.age)
