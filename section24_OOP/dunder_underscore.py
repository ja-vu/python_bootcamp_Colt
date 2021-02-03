# _name -> Private use for a class
# __name -> Python will do something. Name Mangling
# __name__ -> Dunder methods. Used for python specific methods

class Person:
    def __init__(self):
        self.name="Tony"
        self._secret = "hi!"
        self.__msg = "I like turtles"
        self.__lol = "hahaha"
    # def doorman(self,guess):
    #     if guess == self._secret:
    #         # let them in


p = Person()
print(p.name)
print(p._secret)
print(dir(p))