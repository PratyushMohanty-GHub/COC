# Define a class Troops
class Troops:
    def __init__(self, R, C, health, maxHealth, damage):
        self.R = R
        self.C = C
        self.facing = 'd'
        self.damage = damage
        self.health = maxHealth
        self.maxHealth = maxHealth

# Define a sub-class BarbarianKing
class BarbarianKing(Troops):
    def __init__(self, R, C, health, maxHealth, damage):
        super().__init__(R, C, health, maxHealth, damage)
        self.name = 'Barbarian King'
    
    def h_spell(self):
        self.health = self.health*1.5
        if self.health > self.maxHealth:
            self.health = self.maxHealth

    def r_spell(self):
        self.damage = self.damage*2

class barbarian(Troops):
    def __init__(self, R, C, health, maxHealth, damage, speed):
        super().__init__(R, C, health, maxHealth, damage)
        self.name = 'Barbarian'
        self.speed = speed

    def h_spell(self):
        self.health = self.health*1.5
        if self.health > self.maxHealth:
            self.health = self.maxHealth
    
    def r_spell(self):
        self.damage = self.damage*2