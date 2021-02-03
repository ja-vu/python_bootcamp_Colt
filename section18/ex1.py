# def product(num1, num2):
#     return num1 * num2

def return_day(num):
    days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    return days.get(num, None)
print(return_day(1))


## alternate soln

# def return_day(num):
#     days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#     # Check to see if num valid
#     if num > 0 and num <= len(days):
#         # use num - 1 because lists start at 0
#         return days[num - 1]
#     return None