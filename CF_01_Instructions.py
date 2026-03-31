# Functions go here
def make_statement(statement, decoration):
    """Emphasise headings by adding decoration"""

    print(f"{decoration * 3} {statement} {decoration * 3}")

def string_check(question, valid_answers=('yes', 'no'), num_letters=1):

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's in the 'n' letters
            elif response == item[:num_letters]:
                return item

        print(f"Choose an item from {valid_answers}\n")

def instructions():
    make_statement("Instructions", "🛃")

    print('''

These are my instructions, and I have not written them yet

''')

# Main routine

# ask user if they want to see the instructions
# display them if necessary
print()
want_instructions = string_check("Do you want Instructions? ")

if want_instructions == "yes":
    instructions()

print()