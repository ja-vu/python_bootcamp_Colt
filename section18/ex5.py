def multiple_letter_count(a):
    return {a[i]: (a.count(a[i])) for i in range(len(a))}
print(multiple_letter_count("awesome"))



# Solution

def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}