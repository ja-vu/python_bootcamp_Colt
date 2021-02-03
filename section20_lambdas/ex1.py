def remove_negatives(l):
    return list(filter(lambda n:n>=0,l))

remove_negatives([-1,3,4,-99])