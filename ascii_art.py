from pyfiglet import figlet_format
from termcolor import colored

valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white") # colors that termcolor.color can print to the console
valid_colors_string = " ".join([f"{colored(clr, color=clr)}" for clr in valid_colors]) # string of all the valid colors styled with their color

def prompt_user(message=None):
	"""
	Prompts the user for an input color and message (if none is provided) and passes the inputs to the print_art function
	"""
	if not message: # the user hasn't supplied a message yet
		message = figlet_format(input("What message do you want to print?\n"))
	color = input(f"What color? {valid_colors_string}\n")
	print_art(message, color)

def print_art(message, color):
	"""
	Receives a message and a color and prints ascii art to the console in the specified color. If color is invalid the user is prompted for the color once more.
	"""
	if color not in valid_colors:
		print(f"\n{color} is an invalid color!")
		prompt_user(message) # reprompt the user for a color, but don't ask them for their message again
		return
	print(colored(message, color=color))

if __name__ == "__main__":
	prompt_user() 






# def print_art(message, color):
# 	try:
# 		print(colored(message, color=color))
# 	except KeyError:
# 		print(f"{color} is an invalid color!\nValid colors include: {valid_colors_string}")

# message = figlet_format(input("What message do you want to print?\n"))
# color = input(f"What color? {valid_colors_string}\n")
# print_art(message, color)
	