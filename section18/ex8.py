'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''

def frequency(l, term):
    return l.count(term)

frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1