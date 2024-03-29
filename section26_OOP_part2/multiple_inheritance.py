# MRO - Method Resolution Order
# Whenever you create a class, Python sets a MRO for that class, which is the order in which Python will
# look for methods on instance of that class
# dunder method __mro__
# method mro()

class Aquatic:
    def __init__(self, name):
        self.name = name

    def swim(self):
        return f"{self.name} is swimming"

    def greet(self):
        return f"I am {self.name} of the sea!"


class Ambulatory:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return f"{self.name} is walking"

    def greet(self):
        return f"I am {self.name} of the land!"


class Penguin(Ambulatory, Aquatic):
    def __init__(self, name):
        super().__init__(name=name)


jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")
print(captain_cook.swim())
print(captain_cook.walk())
print(captain_cook.greet())