from Human_character_template import Human

class Orc(Human):
    def __init__(self, name, health, rage = 0):
        super().__init__(name, health)
        self.__rage = rage
        self.__damage = 5

    def get_damage(self):
        return self.__damage
    
    def melee_attack(self, target):
        if target.is_alive() and self.is_enraged():
            print(f"Enraged attack by {self.get_name()} the Orc")
            target.take_damage(self.__damage + 5)
            self.__rage = 0
        elif target.is_alive():
            target.take_damage(self.__damage)
            self.__rage += 1

    def is_enraged(self):
        if self.__rage == 5:
            return True
        return False
