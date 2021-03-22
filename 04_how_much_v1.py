# Functions go here


# Main routine goes here

error = "Please enter an whole number between 1 and 10"

valid = False 
while not valid:
	try:
		# Ask the question 
		response = int(input("How much would you like to play with"))

		# if the amount is too low / too high give 
		if 0 < response <= 10:
			print ("You have asked to play with ${}".format(response))


		# output an error
		else:
			print(error)

	except ValueError:
		print(error)

		

