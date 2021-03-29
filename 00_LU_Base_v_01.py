

# Functions go here...
def yes_no(question):
	valid = False
	while not valid: 
		response = input(question).lower()


		if response == "yes" or response == "y":
			response = "yes"
			return response

		elif response == "no" or response == "n":
			response = "no"
			return response

		else:
			print("please answer yes/no")

def instructions():
	print ("**** How to Play ****") 
	print()
	print("The aim of this game is to win a unicron. You will need to enter money in a minium of $1 and a maxiumum of $10. Click <enter> repearedly until you win a unicorn or run out of money. If you lose and dont win a unicorn feel free to play again or click xxx to quit")
	return "" 


def num_check(question, low, high):

	error = "Please enter an whole number between 1 and 10"

	valid = False 
	while not valid:
		try:
			# ask the question
			print()
			response = int(input(question))
			# if the amount is to low / too high give
			if low < response <= high:
				return response

			# output an error
			else:
				print (error)

		except ValueError:
			print(error)

# main Routine goes here...
played_before = yes_no("Have you played the game before?")

if played_before == "no":
	instructions ()
else:
	print ("program continues")

how_much = num_check ("how much would you like to play with?", 0, 10)

print ("You will be spending ${}". format(how_much))


	


