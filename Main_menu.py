import os

def open_main_menu():
    spacer_length = 0
    spacer = "="
    counter = 1
    menu_actions = ["Fight", "Enter Shop", "Current Stats", "Exit"]
    for item in menu_actions:
        if len(item) > spacer_length:
            spacer_length = len(item)
    spacer *= (spacer_length + 3)
    print(spacer)
    for item in menu_actions:
        print(str(counter) + ": " + item)
        print(spacer)
        counter += 1

def clear_screen():
    os.system("clear")
