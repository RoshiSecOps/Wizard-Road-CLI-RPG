class Human:
    def __init__(self, name, health, mana = 0):
        self.__name = name
        self.__health = health
        self.__mana = mana
        self.stamina = self.__health * 0.5
        self.intelligence = self.__mana * 1.5

    def get_all_stats(self):
        print(f"Name: {self.get_name()}")
        print(f"Health: {self.get_health()}")
        print(f"Mana: {self.get_mana()}")
        print(f"Stamina: {self.get_stamina()}")
        print(f"Intelligence: {self.get_intelligence()}")
    
    def get_name(self):
        return self.__name
    
    def get_health(self):
        return self.__health

    def get_mana(self):
        return self.__mana
    
    def get_stamina(self):
        return self.stamina
    
    def get_intelligence(self):
        return self.intelligence
    
    def is_alive(self):
        return self.__health > 0
    
    def take_damage(self, amount):
        self.__health -= amount
        if self.is_alive() == False:
            return False
    def heal_full(self):
        self.__health = 100
        print(f"{self.get_name()} is healed to full {self.get_health()} HP")

    def rest_turn(self, amount):
        self.__health += amount
        print(f"{self.get_name()} gains {amount} health, current health: {self.get_health()}")
            
    
