# numbers = [1,2,3,4,5]
# doubled_numbers = []
#
# for num in numbers:
#     doubled_number = num *2
#     doubled_numbers.append(doubled_number)
#
# print(doubled_numbers)

# numbers = [1,2,3,4,5]
#
# doubled_numbers = [num * 2 for num in numbers]
#
# print(doubled_numbers)

# name = "JAMES"
# upper = [char.upper() for char in name]
#
# print(upper)

# print([num*10 for num in range(1,6)])
#
# print([bool(val) for val in [0, [], '', 1]])

numbers = [1,2,3,4,5,6]

# evens = [num for num in numbers if num % 2 == 0]
# odds = [num for num in numbers if num % 2 != 0]
# print(evens)
# print(odds)

print([num*2 if num % 2 == 0 else num/2 for num in numbers])

with_vowels = "This is so much fun!"
new = ''.join([char for char in with_vowels if char not in "aeiou"])
print(new)