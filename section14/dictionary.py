cat = {
    "name": "Peach",
    "age":3,
    "isCute": True
}

cat2= dict(name="Peach", age=3)




# .values()
for value in cat.values():
    print(value)

# .keys()
for k in cat.keys():
    print(k)

# .items()
for k, v in cat.items():
    print(f" {k} is {v}")