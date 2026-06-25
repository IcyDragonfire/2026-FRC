# Functions
def int_check(question):
    """ Makes sure number is over 0 """
    while True:
        error = "Enter a valid response"

        to_check = input(question)

        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            if response < 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# checks if answer sais answer in list
def turn_options(question):
    """Checking user answers yes or no (y / n)"""


    while True:
        response = input(question).lower()

        if response == "attack" or "a":
            return "attack"
        elif response == "defend" or "d":
            return "defend"
        elif response == "magic" or "m":
            return "magic"
        elif response == "escape" or "e":
            return "escape"
        else:
            print("pick an option that is viable")

# Variables
rounds = 0




# Choose how many rounds you want and print that number
rounds_wanted = int_check("How many rounds do you want [Enter for Infinite]")
if rounds_wanted == "":
    print("You chose infinite rounds\n")
elif rounds_wanted == "0":
    print("You chose 0 rounds. Program ends.")
else:
    print(f"you chose {rounds_wanted} rounds\n")

# Main Routine
while True:
    if rounds == rounds_wanted:
        break

    print(f"Round: {rounds+1}")

    print("Evil Guy Appeared")

    print("")


    turn_options("Pick an option or press enter to progress to next round\n")



    rounds+= 1

