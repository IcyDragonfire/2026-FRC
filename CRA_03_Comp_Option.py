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
player_turn = 0
round_count = 0
enemy_hp = 400
player_hp = 200

# Choose how many rounds you want and print that number
rounds_wanted = int_check("How many rounds do you want [Enter for Infinite]")
if rounds_wanted == "":
    print("You chose infinite rounds\n")
elif rounds_wanted == "0":
    print("You chose 0 rounds. Program ends.")
else:
    print(f"you chose {rounds_wanted} rounds\n")

# Main Routine

#Start of round
while True:
    if round_count == rounds_wanted:
        break
    if player_hp <= 0:
        print("You died")
        break
    enemy_hp = 400
    player_turn = 0
    # Start of turn
    while True:
        defense = 0
        if enemy_hp <= 0:
            print("enemy has died\n")
            break
        cpu_rand_turn = random.randint(1, 3)

        print(f"🛃🛃🛃 Round: {round_count + 1} "
              f"- Turn: {player_turn + 1} "
              f"- Enemy HP: {enemy_hp} - Your HP: {player_hp}\n")

        print("Stuff question country idk lmao")

        print("")

        print(f"{cpu_rand_turn}")

        # Player turn
        option = turn_options("     Player Turn: \n")
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
                print("(magic option menu) \n")
            case "escape":
                print("You tried to escape \n")

        if enemy_hp <= 0:
            break

        # CPU turn
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

        if player_hp <= 0:
            break

        print("")

        player_turn += 1

    round_count += 1

    # make sure player doesn't get HP restored if they are dead
    if player_hp >= 1:
        player_hp += 150
