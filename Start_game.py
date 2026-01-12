from Battle_testing import *
from Main_menu import *
from Character_creation import *

player_one = create_character()
first_enemy = Orc("Rengar", 150, 4)

def trial_gameplay():
    open_main_menu()
    player_choice = int(input("You choose?(1-4): "))
    if player_choice == 1:
        full_battle(first_enemy, player_one)

trial_gameplay()