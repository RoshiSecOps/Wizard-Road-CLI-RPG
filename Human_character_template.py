class Human:
    def __init__(self, name, health, mana):
        self.__name = name
        self.__health = health
        self.__mana = mana
        self.__stamina = self.__health * 0.5
        self.__intelligence = self.__mana * 1.5

    def get_name(self):
        return self.__name
    
    def get_health(self):
        return self.__health

    def get_mana(self):
        return self.__mana
    
    def get_stamina(self):
        return self.__stamina
    
    def get_intelligence(self):
        return self.__intelligence
    
    def is_alive(self):
        return self.__health > 0
    
