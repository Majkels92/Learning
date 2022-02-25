from menu import *


if __name__ == "__main__":
    greeting()
    player_choice = input("""Type 'start game' to begin your journey""")
    status = True
    while status is True:
        if player_choice == "start game":
            player, backpack, player_sack = create_character()
            in_game_menu(player, player_sack, backpack)
            status = False
        else:
            player_choice = input("""Type 'start game' to begin your journey""")


