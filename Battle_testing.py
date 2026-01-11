from Human_character_template import Human
from Orc_character import Orc
from Wizard_character import Wizard

test_enemy = Orc("Rengar", 150, 5)
test_player = Wizard("Zoraph", 100, 100, "Fire")

player_actions = [f"Cast {test_player.get_offensive_spell_name()}", "Skip turn", "Rest"]
enemy_actions = ["Attack", "Rest", "Skip turn"]

player_actions_bar = ""
enemy_actions_bar = ""

for action in player_actions:
    player_actions_bar += f"[{player_actions.index(action) + 1} : {action}]"

for action in enemy_actions:
    enemy_actions_bar += f"[{enemy_actions.index(action) + 1} : {action}]"

print("\n-------------------------------------")
print("player1")
test_player.get_all_stats()

print("\n-------------------------------------")
print("enemy1")
test_enemy.get_all_stats()

test_enemy.melee_attack(test_player)

print("\n-------------------------------------")

test_player.cast_offensive_spell(test_enemy)

print(test_enemy.get_health())

def player_turn(player, possible_actions, enemy):
    print(f"Your turn {player.get_name()}, please choose an action")
    print(possible_actions)
    choice = int(input("Choice: "))
    if choice == 1:
        player.cast_offensive_spell(enemy)
        print(f"{enemy.get_name()} hase {enemy.get_health()} Health left!")
    elif choice == 2:
        print("You skipped")
    elif choice == 3:
        player.rest_turn()
    else:
        print("Invalid choice!")

# To finish enemy turn, choices will be made based on current health or random roll.
def enemy_turn(monster, possible_actions, enemy):
    print(f"{monster.get_name()} the orc's turn!")
    print(possible_actions)
    if monster.get_heath() > 80:
        monster.melee_attack(enemy)
        print(f"{enemy.get_name()} hase {enemy.get_health()} Health left!")
    elif choice == 2:
        print("You skipped")
    elif choice == 3:
        enemy.rest_turn()
    else:
        print("Invalid choice!")

player_turn(test_player, player_actions_bar, test_enemy)