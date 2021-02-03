def interleave(s1,s2):
    return ''.join([''.join(pair) for pair in list(zip(s1,s2))])

print(interleave('hi','no'))
print(interleave('aaa','zzz'))
print(interleave('lzr','iad'))

