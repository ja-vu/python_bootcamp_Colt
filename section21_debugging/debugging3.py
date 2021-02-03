# try
# except
# else
# finally

# try:
#     num = int(input("Please enter a number:"))
# except:
#     print("Thats not a number")
# else:
#     print("IM IN THE ELSE")
# finally:
#     print("runs no matter wht")

# while True:
#     try:
#         num = int(input("Please enter a number:"))
#     except ValueError:
#         print("That's not a number")
#     else:
#         print("GOOD JOB YOU ENTERED A NUMBER")
#         break
#     finally:
#         print("runs no matter waht")


# def divide(a,b):
#     try:
#         result = a / b
#     except ZeroDivisionError:
#         print("Don't divide by 0 please")
#     except TypeError as err:
#         print("a and b must be int or float")
#         print(err)
#     else:
#         print(f"{a} divided by {b} is {result}")


def divide(a,b):
    try:
        result = a / b
    except (ZeroDivisionError, TypeError) as err:
        print("Something went wrong")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")

print(divide(1,2))
print(divide(1,0))
print(divide(1,"a"))