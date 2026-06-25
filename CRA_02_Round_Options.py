import random

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
    """Checking user answers something from this string"""


    while True:
        response = input(question).lower()

        if response == "attack" or response == "a":
            return "attack"
        elif response == "defend" or response == "d":
            return "defend"
        elif response == "magic" or response == "m":
            return "magic"
        elif response == "escape" or response == "e":
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

    print("Stuff question country idk lmao")

    print("")


    option = turn_options("Pick an option or press enter to progress to next round\n")
    print(f"You chose {option}")
    match option:
        case "attack":
            print("You Attacked \n")
        case "defend":
            print("You defended \n")
        case "magic":
            print("(magic option menu) \n")
        case "escape":
            print("You tried to escape \n")

    rounds+= 1

