
def string_check(question, valid_answers=('yes', 'no'), num_letters=1):
    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                print(item[:num_letters])
                return item

            # check if it's in the 'n' letters
            elif response == item[:num_letters]:
                return item

        print(f"Choose an item from {valid_answers}\n")

payment = ("cash", "credit", "ca", "cr")

like_cs = string_check("do you like cs?")
print("you chose", like_cs)

pay = string_check("choose a payment method", payment, 2)
if pay == "cash" or pay == "ca":
    pay = "cash"

print("pay method", pay)

