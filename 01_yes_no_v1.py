show_instructions = ""
while show_instructions.lower() !="xxx":
	# Ask the user if they have played before
	show_instructions = input ("Have you played this game before? ").lower()

	#if they say yes, output 'program continues'
	#if they say no, output 'display instructions'
	#if the answer is invalid, print an answer.

	if show_instructions == "yes" or show_instructions == "y":
		show_instructions = "yes"
		print("program continues")

	elif show_instructions == "no" or show_instructions == "n":
		show_instructions = "no"
		print("display instructions")

	else:
		print("please answer yes/no")

	print()
	print("You chose {}".format(show_instructions))


print("this is the right file")