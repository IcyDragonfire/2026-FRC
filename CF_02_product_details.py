# Functions
def num_check(question, num_type, exit_code=None):
    """Checks user enters and integer or is more than zero"""

    if num_type == "integer":
        error = "Enter an integer more than zero\n"
        change_to = int
    else:
        error = "Enter a number more than zero\n"
        change_to = float


    while True:
        response = input(question).lower()

        # exit code
        if response == exit_code:
            return response

        try:
            # change response to an integer and check it is more than zero
            response = change_to(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def not_blank(question):
    """Checks that the users response isn't blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("You can not make this answer blank. Try again. \n")

def get_expenses(exp_type):
    """Gets variable and outputs PANDA string"""

    # Lists for Panda
    all_items = []

    # expense dictionary

    # loop to get expenses
    while True:
        item_name = not_blank("Item Name: ")

        # check users enter at least one variable
        if (exp_type == "variable" and
            item_name == "xxx") and len(all_items) == 0:
            print("You have not entered anything.")
            continue

        elif item_name == "xxx":
            break

        all_items.append(item_name)

    # return all items for now so we can check loop
    return all_items


def currency(x):
    return "${:.2f}".format(x)

# Main routine

print("Getting Variable Costs...")
variable_expenses = get_expenses("variable")
num_variable = len(variable_expenses)
print(f"You entered {num_variable} items")
print()

# loop for testing
while True:
    product_name = not_blank("Product Name: ")
    quantity_made = num_check("Quantity being made: ", "Integer")
    print(f"You are making {quantity_made} {product_name}")
    print()
