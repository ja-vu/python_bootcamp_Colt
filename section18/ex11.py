'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''

def compact(lst):
    tmp = []
    for item in lst:
        if item:
            tmp.append(item)
    return tmp


# def compact(lst):
#     return [val for val in lst if val]