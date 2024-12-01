# Parent Class: Superhero
class Superhero:
    def __init__(self, name, alias, superpower, strength_level):
        self.name = name
        self.alias = alias
        self.superpower = superpower
        self.strength_level = strength_level
    
    def display_identity(self):
        return f"{self.alias} (real name: {self.name}) is a superhero with {self.superpower}."

    def use_power(self):
        return f"{self.alias} uses {self.superpower}!"
    
# Child Class: TechHero (inherits from Superhero)
class TechHero(Superhero):
    def __init__(self, name, alias, superpower, strength_level, gadgets):
        super().__init__(name, alias, superpower, strength_level)
        self.gadgets = gadgets

    def display_identity(self):
        return f"{self.alias} (real name: {self.name}) is a tech-savvy superhero equipped with {', '.join(self.gadgets)}."

# Child Class: MysticHero (inherits from Superhero)
class MysticHero(Superhero):
    def __init__(self, name, alias, superpower, strength_level, magical_artifacts):
        super().__init__(name, alias, superpower, strength_level)
        self.magical_artifacts = magical_artifacts

    def use_power(self):
        return f"{self.alias} summons the power of {', '.join(self.magical_artifacts)} to enhance {self.superpower}!"
        
# Creating objects
hero1 = Superhero("Clark Kent", "Superman", "super strength", 100)
hero2 = TechHero("Tony Stark", "Iron Man", "intelligence and tech", 90, ["Iron Suit", "Jarvis AI"])
hero3 = MysticHero("Stephen Strange", "Doctor Strange", "magic", 95, ["Eye of Agamotto", "Cloak of Levitation"])

# Testing the classes
print(hero1.display_identity())
print(hero2.display_identity())
print(hero3.use_power())
