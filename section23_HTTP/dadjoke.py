from termcolor import colored
from colorama import init
from pyfiglet import figlet_format
from random import randint
import requests

init()


def print_dad_joke_logo(msg, color):
    valid_colors = ("red", "green", "yellow", "blue",
                    "magenta", "cyan", "white")
    if color not in valid_colors:
        color = "magenta"
    result = colored(figlet_format(msg), color=color)
    print(result)


def joke_generator():
    url = "https://icanhazdadjoke.com/search"
    search_term = input("Let me tell you a joke! Give me a topic: ")

    response = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={"term": search_term}
    )
    data = response.json()
    if data['total_jokes'] == 0:
        print(
            f"Sorry, I don't have any jokes about {search_term}. Please try again.")
    else:
        rand_joke = randint(0, data['total_jokes'] - 1)
        print(
            f"I've got {data['total_jokes']} jokes about {search_term}. Here it is: ")
        print(data["results"][rand_joke]["joke"])


print_dad_joke_logo("Dad Joke 3000", "cyan")
joke_generator()
