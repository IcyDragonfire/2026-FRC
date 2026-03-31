import pandas

# Functions
def num_check(question, num_type="float", exit_code=None):
    """Checks user enters and integer or is more than zero"""

    if num_type == "float":
        error = "Enter an number more than zero\n"
        change_to = int
    else:
        error = "Enter a number more than zero\n"



    while True:

        response = input(question)

        # exit code
        if response == exit_code:
            return response

        try:

            if num_type == "float":
                response = float(response)
            else:
                response = int(response)

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

def get_expenses(exp_type, how_many=1):
    """Gets variable and outputs PANDA string"""

    # Lists for Panda
    all_items = []
    all_amounts = []
    all_dollar_per_item = []

    # expense dictionary
    expenses_dict = {
        "Item": all_items,
        "Amount": all_amounts,
        "$ / Item": all_dollar_per_item,
    }

    # default amount to 1 for fixed expenses and
    # to avoid PEP 8 error for variable expenses
    amount = 1

    # loop to get expenses
    while True:
        item_name = not_blank("Item Name: ")

        # check users enter at least one variable
        if ((exp_type == "variable" and item_name == "xxx")
                and len(all_items) == 0):
            print("You have not entered anything.")
            continue

        elif item_name == "xxx":
            break

        # get item amount <enter> defaults to number of products made

        amount = num_check(f"how many <enter for {how_many}>: ",
                            "integer", "")

        if amount == "":
            amount = how_many

        cost = num_check("Price for one? ", "float")

        all_items.append(item_name)
        all_amounts.append(amount)
        all_dollar_per_item.append(cost)

    # make panda
    expense_frame = pandas.DataFrame(expenses_dict)

    # calculate row cost
    expense_frame['Cost'] = expense_frame['Amount'] * expense_frame['$ / Item']

    # calculate subtotal
    subtotal = expense_frame['Cost'].sum()

    # return all items for now so we can check loop
    return expense_frame, subtotal

    # # return all items for now so we can check loop
    # return all_items


def currency(x):
    return "${:.2f}".format(x)

# Main routine

quantity_made = num_check("Quantity being made: ",
                          "integer")
print()

print("Getting Variable Costs...")
variable_expenses = get_expenses("variable", quantity_made)
print()
variable_panda = variable_expenses[0]
variable_subtotal = variable_expenses[1]

print(variable_panda)
print(variable_subtotal)