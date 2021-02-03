# PDB - Python Debugger - To set breakpoints in our code we can use pdb by:
import pdb; pdb.set.set_trace()

first = "First"
second = "Second"
pdb.set_trace()
result = first + second
third = "Third"
result += third
print(result)


# PDB Commands
# l (list)
# n (next line)
# p (print)
# c (continue - finishes debugging)
# q (quit)