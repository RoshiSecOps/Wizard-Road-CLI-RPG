from Battle_testing import *
from Main_menu import *
from Character_creation import *
import time

player_one = create_character()
first_enemy = Orc("Rengar", 150, 4)
second_enemy = Orc("Rengar's cousin", 150, 4)

def trial_gameplay():
    while player_one.is_alive() == True:
        open_main_menu()
        player_choice = int(input("You choose?( 1 - 5 ): "))
        if player_choice == 1:
            if first_enemy.is_alive() == True:
                full_battle(first_enemy, player_one)
            else:
                full_battle(second_enemy, player_one)
            clear_screen()
        elif player_choice == 2:
            if player_one.get_level() < 2:
                print("Level too low, come back once you are stronger!")
                print("[ Going back to main menu in 2 seconds ]")
                time.sleep(2)
                clear_screen()
        elif player_choice == 3:
            player_one.get_all_stats()
            print(f"Current level [{player_one.get_level()}]")
            print("[ Going back to menu in 2 seconds ]")
            time.sleep(2)
            pause_for_more = int(input("Need more time, how many more seconds?(0 to exit): "))
            time.sleep(pause_for_more)
            clear_screen()
        elif player_choice == 4:
            player_one.heal_full()
            print("[ Going back to menu in 2 second ]")
            time.sleep(1)
            clear_screen()
        elif player_choice == 5:
            print("Exiting")
            return
        else:
            print("Invalid Choice")
            clear_screen()
play_a_game = trial_gameplay()