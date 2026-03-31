import pandas
from tabulate import tabulate
from datetime import date
import math


# Functions
def make_statement(statement, decoration):
    return (f"{decoration * 3} {statement} {decoration * 3}")

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

def string_check(question, valid_answers=('yes', 'no'),
                 num_letters=1):

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
    amount = how_many   # How_many defaults to 1
    how_much_question = "How much? $"

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

        if exp_type == "variable":
            amount = num_check(f"how many <enter for {how_many}>: ",
                                "integer", "")

            if amount == "":
                amount = how_many

        cost = num_check("Price for one? ", "float")

        print()

        all_items.append(item_name)
        all_amounts.append(amount)
        all_dollar_per_item.append(cost)

    # make panda
    expense_frame = pandas.DataFrame(expenses_dict)

    # calculate row cost
    expense_frame['Cost'] = expense_frame['Amount'] * expense_frame['$ / Item']

    # calculate subtotal
    subtotal = expense_frame['Cost'].sum()

    # apply currency formatting to currency columns.
    add_dollars = ['$ / Item', 'Cost']
    for var_item in add_dollars:
        expense_frame[var_item] = expense_frame[var_item].apply(currency)

    # make expense frame into a string with the desired columns
    if exp_type == "variable":
        expense_string = tabulate(expense_frame, headers='keys',
                                  tablefmt='psql', showindex=False)
    else:
        expense_string = tabulate(expense_frame[['Item', 'Cost']], headers='keys',
                                  tablefmt='psql', showindex=False)

    # return all items for now so we can check loop
    return expense_string, subtotal

def currency(x):
    return "${:.2f}".format(x)

def profit_goal(total_costs):
    """Calculates profit goal work out profit goal and total sales required"""

    error = "Enter a valid profit goal"

    valid = False
    while not valid:

        # ask for profit goal
        response = input("What is your profit goal (eg $500 or 50%")

        # check is character is $
        if response[0] == "$":
            profit_type = "$"
            # get amount (everything after the $)
            amount = response[1:]

        # check if last character is %
        elif response[-1] == "%":
            profit_type = "%"
            # get amount (everything after the %)
            amount = response[:-1]

        # check if last character is %
        elif response[-1] == "%":
            profit_type = "%"
            # get amount (everything before the %
            amount = response[:-1]

        else:
            # set response to amount for now
            profit_type = "unknown"
            amount = response

        try:
            # check amount is a number more than zero
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

        if profit_type == "unknown" and amount >= 100:
            dollar_type = string_check(f"do you mean ${amount:.2f}.   ie {amount:.2f} dollars? ,")

            # set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = string_check(f"Do you mean {amount}%? , Y / N: ")
            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        # return profit goal to main routine
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal

def round_up(amount, round_val):
    """Rounds amount to desired hole number"""
    return int(math.ceil(amount / round_val)) * round_val


# Main routine

# initialise variables

# assume we have no fixed expenses for now
fixed_subtotal = 0
fixed_panda_string = ""

print(make_statement("Fundraising Calculator", "🛃"))

print()
want_instructions = string_check("Do you want to see the instructions")
print()

if want_instructions == "yes":
    instructions()

print()

# get product details
product_name = not_blank("Product Name: ")
quantity_made = num_check("Quantity being made: ", "integer")

# get variable expenses...
print("Let's get the variable expenses....")
variable_expenses = get_expenses("variable", quantity_made)

variable_panda_string = variable_expenses[0]
variable_subtotal = variable_expenses[1]

print()

# ask user if they have fixed expenses and retrieve them
print()
has_fixed = string_check("Do you have fixed expenses ")

if has_fixed == "yes":
    fixed_expenses = get_expenses("fixed")

    fixed_panda_string = fixed_expenses[0]
    fixed_subtotal = fixed_expenses[1]

    # if user has not entered any fixed expenses,
    # set empty panda to "" so that it does not display
    if fixed_subtotal == 0:
        has_fixed = "no"
        fixed_panda_string = ""

total_expenses = variable_subtotal + fixed_subtotal
total_expenses_string = f"Total Expenses: ${total_expenses:.2f}"


# get profit goal here
target = profit_goal(total_expenses)
sales_target = total_expenses + target

# Calculate minimum selling price and round
# it to nearest desired dollar amount
selling_price = (total_expenses + target) / quantity_made
round_to = num_check("Round to: ", 'integer')
suggested_price = round_up(selling_price, round_to)

# strings / output area

# **** get current date for heading and filename ****
today = date.today()

# get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

# headings / strings...
main_heading_string = make_statement(f"Fundraising Calculator "
                                     f"({product_name}, {day}/{month}/{year})", "=")
quantity_string = f"Quantity being made: {quantity_made}"
variable_heading_string = make_statement("variable expenses", "-")
variable_subtotal_string = f"variable expenses subtotal: ${variable_subtotal:.2f}"

# set up strings if we have fixed costs
if has_fixed == "yes":
    fixed_heading_string = make_statement("Fixed Expenses", "-")
    fixed_subtotal_string = f"Fixed Expenses Subtotal: {fixed_subtotal:.2f}"

# set fixed cost strings to blank if we don't have fixed costs
else:
    fixed_heading_string = make_statement("You have no fixed expenses", "-")
    fixed_subtotal_string = "Fixed expenses subtotal: $0.00"

selling_price_heading = make_statement("Selling Price Calculations", '#')
profit_goal_string = f"Profit Goal: ${target:.2f}"
sales_target_string = f"\nTotal Sales Needed: ${sales_target:.2f}"

minimum_price_string = f"Minimum Selling Price: ${selling_price:.2f}"
suggested_price_string = make_statement(f"Suggested Selling Price: "
                                        f"${suggested_price:.2f}", "*")

# list of strings to be outputted / written to file
to_write = [main_heading_string, quantity_string,
            "\n", variable_heading_string, variable_panda_string,
            variable_subtotal_string,
            "\n", fixed_heading_string, fixed_panda_string,
            fixed_subtotal_string, total_expenses_string]

# print area
print()
for item in to_write:
    print(item)

# create file to hold data (add .txt extension)
file_name = f"{product_name}_{year}_{month}_{day}"
write_to = "{}.txt" .format(file_name)

text_file = open(write_to, "w+")

# write the item to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")
    