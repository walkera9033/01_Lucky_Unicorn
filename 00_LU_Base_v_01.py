import random
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
            print("Please answer yes / no")

def instructions():
    print("**** How to play ****")
    print()
    print("In this particular game, your aim to win a unicorn. You have to enter a sum of money with the minimum being $1"
          "and the maximum being $10. "
          "All you have to do is repeatedly press <Enter> till you get a unicorn. ")
    print("Each round costs $1. You win $5 if you get a Unicorn, 50c if you get a horse or zebra. "
          "but if you get a donkey, you will not get anything. ")
    print("If you do not succeed in winning a unicorn, feel free to restart the game or exit with <xxx>."
          )
    return ""

def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"
    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low / too high give
            if low < response <= high:
                return response
            # output an error
            else:
                print(error)
        except ValueError:
            print(error)


def statement_generator(statement, decoration):
    sides = decoration * 3
    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)
    print(top_bottom)
    print(statement)
    print(top_bottom)
    return ""


statement_generator("Welcome to the Lucky Unicorn Game", "*")
print()
# Main Routine goes here...
played_before = yes_no("Have you played the game before? ")
if played_before == "no":
    instructions()
# Ask user how much they want to play with...
how_much = num_check("How much would you like to play with? ", 0, 10)
balance = how_much
rounds_played = 0
play_again = input("Press <Enter> to play...").lower()
while play_again == "":

 # increase # of rounds played
    rounds_played += 1
    # Print round number
    print("*** Round #{} ***".format(rounds_played))
    chosen_num = random.randint(1, 100)
    # Adjust balance
    # if the random # is between 1 and 5,
    # user gets a unicorn (add  $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        chosen_dec = "*"
        balance += 4
    # if the random # is between 6 and 36
    # user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        chosen_dec = "D"
        balance -= 1

				 # The token is either an horse or a zebra...
    # in both cases , subtract $0.5 from the balance
    else:
        # if the number is even then set the chosen
        # item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"
            chosen_dec = "H"
        # otherwise set it to a zebra
        else:
            chosen = "zebra"
            chosen_dec = "Z"
        balance -= 0.5
    feedback = "You got a {}, your balance is ${:.2f}".format(chosen, balance)
    statement_generator(feedback, chosen_dec)
    print()


    if balance < 1:
        # if balance is too low, exit the game and
        # output a suitable message
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        print()
        play_again = input("Push Enter to play or 'xxx' to quit")
print()
print("Final Balance: ${:.2f} ".format(balance))
print("*Thanks For Playing*")