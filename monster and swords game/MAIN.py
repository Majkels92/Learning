from menu import *


if __name__ == "__main__":
    greeting()
    player_choice = input("""Type:
     START GAME - type 's' to begin your journey
     CONTINUE GAME - type 'c' to begin your journey """)
    status = True
    while status is True:
        if player_choice == "s":
            player, backpack, player_sack = create_character()
            in_game_menu(player, player_sack, backpack)
            status = False
        elif player_choice == "c":
            print("This feature is not working yet")
        else:
            player_choice = input("""Type 'start game' to begin your journey""")


