import time

# Define a class Building
class Building:
    def __init__(self, R, C, health, maxHealth):
        self.R = R
        self.C = C
        self.health = health
        self.maxHealth = maxHealth

# Define a sub-class TownHall
class TownHall(Building):
    def __init__(self, R, C, health, maxHealth):
        super().__init__(R, C, health, maxHealth)
        self.name = 'Town Hall'
    
    def l_spell(self):
        self.health = self.health*0.75

# Define a sub-class Barracks
class Hut(Building):
    def __init__(self, hutID, R, C, health, maxHealth):
        super().__init__(R, C, health, maxHealth)
        self.name = 'Hut'
        self.hutID = hutID

    def l_spell(self):
        self.health = self.health*0.75

# Define a sub-class Wall
class Wall(Building):
    def __init__(self, wallID, R, C, health, maxHealth):
        super().__init__(R, C, health, maxHealth)
        self.name = 'Wall'
        self.wallID = wallID
    
    def l_spell(self):
        self.health = self.health*0.75
        
# Define a sub-class Cannon
class Cannon(Building):
    def __init__(self, cannonID, R, C, health, maxHealth, damage, range):
        super().__init__(R, C, health, maxHealth)
        self.name = 'Cannon'
        self.cannonID = cannonID
        self.damage = damage
        self.range = range
    
    def l_spell(self):
        self.health = self.health*0.75
