# Polymorphism
# A key principle OOP is the idea of polymorphism - an object can take on many (poly)
# forms (morph)

# While a formal definition of polymorphism is more difficult , here are two important
# practical applications

"""
1. The same class method works in a similar way for different classes.

A common implementation of this is to have a method in a base (or parent) class that is
overridden by a subclass. This is called method overriding
2. The same operation works for different kinds of objects
"""
class Animal():
    def speak(self):
        raise NotImplementedError("Subclass needs to implement this method")


class Dog(Animal):
    def speak(self):
        return "woof"


class Cat(Animal):
    def speak(self):
        return "meow"


class Fish(Animal):
    pass


d = Dog()
print(d.speak())
f = Fish()
print(f.speak())