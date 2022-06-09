import requests
from random import choice
from termcolor import colored
url = "https://icanhazdadjoke.com/search"


user_input = input("Let me tell you a joke! Give me a topic: ")
response = requests.get(
	url, 
	headers={"Accept": "application/json"},
	params={"term": user_input}
)
data = response.json() # turn the string into a dictionary
if data["results"]:
	joke = choice(data["results"])["joke"]
	# print(data["results"])
	# print(f"status: {data['status']}")
	if data["total_jokes"] == 1: print(f"I found one joke about {user_input}:")
	else: print(f"I found {data['total_jokes']} jokes about {user_input}, here's one:")
	print(colored(joke, 'cyan'))
else:
	print(f"Sorry, I don't have any jokes about {user_input}")



