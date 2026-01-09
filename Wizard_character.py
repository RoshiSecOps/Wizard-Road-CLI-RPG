from Human_character_template import Human

class Wizard(Human):
    
    def __init__(self, name, health, mana, element):
        super().__init__(name, health, mana)
        self.__element = element
        self.__damage = self.intelligence * 0.3

    
    def get_damage(self):
        return self.__damage

    def invoke_element(self):
        return f"{self.__name} the {self.__element} Wizard"
    
    def get_all_stats(self):
        print(f"Name: {self.get_name()}")
        print(f"Health: {self.get_health()}")
        print(f"Mana: {self.get_mana()}")
        print(f"Stamina: {self.get_stamina()}")
        print(f"Intelligence: {self.get_intelligence()}")

    def get_offensive_spell_name(self):
        if self.__element == "Lightning":
            return "Lightning Bolt"
        if self.__element == "Fire":
            return "Fire Ball"
        if self.__element == "Frost":
            return "Frost Bolt"

    def get_offensive_spell_info(self):
        if self.__element == "Lightning":
            self.__damage += 5
            return f"{self.__name}, your attack spell is Lightning Bolt, it deals {self.__damage} damage!"
        elif self.__element == "Fire":
            self.__damage += 10
            return f"{self.__name}, your attack spell is Fire Ball, it deals {self.__damage} damage!"
        elif self.__element == "Frost":
            self.__damage -= 5
            return f"{self.__name}, your attack spell is Frost Bolt, it deals {self.__damage} damage!"
    
    def cast_offensive_spell(self, target):
        if target.is_alive():
            target.take_damage(self.__damage)
            return f"Cast {self.get_offensive_spell_name} on {target.__name} for {self.__damage} Damage"
  



