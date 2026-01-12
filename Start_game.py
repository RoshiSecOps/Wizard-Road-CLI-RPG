from Battle_testing import *
from Main_menu import *
from Character_creation import *

player_one = create_character()
first_enemy = Orc("Rengar", 150, 4)

def trial_gameplay():
    while player_one.is_alive() == True:
        open_main_menu()
        player_choice = int(input("You choose?(1-4): "))
        if player_choice == 1:
            full_battle(first_enemy, player_one)
        elif player_choice == 2:
            return "Work in progress"
        elif player_choice == 3:
            return player_one.get_all_stats()
        elif player_choice == 4:
            return "Exiting"
        else:
            return "Invalid Choice"

play_a_game = trial_gameplay()
print(play_a_game)