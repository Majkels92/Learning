from characters import *
import locations, actions, containers, bubble_sort_backpack


def greeting():
    print("WELCOME MIGHTY TRAVELER INTO MAGIC AND FULL OF ADVENTURES GAME\n\n")


def create_character():
    print("Hmmm...now let's create your character...")
    chosen_name = input("What is your name ?")
    player = Creature(name=chosen_name)
    print(f"Now my dear {chosen_name} let's begin your battle for better tomorrow")
    player.weapon_in_hand = Weapons(20, 2.0)
    backpack = containers.Backpack()
    player_sack = containers.GoldSack()
    return player, backpack, player_sack


def inside_location_menu(player, player_sack, backpack):
    player_location_move = input("""Which path will u take? left(1) - it's easy, right(2) or middle(3) - it's hell?
    Or maybe u want to flee(4) and return to your Camp.""")
    if player_location_move == '1' or player_location_move == 'left':
        enemy = locations.LocationPaths.easy_encounter()
        actions.Fight.fight(player, enemy, player_sack, backpack)
        inside_location_menu(player, player_sack, backpack)
    elif player_location_move == '2' or player_location_move == 'right':
        enemy = locations.LocationPaths.medium_encounter()
        actions.Fight.fight(player, enemy, player_sack, backpack)
        inside_location_menu(player, player_sack, backpack)
    elif player_location_move == '3' or player_location_move == 'middle':
        enemy = locations.LocationPaths.hard_encounter()
        actions.Fight.fight(player, enemy, player_sack, backpack)
        inside_location_menu(player, player_sack, backpack)
    elif player_location_move == '4' or player_location_move == 'flee':
        locations.Camp.entrance_description()
        in_game_menu(player, player_sack, backpack)
        inside_location_menu(player, player_sack, backpack)
    else:
        inside_location_menu(player, player_sack, backpack)


def backpack_menu(player, player_sack, backpack):
    backpack_move = input("""What do you want to do?
    show what is in backpack - type: 1
    withdraw from back pack - type: 2
    sort items in backpack - type: 3
    return to previous menu - type: 4""")
    if backpack_move == '1':
        backpack.show_slots()
        backpack_menu(player, player_sack, backpack)
    elif backpack_move == '2':
        slot_index = int(input("which slot ?"))
        backpack.withdraw_item_from_slot(slot_index)
        backpack_menu(player, player_sack, backpack)
    elif backpack_move == '3':
        bubble_sort_backpack.bubble_sorting(backpack.backpack_slots)
        backpack_menu(player, player_sack, backpack)
    elif backpack_move == '4':
        in_game_menu(player, player_sack, backpack)
    else:
        backpack_menu(player, player_sack, backpack)


def in_game_menu(player, player_sack, backpack):
    player_move = input("""What do you want to do?
    explore Marhaba Desert - type: 1
    explore Forest - type: 2
    explore Dark Cave - type: 3
    check your stats - type: 4
    show your backpack - type 5:
    exit game - type: exit""")
    if player_move == '1':
        locations.MarhabaDesert.entrance_description()
        inside_location_menu(player, player_sack, backpack)
    elif player_move == '2':
        locations.Forest.entrance_description()
        inside_location_menu(player, player_sack, backpack)
    elif player_move == '3':
        locations.DarkCave.entrance_description()
        inside_location_menu(player, player_sack, backpack)
    elif player_move == '4':
        player.show_stats()
    elif player_move == '5':
        backpack_menu(player, player_sack, backpack)
    elif player_move == 'exit':
        input('press ENTER to exit')
        exit()
    else:
        print("You can't go there...")
        in_game_menu(player, player_sack, backpack)



