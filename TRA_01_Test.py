# Checks if the answer the user puts in is in this list of variables
def magic_option(question, valid_answers):
    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                print(item)
                return item

            # check if it's the first letter
            elif response == item[0]:
                return item

        print(f"Choose an item from {valid_answers}\n")

#
magics = ("shock", "bigbang", "cheat")
yes_no = ("yes", "no")

want_coffee = magic_option("Do  you want coffee? ", yes_no)
question = magic_option("Pick an answer", magics)

# if question == "shock" or question == "s":
#     question = "shock"

print(f"You chose {question}")

