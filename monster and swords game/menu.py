def greeting():
    print("WELCOME MIGHTY TRAVELER INTO MAGIC AND FULL OF ADVENTURES GAME\n\n")

def create_character():
    pass

def main_menu():
    player_choice = input("""Type 'start game' to begin your journey""")
    if player_choice == "start game":
        create_character()
    else:
        print("This action does not exist, boy!")

def game_menu():
    player_move = input("What you want to do?")
    if player_move == 1:
        pass
    elif player_move == 2:
        pass
    elif player_move == 3:
        pass