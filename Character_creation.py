from Wizard_character import *
from Human_character_template import *

wizard_elements = ["Fire", "Frost", "Lightning"]
wizard_health = 100
wizard_mana = 50

print("Welcome to Wizard Road, may your adventure be prosperous!")

player_name = input("What is your name, adventurer? \n")
player_name = player_name.lower().capitalize()

print(f"\nGreetings, {player_name}! It is time to pick your elemental prowess!\nAvailable options are:")

for i in range(0, 3):
    element_number = i+1
    print(f"\t{element_number}: {wizard_elements[i]}")

print(f"\n{player_name}, please choose an element from 1 to 3:")
player_element = input("Enter choice: ")
player_element = wizard_elements[int(player_element) - 1]

player_one = Wizard(player_name, wizard_health, wizard_mana, player_element)

print(f"\n{player_name}, you've chosen to become a {player_element} Wizard!\nGood choice! Your offensive spell is {player_one.get_offensive_spell_name()}\n")



player_one.get_all_stats()

