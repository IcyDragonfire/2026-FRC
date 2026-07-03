# Import random for CPU option and import pandas to
# format the statistics at the end
import random
import pandas


# All Functions
def make_statement(decoration, statement, instructions):
    """Emphasise headings by adding decoration"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


def instructions():
    make_statement("🛃", "Instructions", "🛃")

    print('''
EPIC COOL GAME: THE GAME - Instructions

This is a really cool game I think, choose how many rounds you want to play, and then fight the CPU

There are 4 main turn options: Attack Defend Magic and Escape

    Attack does 100 damage to the CPU

    Defend counterattacks if the CPU does a special attack
    
    Magic brings up the Magic option list
    
    Escape quits out of the code entirely
    
There are 3 magic options you can use:

    Shock stuns the Cpu for that turn and does 50 damage
    
    Bigbang does 200 damage
    
    Cheat murders the CPU, like that guy is dead bro
    
Enjoy game, it is cool. Like its literally in the name!


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

# Checks if the answer the user puts in is in this list of variables
def string_check(question, valid_answers):
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


# checks if answer sais answer in list
def country_options(question):
    """Checking user answers something from this string"""

    while True:
        response = input(question).lower()

        if response == "africa" or response == "af":
            return africa
        elif response == "asia" or response == "as":
            return asia
        elif response == "europe" or response == "eu":
            return europe
        elif response == "north america" or response == "na":
            return north_america
        elif response == "south america" or response == "sa":
            return south_america
        elif response == "oceania" or response == "oc":
            return oceania
        else:
            print('''pick an option that is viable out of:

Asia / As
Africa / Af
Europe / Eu
North America / Na
South America / Sa
Oceania / Oc
''')


# Variables, some are set to 0 or "N/A" as a default
player_turn = 0
round_count = 0
enemy_hp = 400
player_hp = 200
stun = 0
magic_select = "N/A"
option = "N/A"

# list names for displaying panda details
round_num = []
turn_num = []
player_opt = []
magic_question = []
cpu_option = []
player_hp_panda = []
enemy_hp_panda = []

# Panda variables that will get appended at the end of each turn
turn_rounds_dict = {
    'Round': round_num,
    'Turn': turn_num,
    'Player option': player_opt,
    'Magic': magic_question,
    'Computer option': cpu_option,
    'Player HP': player_hp_panda,
    'Computer HP': enemy_hp_panda
}

# Magic options list
magics = ("shock", "bigbang", "cheat")
turn_opt = ("attack", "defend", "magic", "escape")

# Country lists for continent questions, data provided by teacher
africa = [
    "Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi",
    "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros",
    "Congo", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea",
    "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea",
    "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar",
    "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique",
    "Namibia", "Niger", "Nigeria", "Rwanda", "Sao Tome and Principe",
    "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa",
    "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda",
    "Zambia", "Zimbabwe"
]

asia = [
    "Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan",
    "Brunei", "Cambodia", "China", "Cyprus", "Georgia", "India", "Indonesia",
    "Iran", "Iraq", "Israel", "Japan", "Jordan", "Kazakhstan", "Kuwait",
    "Kyrgyzstan", "Laos", "Lebanon", "Malaysia", "Maldives", "Mongolia",
    "Myanmar", "Nepal", "North Korea", "Oman", "Pakistan", "Palestine",
    "Philippines", "Qatar", "Saudi Arabia", "Singapore", "South Korea",
    "Sri Lanka", "Syria", "Taiwan", "Tajikistan", "Thailand", "Timor-Leste",
    "Turkey", "Turkmenistan", "United Arab Emirates", "Uzbekistan", "Vietnam", "Yemen"
]

europe = [
    "Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina",
    "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Estonia", "Finland",
    "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy",
    "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova",
    "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland",
    "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia",
    "Slovenia", "Spain", "Sweden", "Switzerland", "Ukraine", "United Kingdom", "Vatican City"
]

north_america = [
    "Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Canada", "Costa Rica",
    "Cuba", "Dominica", "Dominican Republic", "El Salvador", "Grenada", "Guatemala",
    "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Saint Kitts and Nevis",
    "Saint Lucia", "Saint Vincent and the Grenadines", "Trinidad and Tobago", "United States"
]

south_america = [
    "Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana",
    "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"
]

oceania = [
    "Australia", "Fiji", "Kiribati", "Marshall Islands", "Micronesia", "Nauru",
    "New Zealand", "Palau", "Papua New Guinea", "Samoa", "Solomon Islands",
    "Tonga", "Tuvalu", "Vanuatu"]

all_lists = ["africa", "asia", "europe", "north america", "south america", "oceania"]

# main routine
want_instructions = yes_no("Do you want Instructions? ")

print()
if want_instructions == "yes":
    instructions()
else:
    print("No instructions\n")

# Choose how many rounds you want and print that number
rounds_wanted = int_check("How many rounds do you want [Enter for Infinite]")
if rounds_wanted == "":
    print("You chose infinite rounds\n")
elif rounds_wanted == "0":
    print("You chose 0 rounds. Program ends.")
else:
    print(f"you chose {rounds_wanted} rounds\n")

# Start of round
while True:

    # breaks code if Round count = rounds wanted
    # Or if Player HP is 0 or less
    print("Start of new round")
    if round_count == rounds_wanted:
        break
    if player_hp <= 0:
        print("You died")
        break
    # Initialise values at the start of the round
    enemy_hp = 400
    player_turn = 0

    # Start of turn
    while True:
        magic_select = "N/A"

        # Initialise values at the start of the turn
        stun = 0
        defense = 0

        print("start of turn")
        # choose a list
        list_name = random.choice(all_lists)

        # choose an item in the chosen list
        question = random.choice(list_name)

        # define list names into text
        if list_name == "africa":
            list = africa
        elif list_name == "asia":
            list = asia
        elif list_name == "europe":
            list = europe
        elif list_name == "north america":
            list = north_america
        elif list_name == "south america":
            list = south_america
        elif list_name == "oceania":
            list = oceania
        else:
            list = "did not work"

        # Picks the random country
        random_country = random.choice(list)

        # append variables for panda if the CPUs HP is zero
        if enemy_hp <= 0:
            enemy_hp = 0
            enemy_option = "N/A"
            print("enemy has died\n")
            round_num.append(round_count + 1)
            turn_num.append(player_turn + 1)
            player_opt.append(option)
            magic_question.append(magic_select)
            cpu_option.append(enemy_option)
            player_hp_panda.append(player_hp)
            enemy_hp_panda.append(enemy_hp)
            break
        cpu_rand_turn = random.randint(1, 3)

        # Defines what action the CPU will use for the turn
        if cpu_rand_turn == 1:
            enemy_option = "attack"
        elif cpu_rand_turn == 2:
            enemy_option = "special attack"
        else:
            enemy_option = "heal"

        # Display of Round, Turn, Player hp and CPU hp
        print(f"🛃🛃🛃 Round: {round_count + 1} "
              f"- Turn: {player_turn + 1} "
              f"- Enemy HP: {enemy_hp} - Your HP: {player_hp}\n")

        print("")

        print(f"{cpu_rand_turn}")

        # Player turn
        option = string_check('''     Player Turn: 
    (attack / a) (defend / d)
    (magic / m) (escape / e) \n''', turn_opt)
        print(f"You chose {option}")
        match option:
            case "attack":
                print("You Attacked \n")
                enemy_hp -= 100
                print(f"Enemy HP: {enemy_hp}\n")
            case "defend":
                print("You defended \n")
                defense = 1
            case "magic":
                print("Answer a question correctly to use a magic attack\n")
                country_answer = country_options(f"What continent is {random_country} in? ")

                # Checks if the country answer is in the list,
                # Then if it is correct, let them proceed to picking magic option
                if country_answer == list:
                    print(f"Yes, {random_country} is in {list_name}\n")
                    print()
                    # Magic option, also makes sure you pick the right option
                    magic_select = string_check('''What magic option will you pick?
(shock / s) (bigbang / b) (Cheat / c) ''', magics)
                    match magic_select:
                        case "shock":
                            print(f"you chose {magic_select}, -50 CPU HP")
                            enemy_hp -= 50
                            stun = 1
                    match magic_select:
                        case "bigbang":
                            print(f"you chose {magic_select}, -200 CPU HP")
                            enemy_hp -= 200
                    match magic_select:
                        case "cheat":
                            print(f"you chose {magic_select}, CPU dies")
                            enemy_hp -= 10000

                else:
                    print("You are WRONG")

                print("")
            case "escape":
                print("You successfully escaped \n")
                quit()

        # Checks if the CPUs Health Points are zero or below
        if enemy_hp <= 0:
            enemy_hp = 0
            enemy_option = "N/A"
            round_num.append(round_count + 1)
            turn_num.append(player_turn + 1)
            player_opt.append(option)
            magic_question.append(magic_select)
            cpu_option.append(enemy_option)
            player_hp_panda.append(player_hp)
            enemy_hp_panda.append(enemy_hp)
            break

        # Checks if the player has selected the stun magic, and if so,
        # CPUs turn and append variables to panda
        if stun == 1:
            enemy_option = "N/A"
            round_num.append(round_count + 1)
            turn_num.append(player_turn + 1)
            player_opt.append(option)
            magic_question.append(magic_select)
            cpu_option.append(enemy_option)
            player_hp_panda.append(player_hp)
            enemy_hp_panda.append(enemy_hp)
            player_turn += 1
            continue

        # Start of the CPUs turn
        print("     CPU Turn: ")
        if cpu_rand_turn == 1:
            print("CPU attacked")
            player_hp -= 100
            print(f"Your HP is now {player_hp}")
        elif cpu_rand_turn == 2:
            print("CPU Preformed a special attack")
            if defense == 0:
                player_hp -= 50
            else:
                print('''
                You counterattacked.

CPU loses HP\n''')
                enemy_hp -= 150
                print(f"CPU HP: {enemy_hp}")
            print(f"Your HP is now {player_hp}\n")
        else:
            print("CPU regained 50 HP")
            enemy_hp += 50
            print(f"CPU HP: {enemy_hp}\n")



        # end of turn, append all variables to panda
        round_num.append(round_count+1)
        turn_num.append(player_turn+1)
        player_opt.append(option)
        magic_question.append(magic_select)
        cpu_option.append(enemy_option)
        player_hp_panda.append(player_hp)
        enemy_hp_panda.append(enemy_hp)

        if player_hp <= 0:
            break

        print("")

        # Adds player HP to go up so the user doesn't die in two
        # hits by the CPU, resets stun variable so CPU doesn't get
        # stunned the next turn, and also makes the turn count go up
        player_hp += 10
        stun = 0
        player_turn += 1


    # end of round / add round count number by 1
    round_count += 1


    # Makes the player regain a good amount of HP if they are still
    # alive, and the CPU is dead
    if player_hp >= 1:
        player_hp += 150

# Create Dataframe / Table from dictionary
game_frame = pandas.DataFrame(turn_rounds_dict)

# print out the statistics at the end - Panda
print(game_frame)
