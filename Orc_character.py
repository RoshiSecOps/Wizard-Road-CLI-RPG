from Human_character_template import Human

class Orc(Human):
    def __init__(self, name, health, damage, rage = 0):
        super().__init__(name, health)
        self.__rage = rage
        self.__damage = damage
        self.__race = "Orc"

    def get_damage(self):
        return self.__damage

    def get_race(self):
        return self.__race
    
    def melee_attack(self, target):
        if target.is_alive() and self.is_enraged():
            enraged_damage = self.__damage * 2
            target.take_damage(enraged_damage)
            self.__rage = 0
            print(f"{self.get_name()} attacks {target.get_name()} for {enraged_damage} Damage.")
        elif target.is_alive():
            target.take_damage(self.__damage)
            self.__rage += 1
            print(f"{self.get_name()} Attacks {target.get_name()} for {self.__damage} Damage.")

    def is_enraged(self):
        if self.__rage == 5:
            return True
        return False
