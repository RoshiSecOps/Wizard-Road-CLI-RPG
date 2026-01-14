class basic_spell():
    def __init__(self, name, damage, description):
        self.name = name
        self.damage = damage
        self.description = description

    def get_damage(self):
        return self.damage
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description

class fire_spell_combustion(basic_spell):
    def __init__(self, name, description):
        super().__init__(name, description)
        
    def cast_spell(self, caster):
        if caster.is_alive():
            caster.enable_crit()
            print(f"{caster.get_name()} activates Combustion, triple damage next turn!")

class fire_spell_goldenflame(basic_spell):
    def __init__(self, name, damage, description):
        super().__init__(name, damage, description)
    
    def cast_spell(self, caster):
        caster.rest_turn(self.damage)

class frost_spell_chill(basic_spell):
    def __init__(self, name, description):
        super().__init__(name, description)
        
    def cast_spell(self, caster):
        if caster.is_alive():
            caster.enable_crit()
            print(f"{caster.get_name()} activates Chill, triple damage next turn!")

class frost_spell_iceblock(basic_spell):
    def __init__(self, name, damage, description):
        super().__init__(name, damage, description)
        
    def cast_spell(self, caster):
        caster.rest_turn(self.damage)

class lightning_spell_thundering(basic_spell):
    def __init__(self, name, description):
        super().__init__(name, description)
        
    def cast_spell(self, caster):
        if caster.is_alive():
            caster.enable_crit()
            print(f"{caster.get_name()} activates Thundering, triple damage next turn!")

class lightning_spell_flashheal(basic_spell):
    def __init__(self, name, damage, description):
        super().__init__(name, damage, description)

    def cast_spell(self, caster):
        caster.rest_turn(self.damage)

frost_crit = frost_spell_chill("Chill", "Your next Frost bolt will have it's damage tripled","")
frost_heal = frost_spell_iceblock("Ice Block", 60, "Surround yourself in a block of ICE, healing for 60 points")

fire_crit = fire_spell_combustion("Combustion", "Combust, dealing critical damage on your next attack!")
fire_heal = fire_spell_goldenflame("Golden Flames", 60, "Engulf in golden flames, healing for 60 points")

lightning_crit = lightning_spell_thundering("Thundering", "Call forth the thunder! Damage of next attack is tripled!")
lightning_heal = lightning_spell_flashheal("Flash Heal", 60, "Call forth a flash of lightning that heals you for 60 points")
