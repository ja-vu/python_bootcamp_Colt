l = [1,2,3,4]

evens = list(filter(lambda x: x % 2 == 0,l))

# filter
# There is a lambda for each value in the iterable.
# Returns filter object which can be converted into other iterables
# The object contains only the values that return true to the lambda


users = [
    {"username": "samuel", "tweets": ["I love cake", "I love pie"]},
    {"username": "katie", "tweets": ["I love cake my cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": ["dogs are the best"]},
    {"username": "guitar_gal", "tweets": []}
]

# inactive_users = list(filter(lambda u: len(u['tweets']) == 0 , users))
# inactive_users = list(filter(lambda u: not u['tweets'], users)) # [] '' 0 are falsy
# print(inactive_users)

# only collect username for inactive users
usernames = list(map(lambda user: user["username"].upper(), filter(lambda u: not u['tweets'], users)))
print(usernames)

# list comprehension
inactive_users2 = [user for user in users if not user["tweets"]]
print(inactive_users2)


# MAP AND FILTER
names = ['Lassie', 'Colt', 'Rusty']

# return a new list only if value is < 5 chars

msg= list(map(lambda name: f"Your instructor is {name}", filter(lambda value: len(value) <5, names)))
