# **kwargs  - A special operator we can pass to functions
# Gathers remaining keyword arguments as a dictionary
# This is just a parameter - You can call it whatever you want

# def fav_colors(**kwargs):
#     for person, color in kwargs.items():
#         print(f"{person}'s favorite color is {color}")
#
# fav_colors(colt="purple", ruby="red", ethel="teal")
# fav_colors(colt="purple", ruby="red", ethel="teal", ted="blue")
# fav_colors(colt="ROYAL DEEP BLUE")
#



def special_greeting(**kwargs):
    if "David" in kwargs and kwargs["David"] == "special":
        return "You get a special greeting David!"
    elif "David" in kwargs:
        return f"{kwargs['David']} David!"
    return "Not sure who this is..."

# print(special_greeting(David='hello'))
# print(special_greeting(Bob='hi'))
# print(special_greeting(David='special'))
print(special_greeting(David='special', Heather="hello"))