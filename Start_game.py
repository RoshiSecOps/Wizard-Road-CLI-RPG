from Battle_testing import *
from Main_menu import *
from Character_creation import *
from Spell_book import *
import time

frost_crit = frost_spell_chill("Chill", "Your next Frost bolt will have it's damage tripled",0)
frost_heal = frost_spell_iceblock("Ice Block", "Surround yourself in a block of ICE, healing for 60 points", 60)

fire_crit = fire_spell_combustion("Combustion", "Combust, dealing critical damage on your next attack!",0)
fire_heal = fire_spell_goldenflame("Golden Flames", "Engulf in golden flames, healing for 60 points", 60)

lightning_crit = lightning_spell_thundering("Thundering", "Call forth the thunder! Damage of next attack is tripled!",0)
lightning_heal = lightning_spell_flashheal("Flash Heal", "Call forth a flash of lightning that heals you for 60 points", 60)

Frost_spell_book = [frost_crit, frost_heal]
Fire_spell_book = [fire_crit, fire_heal]
Lightning_spell_book = [lightning_crit, lightning_heal]

player_one = create_character()
first_enemy = Orc("Rengar", 150, 4)
second_enemy = Orc("Rengar's cousin", 150, 4)

def trial_gameplay():
    while player_one.is_alive() == True:
        open_main_menu()
        player_choice = int(input("You choose?( 1 - 5 ): "))
        if player_choice == 1:
            if first_enemy.is_alive() == True:
                print(f"{player_one.get_name()} is fighting {first_enemy.get_name()}, fight starts in 2 seconds!")
                time.sleep(2)
                full_battle(first_enemy, player_one)
            else:
                print(f"{player_one.get_name()} is fighting {second_enemy.get_name()}, fight starts in 2 seconds!")
                time.sleep(2)
                full_battle(second_enemy, player_one)
            clear_screen()
        elif player_choice == 2:
            if player_one.get_level() < 2:
                print("Level too low, come back once you are stronger!")
                print("[ Going back to main menu in 2 seconds ]")
                time.sleep(2)
                clear_screen()
            else:
                if player_one.get_element() == "Fire":
                    for spell in Fire_spell_book:
                        print("=============================")
                        print(spell.get_name())
                        print('-----------------------------')
                        print(f"Damage: {spell.get_damage()}")
                        print('-----------------------------')
                        print(spell.get_description())
                        print('-----------------------------')
                    spell_choice = input("Would you like to lear one of there spells?")
                if player_one.get_element() == "Frost":
                    for spell in Frost_spell_book:
                        print("=============================")
                        print(spell.get_name())
                        print('-----------------------------')
                        print(f"Damage: {spell.get_damage()}")
                        print('-----------------------------')
                        print(spell.get_description())
                        print('-----------------------------')
                    spell_choice = input("Would you like to lear one of there spells?")
                if player_one.get_element() == "Lightning":
                    for spell in Lightning_spell_book:
                        print("=============================")
                        print(spell.get_name())
                        print('-----------------------------')
                        print(f"Damage: {spell.get_damage()}")
                        print('-----------------------------')
                        print(spell.get_description())
                        print('-----------------------------')
                    spell_choice = input("Would you like to lear one of there spells?")
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