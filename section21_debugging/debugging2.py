# Handle Errors

# Try-Except block

# try:
#     foobar
# except:
#     print("PROBLEM")
# print("AFTER THE TRY")
#
#
#
# try:
#     colt
# except NameError:
#     print("YOU TRIED TO USE A VAR THAT WAS NEVER DECLARED")

d = {"name": "Rusty"}

def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None


print(get(d,"name"))
