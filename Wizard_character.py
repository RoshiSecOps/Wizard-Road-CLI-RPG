from Human_character_template import Human

class Wizard(Human):
    
    def __init__(self, name, health, mana, element):
        super().__init__(name, health, mana)
        self.__element = element
        self.__damage = self.intelligence * 0.3
        self.crit = 0
        self.level = 1
        self.buff_spell = 0
        self.defensive_spell = 0

    def get_level(self):
        return self.level
    
    def get_element(self):
        return self.__element

    def level_up(self):
        self.level += 1
        return self.level

    def get_damage(self):
        return self.__damage

    def invoke_element(self):
        return f"{self.__name} the {self.__element} Wizard"
    
    def enable_crit(self):
        self.crit = 1

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
        if target.is_alive() and self.crit == 1:
            target.take_damage(self.__damage * 3)
            print(f"Cast CRITICAL {self.get_offensive_spell_name()} on {target.get_name()} for {self.__damage * 3} Damage")
            self.crit = 0

        if target.is_alive():
            target.take_damage(self.__damage)
            print(f"Cast {self.get_offensive_spell_name()} on {target.get_name()} for {self.__damage} Damage")
  
    def cast_buff_spell(self, spell):
        spell.cast_spell(self)
    
    def cast_defensive_spell(self, spell):
        spell.cast_spell(self)


