# SyntaxError
# Occurs when Python encounters incorrect syntax (something it doesn't parse)
# Usually due to typos or not knowing Python well enough

# def first:
# None = 1
# return

# NameError - This occurs when a variable ais not defined ie, it hasn't been assigned
# TypeError - Occurs when - an operation or function is applied to the wrong type
# python cannot interpret an operation on two data type
# IndexError - Occurs when you try to access an element in a list using an invalid index
# ValueError - Occurs when a built-in operation or func receives an argument that has the right type but an inappropriate value
# KeyError - Occur when a dictionary does not have a specific key
# AttributeError - This occurs when a variable does not have an attribute

#raise ValueError('invalid value')

def colorize(text, color):
    colors = ("cyan", " yellow", "blue", "magenta", "blue", "green")
    if type(color) is not str:
        raise TypeError("Color must be a string")
    if type(text) is not str:
        raise TypeError("Text must be a string")
    if color not in colors:
        raise ValueError("color is invalid color")
    print(f"Printed {text} in {color}")

# colorize("hello", "red")
# colorize([], "red")
colorize("F", "cyan")

# colorize(3, "red")