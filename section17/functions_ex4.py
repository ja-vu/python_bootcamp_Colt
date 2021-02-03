def speak(animal="dog"):
    if animal == "pig":
        return "oink"
    elif animal == "duck":
        return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    return "?"

print(speak())
print(speak("snake"))

# Alternative solution using a dictionary

# def speak(animal="dog"):
#     noises = {
#         "dog": "woof",
#         "pig": "oink",
#         "duck": "quack",
#         "cat": "meow"
#     }
#     noise = noises.get(animal)
#     if noise:
#         return noise
#     return "?"

# Another alternative solution

# def speak(animal="dog"):
#     noises = {"dog": "woof","pig": "oink","duck": "quack","cat": "meow"}
#     return noises.get(animal, '?')