# make sure your solution is assigned to the answer variable so the tests can work!
str1 = "aeiou"

answer = {str1[i]:0 for i in range(0,len(str1))}

# answer = {char:0 for char in 'aeiou'}
# answer = dict.fromkeys("aeiou",0)
print(answer)