def extremes(lst):
    if all((s,str) for s in lst):
        return tuple(((min(lst), max(lst)) for s in lst))
    else:
        res = min(lst), max(lst)
        return res

extremes([1,2,3,4,5])
extremes('alcatraz')
extremes((99,25,30,-7))


def extremes(nums):
    return (min(nums), max(nums))