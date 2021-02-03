"""
What is a Function?
- A process for executing a task
- It can accept input and return an output
- Useful for executing similar procedures over and over

Why use Functions?
- Stay DRY - Don't Repeat Yourself (opposite of WET - Write everything twice)
- Clean up and prevent code duplication
- "Abstract away" code for other users
"""

# def name_of_function():
    # block of code

def sing_happy_birthday(name):
    print('Happy Birthday To You')
    print('Happy Birthday To You')
    print(f'Happy Birthday Dear {name}')
    print('Happy Birthday To You')

sing_happy_birthday("Phuoc")