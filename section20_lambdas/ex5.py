def sum_even_values(*args):
    return sum([num for num in args if num %2 == 0])

sum_even_values(1,2,3,4,5,6)
sum_even_values(1)


def sum_floats(*args):
    return sum([num for num in args if type(num) == float])


sum_floats(1.5, 2.4, 'awesome', [], 1)