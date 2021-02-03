
def generate_evens():
    even_nums = [n for n in range(1, 50) if n % 2 == 0]
    return even_nums

print(generate_evens())