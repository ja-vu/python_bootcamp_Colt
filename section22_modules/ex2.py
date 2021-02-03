import keyword
def contains_keyword(*args):
    return any([keyword.iskeyword(arg) for arg in args])


print(contains_keyword("hello", "goodbye")) #false
print(contains_keyword("def", "haha","lol","chicken", "alaska")) #true
print(contains_keyword("four", "for","if")) #true



# solution from Colt

# def contains_keyword(*args):
#     for item in args:
#         if keyword.iskeyword(item):
#             return True
#     return False