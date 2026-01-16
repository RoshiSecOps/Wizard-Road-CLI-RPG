from Human_character_template import Human
from Orc_character import Orc
from Wizard_character import Wizard
import time

def create_user_actions(test_player, buff, heal):
    player_actions = [f"Cast {test_player.get_offensive_spell_name()}", "Skip turn", "Rest"]
    player_actions_bar = ""
    for action in player_actions:
        player_actions_bar += f"[{player_actions.index(action) + 1} : {action}]"
    if test_player.can_buff() == True and test_player.can_heal() == True:
        player_actions_bar = player_actions_bar + f"[4: {buff.get_name()}] [5: {heal.get_name()}]"
    return player_actions_bar

def create_enemy_actions():
    enemy_actions = ["Attack", "Rest"]
    enemy_actions_bar = ""
    for action in enemy_actions:
        enemy_actions_bar += f"[{enemy_actions.index(action) + 1} : {action}]"
    return enemy_actions_bar

def player_turn(player, enemy, buff, heal):
    print("<------------------------------------------------------>")
    print(f"Your turn {player.get_name()}, please choose an action")
    possible_actions = create_user_actions(player, buff, heal)
    print(possible_actions)
    choice = int(input("Choice: "))
    if choice == 1:
        player.cast_offensive_spell(enemy)
        print(f"{enemy.get_name()} has {enemy.get_health()} Health left!")
    elif choice == 2:
        print("You skipped")
    elif choice == 3:
        player.rest_turn(10)
    elif choice == 4:
        if player.can_buff() == True:
            buff.cast_spell(player)
        else:
            print("Spell not unlocked")
    elif choice == 5:
        if player.can_heal() == True:
            heal.cast_spell(player)
            print(f"Current health {player.get_health()}")
        else:
            print("Spell not unlocked")
    else:
        print("Invalid choice!")

def enemy_turn(monster, enemy):
    if monster.is_alive() == False:
        return
    print("<------------------------------------------------------>")
    print(f"{monster.get_name()} the {monster.get_race()}'s turn!")
    possible_actions = create_enemy_actions()
    print(possible_actions)
    if monster.get_health() > 30:
        monster.melee_attack(enemy)
        print(f"{enemy.get_name()} has {enemy.get_health()} Health left!")
    else:
        monster.rest_turn(20)
        print(f"{monster.get_name()} has rested to heal. Current health {monster.get_health()}.")

def full_battle(test_enemy, test_player, buff, heal):
    while True:
        if test_enemy.is_alive() == False:
            test_player.level_up()
            print(f"{test_player.get_name()} has defeated {test_enemy.get_name()}!")
            print("<------------------------------------------------------>")
            print(f"Player is now level {test_player.get_level()}, going back to main menu in 2 seconds.")
            time.sleep(2)
            break
        elif test_player.is_alive() == False:
            print(f"{test_player.get_name()} has perished...")
            break
        else:
            player_turn(test_player, test_enemy, buff, heal)
            time.sleep(1)
            enemy_turn(test_enemy, test_player)
            time.sleep(1)
    return False

