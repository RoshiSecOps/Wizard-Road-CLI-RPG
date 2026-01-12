from Human_character_template import Human
from Orc_character import Orc
from Wizard_character import Wizard

test_enemy = Orc("Rengar", 150, 4)
test_player = Wizard("Zoraph", 100, 100, "Fire")

player_actions = [f"Cast {test_player.get_offensive_spell_name()}", "Skip turn", "Rest"]
enemy_actions = ["Attack", "Rest"]

player_actions_bar = ""
enemy_actions_bar = ""

for action in player_actions:
    player_actions_bar += f"[{player_actions.index(action) + 1} : {action}]"

for action in enemy_actions:
    enemy_actions_bar += f"[{enemy_actions.index(action) + 1} : {action}]"

def player_turn(player, possible_actions, enemy):
    print("<------------------------------------------------------>")
    print(f"Your turn {player.get_name()}, please choose an action")
    print(possible_actions)
    choice = int(input("Choice: "))
    if choice == 1:
        player.cast_offensive_spell(enemy)
        print(f"{enemy.get_name()} has {enemy.get_health()} Health left!")
    elif choice == 2:
        print("You skipped")
    elif choice == 3:
        player.rest_turn(10)
    else:
        print("Invalid choice!")

def enemy_turn(monster, possible_actions, enemy):
    if monster.is_alive() == False:
        return
    print("<------------------------------------------------------>")
    print(f"{monster.get_name()} the {monster.get_race()}'s turn!")
    print(possible_actions)
    if monster.get_health() > 70:
        monster.melee_attack(enemy)
        print(f"{enemy.get_name()} has {enemy.get_health()} Health left!")
    else:
        monster.rest_turn(20)
        print(f"{monster.get_name()} has rested to heal. Current health {monster.get_health()}.")

def full_battle(test_enemy, enemy_actions_bar, test_player):
    while True:
        if test_enemy.is_alive() == False:
            print(f"{test_player.get_name()} has defeated {test_enemy.get_name()}!")
            break
        elif test_player.is_alive() == False:
            print(f"{test_player.get_name()} has perished...")
            break
        else:
            player_turn(test_player, player_actions_bar, test_enemy)
            enemy_turn(test_enemy, enemy_actions_bar, test_player)
    return

full_battle(test_enemy, enemy_actions_bar, test_player)