"""
Iterator: An object that can be iterated upon. An object which returns data, one element at
a time when next() is called on it.

Iterable: An object which will return an iterator when iter() is called on it
"""

# Custom for loop


def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            break
        else:
            func(thing)


def square(x):
    print(x*x)


my_for([1,2,3,4], print)
my_for("hello", print)

my_for([1,2,3,4,5], square)