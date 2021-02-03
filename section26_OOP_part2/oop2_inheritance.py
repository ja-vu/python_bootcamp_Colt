# Inheritance
# A key feature of OOP is the ability to define a class which inherits from another class
# (a "base" or "parent" class)

# In Python, inheritance works by passing the parent class as an argument to the def of a child class

class Animal:
    def make_sound(self, sound):
        print(f"This animal says {sound}")
    cool = True


class Cat(Animal):
    pass


blue = Cat()
# gandalf.make_sound("meow")
# gandalf.cool

print(isinstance(blue, Cat))