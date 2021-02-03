'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''
def isEven(num):
    return num % 2 == 0


def partition(lst, fn):
    truthy = []
    falsy = []
    for val in lst:
        if fn(val):
            truthy.append(val)
        else:
            falsy.append(val)
    return [truthy, falsy]

print(partition([1,2,3,4], isEven)) # [[2,4],[1,3]]
