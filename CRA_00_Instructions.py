def make_statement(decoration, statement, instructions):
    """Emphasise headings by adding decoration"""

    print(f"{decoration * 3} {statement} {decoration * 3}")

def instructions():
    make_statement("🛃", "Instructions", "🛃")

    print('''
    
You are playing a super awesome scoreboard game where there is a scoreboard

There is rounds and you want to get more points than your opponent (Evil Computer)



    ''')

def yes_no(question):
    """Checking user answers yes or no (y / n)"""


    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print()
            print("Input a yes or no answer.\n")

# Main routine

print()
want_instructions = yes_no("Do you want Instructions? ")

print()
if want_instructions == "yes":
    instructions()
else:
    print("No instructions")