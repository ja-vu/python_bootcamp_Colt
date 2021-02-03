'''
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
'''

def triple_and_filter(lst):
    return [num*3 for num in lst if num % 4 == 0]

triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12])


# another solution with map and filter

def triple_and_filter(lst):
    return list(filter(lambda x: x%4, map(lambda x:x*3,lst)))