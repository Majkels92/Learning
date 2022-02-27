import random
import validators
import time


class ActionsFight:
    """Actions connected with fight"""

    @staticmethod
    def attack(weapon, creature):
        hit = weapon.weapon_damage_output()
        multiplier = weapon._attack_speed
        hp_loss = hit*multiplier + creature.player_basic_attack  # damage from attack
        return int(hp_loss)

    @staticmethod
    def evade_attack(character):
        chance_to_evade = character.evasion/100
        result = round(random.uniform(0, 1), 2)
        if chance_to_evade >= result:
            evade = True
        else:
            evade = False
        return evade


class Actions:

    # method transferring dropped gold from beaten enemy or opened chest to chosen sack (usually player's)
    @staticmethod
    def loot_gold(looted_obj, sack):
        sack.put_gold_into_sack(looted_obj.gold_drop)

    @staticmethod
    def loot_chest(chest_source, sack, backpack):
        chest_source.chest_drop.open_chest(sack, backpack)

    @staticmethod
    def gain_experience(player, experience_source):
        player.experience += experience_source.gained_experience
        print(f"You gained {experience_source.gained_experience} EXP")
        player.leveling_method()


class Fight:

    # method simulating fight, if player win fight, gives him dropped gold from nemesis
    @staticmethod
    def fight(player, enemy, player_sack, backpack):
        player_hp = player._health_points
        enemy_hp = enemy._health_points
        print("FIGHT BEGINS:")
        time.sleep(1)
        while player.alive is True or enemy.alive is True:
            hit = ActionsFight.attack(player.weapon_in_hand, player)
            print(f"You hit for {hit} hp")
            if ActionsFight.evade_attack(enemy) is True:
                print(f"Attack evaded")
            else:
                enemy_hp = validators.subtraction_n_change_below_0(enemy_hp, hit)
            time.sleep(0.3)
            print(f"ENEMY has {enemy_hp} HP left.")
            time.sleep(1)
            if enemy_hp <= 0:
                enemy.alive = False
                break
            hit = ActionsFight.attack(enemy.weapon_in_hand, enemy)
            print(f"Enemy hit for {hit} hp")
            if ActionsFight.evade_attack(player) is True:
                print(f"Attack evaded")
            else:
                player_hp = validators.subtraction_n_change_below_0(player_hp, hit)
            time.sleep(0.3)
            print(f"YOU have {player_hp} HP left.")
            time.sleep(1)
            if player_hp <= 0:
                player.alive = False
                break
        if player.alive is False:
            print("You died, GAME OVER")
            exit()
        else:
            print("You won fight!")
            if enemy.chest_drop is not None:
                Actions.loot_chest(enemy, player_sack, backpack)
            Actions.loot_gold(enemy, player_sack)
            Actions.gain_experience(player, enemy)
