from Human_character_template import Human
from Orc_character import Orc
from Wizard_character import Wizard

test_enemy = Orc("Rengar", 150, 5)
test_player = Wizard("Zoraph", 100, 100, "Fire")

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
