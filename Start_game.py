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

Frost_spell_book = []
Fire_spell_book = []
Lightning_spell_book = []

player_one = create_character()

def get_spellbook_by_element(player_one):
    if player_one.get_element() == "Frost":
        Frost_spell_book = [frost_crit, frost_heal]
        buff = frost_crit
        heal = frost_heal
        return Frost_spell_book, buff, heal
    
    elif player_one.get_element() == "Fire":
        Fire_spell_book = [fire_crit, fire_heal]
        buff = fire_crit
        heal = fire_heal
        return Fire_spell_book, buff, heal

    elif player_one.get_element() == "Lightning":
        Lightning_spell_book = [lightning_crit, lightning_heal]
        buff = lightning_crit
        heal = lightning_heal
        return Lightning_spell_book, buff, heal

actual_spellbook, buff, heal = get_spellbook_by_element(player_one)

first_enemy = Orc("Rengar", 150, 5, 5)
second_enemy = Orc("Rengar's cousin", 150, 10, 5)
third_enemy = Orc("The BOSS", 300, 20, 5)

def learn_advanced_spell(player, choice, available_spells, buff, heal):
    if choice == 1 and len(available_spells) == 2:
        player.learn_buff()
        time.sleep(1)
        clear_screen()
    elif choice == 2 and len(available_spells) == 2:
        player.learn_heal()
        time.sleep(1)
        clear_screen()
    elif choice == 1 and len(available_spells) == 1 and available_spells[0] == buff:
        player.learn_buff()
        time.sleep(1)
        clear_screen()
    elif choice == 1 and len(available_spells) == 1 and available_spells[0] == heal:
        player.learn_heal()
        time.sleep(1)
        clear_screen()
    else:
        time.sleep(1)
        clear_screen()
        return
        

def trial_gameplay(buff, heal):
    while player_one.is_alive() == True:
        open_main_menu()
        player_choice = int(input("You choose?( 1 - 5 ): "))
        if player_choice == 1:
            if first_enemy.is_alive() == True:
                print(f"{player_one.get_name()} is fighting {first_enemy.get_name()}, fight starts in 2 seconds!")
                time.sleep(2)
                full_battle(first_enemy, player_one, buff, heal)
            elif second_enemy.is_alive() == True:
                print(f"{player_one.get_name()} is fighting {second_enemy.get_name()}, fight starts in 2 seconds!")
                time.sleep(2)
                full_battle(second_enemy, player_one, buff, heal)
            elif third_enemy.is_alive() == True:
                print(f"{player_one.get_name()} is fighting {third_enemy.get_name()}, fight starts in 2 seconds!")
                time.sleep(2)
                full_battle(third_enemy, player_one, buff, heal)
            else:
                print("You've completed the Game, congratulations!")
            clear_screen()
        elif player_choice == 2:
            if player_one.get_level() < 2:
                print("Level too low, come back once you are stronger!")
                print("[ Going back to main menu in 2 seconds ]")
                time.sleep(2)
                clear_screen()
            else:
                counter = 1
                if player_one.get_element() == "Fire":
                    if len(actual_spellbook) == 0:
                        print("All spells learned.")
                        time.sleep(1)
                        clear_screen()
                    else:
                        for spell in actual_spellbook:
                            print("=============================")
                            print(f"{counter}: {spell.get_name()}")
                            print('-----------------------------')
                            print(f"Damage: {spell.get_damage()}")
                            print('-----------------------------')
                            print(spell.get_description())
                            print('-----------------------------')
                            counter += 1
                        spell_choice = int(input("Would you like to lear one of there spells? (pick 1 or 2)"))
                        if spell_choice == 1:
                            learn_advanced_spell(player_one, spell_choice, actual_spellbook, buff, heal)
                            del actual_spellbook[0]
                        elif spell_choice == 2:
                            learn_advanced_spell(player_one, spell_choice, actual_spellbook, buff, heal)
                            del actual_spellbook[1]
                        else:
                            print("Not a valid choice")
                if player_one.get_element() == "Frost":
                    if len(actual_spellbook) == 0:
                        print("All spells learned.")
                        time.sleep(1)
                        clear_screen()
                    else:
                        for spell in actual_spellbook:
                            print("=============================")
                            print(f"{counter}: {spell.get_name()}")
                            print('-----------------------------')
                            print(f"Damage: {spell.get_damage()}")
                            print('-----------------------------')
                            print(spell.get_description())
                            print('-----------------------------')
                            counter += 1
                        spell_choice = int(input("Would you like to lear one of there spells? (pick 1 or 2)"))
                        if spell_choice == 1:
                            learn_advanced_spell(player_one, spell_choice, actual_spellbook, buff, heal)
                            del actual_spellbook[0]
                        elif spell_choice == 2:
                            learn_advanced_spell(player_one, spell_choice, actual_spellbook, buff, heal)
                            del actual_spellbook[1]
                        else:
                            print("Not a valid choice")
                if player_one.get_element() == "Lightning":
                    if len(actual_spellbook) == 0:
                        print("All spells learned.")
                        time.sleep(1)
                        clear_screen()
                    else:
                        for spell in actual_spellbook:
                            print("=============================")
                            print(f"{counter}: {spell.get_name()}")
                            print('-----------------------------')
                            print(f"Damage: {spell.get_damage()}")
                            print('-----------------------------')
                            print(spell.get_description())
                            print('-----------------------------')
                            counter += 1
                        spell_choice = int(input("Would you like to lear one of there spells? (pick 1 or 2)"))
                        if spell_choice == 1:
                            learn_advanced_spell(player_one, spell_choice, actual_spellbook, buff, heal)
                            del actual_spellbook[0]
                        elif spell_choice == 2:
                            learn_advanced_spell(player_one, spell_choice, actual_spellbook, buff, heal)
                            del actual_spellbook[1]
                        else:
                            print("Not a valid choice")
        elif player_choice == 3:
            player_one.get_all_stats()
            print(player_one.can_buff())
            print(player_one.can_heal())
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
play_a_game = trial_gameplay(buff, heal)