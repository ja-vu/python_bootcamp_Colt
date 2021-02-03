# Max
# Return the largest item in an iterable or the largest of two or more arguments

# Min
# Return the smallest item in an iterable


names = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

# min(len(name) for name in names)

max(names,key=lambda n: len(n))
min(names,key=lambda n: len(n))

########################################################################


songs = [
    {"title":"happy birthday", 'playcount':1},
    {"title":"Survive", 'playcount':6},
    {"title":"YMCA", 'playcount':99},
    {"title":"Toxic", 'playcount':31},
]

min(songs, key=lambda s:s['playcount'])
min(songs, key=lambda s:s['playcount'])['title']