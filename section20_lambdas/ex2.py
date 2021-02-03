def is_all_strings(lst):
    return all(type(l) == str for l in lst)

print(is_all_strings([2,'a','b','c']))