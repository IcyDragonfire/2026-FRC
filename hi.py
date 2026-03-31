num_check = 3425
get_expenses = "sdfgfdgfdsg"
quantity_made = num_check("Quantity being made: ",
                          "integer")
print()

print("Getting Variable Costs...")
variable_expenses = get_expenses("variable", quantity_made)
print()
variable_panda = variable_expenses[0]
variable_subtotal = variable_expenses[1]

print("Getting Fixed Costs...")
fixed_expenses = get_expenses("fixed")
print()
fixed_panda = get_expenses[0]
fixed_subtotal = fixed_panda[0]

# Temporary output area (for easy testing)

print("=== Variable Expenses ===")
print(variable_panda)
print(f"Fixed Subtotal: ${fixed_subtotal:.2f}")

print("=== Fixed Expenses ===")
print(fixed_panda)
print(f"Fixed Subtotal: ${fixed_subtotal:.2f}")

print()
total_expenses = variable_subtotal + fixed_subtotal
print(f"Total Expenses: ${total_expenses:.2f}")