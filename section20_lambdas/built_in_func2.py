# Sorted
# Returns a new sorted list from the items in iterable

more_nums = [3,4,1,5,6,21,44,19]
print(sorted(more_nums, reverse=True))
sorted((2,1,45,23,99))




users = [
    {"username": "samuel", "tweets": ["I love cake", "I love pie"]},
    {"username": "katie", "tweets": ["I love cake my cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": ["dogs are the best"]},
    {"username": "guitar_gal", "tweets": []}
]

print(sorted(users, key=lambda user:user['username']))
print(sorted(users, key=lambda user:len(user['tweets']),reverse=True))