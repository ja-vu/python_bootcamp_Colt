instructor = {
    "name": "James",
    "age": 30
}

# .clear() - Clears all the keys and values in a dictionary

# .copy() - Makes a copy of a dictionary

# .fromkeys() - Creates key-value pairs from comma seperated values

# .get() - Retrieves a key in an object and return None instead of a KeyError if they does not Exist

# .pop() - takes a single argument corresponding to a key a removes that key-value pair from the dict
# returns the value corresponding to the key that was removed

# .popitem() - Removes a random key in a dictionary

# update() - Update keys and values in a dict with another set of key values
# pairs

first = dict(a=1,b=2,c=3,d=5,e=6)
second = {}

second.update(first)
second
second['a'] = "AMAZING"