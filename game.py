import os
import colorama
from numpy import matrix
from objects.Buildings import *
from objects.Troops import *

class Game:
    def __init__(self):
        self.all_hut = []
        self.all_wall = []
        self.all_cannon = []
        self.barbarians = []

        self.no_of_stars = 0
        self.no_of_building_left = 7
        self.total_no_of_building = 7
    
        self.matrix = [['*' for i in range(50)] for j in range(25)]
        self.th = TownHall(11,23,1000,1000)
        for i in range(25):
            for j in range(50):
            # Town Hall
                if i >= 11 and i <= 13 and j >= 23 and j <= 26:
                    self.matrix[i][j] = 'T'
            # Walls
                elif (i == 3 and j >= 15 and j <= 34) or (i == 21 and j >= 15 and j <= 34) or (j == 15 and i >= 3 and i <= 21) or (j == 34 and i >= 3 and i <= 21):
                    self.matrix[i][j] = 'W'
                    self.all_wall.append(Wall(len(self.all_wall), i, j, 100, 100))
            # Huts
                elif (i == 7 or i == 17) and (j == 21 or j == 28):
                    self.matrix[i][j] = 'H'
                    self.all_hut.append(Hut(len(self.all_hut), i, j, 100, 100))
            # Canons
                elif (i == 12) and (j == 19 or j == 30):
                    self.matrix[i][j] = 'C'
                    self.all_cannon.append(Cannon(len(self.all_cannon), i, j, 100, 100, 5, 5))
                else:
                    self.matrix[i][j] = '*'
        
        self.BarbarianKing = BarbarianKing(12, 9, 1000, 1000, 20)
        self.matrix[self.BarbarianKing.R][self.BarbarianKing.C] = 'K'

    def printMatrix(self):
        # Print Welcome Message in center of screen
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colorama.Fore.CYAN)
        print('                              ' + 'Welcome to the game of Clash Of Clans!!!')

        # Print no. of stars in the match
        print(colorama.Fore.GREEN + '                                          ' + 'No. of Stars: ' + colorama.Fore.LIGHTYELLOW_EX + ' * ' * self.no_of_stars)
        print(colorama.Fore.GREEN)
        for i in range(25):
            for j in range(50):
                if (self.matrix[i][j] == '*'):
                    # Print in white
                    print(colorama.Fore.LIGHTBLUE_EX + self.matrix[i][j], end=' ')
                elif (self.matrix[i][j] == 'K'):
                    if (self.BarbarianKing.health > 0):
                        print(colorama.Fore.CYAN + self.matrix[i][j], end=' ')
                    else :
                        self.matrix[i][j] = '*'
                        print(colorama.Fore.LIGHTBLACK_EX + self.matrix[i][j], end=' ')
                elif (self.matrix[i][j] == 'T'):
                    if self.th.health > (self.th.maxHealth / 2):
                        print(colorama.Fore.LIGHTGREEN_EX + self.matrix[i][j], end=' ')
                    elif self.th.health > (self.th.maxHealth / 4):
                        print(colorama.Fore.YELLOW + self.matrix[i][j], end=' ')
                    elif self.th.health > 0:
                        print(colorama.Fore.RED + self.matrix[i][j], end=' ')
                    else :
                        self.matrix[i][j] = '*'
                        print(colorama.Fore.LIGHTBLACK_EX + self.matrix[i][j], end=' ')
                elif (self.matrix[i][j] == 'W'):
                    for w in self.all_wall:
                        if (w.R == i and w.C == j):
                            if (w.health > (w.maxHealth / 2)):
                                print(colorama.Fore.LIGHTGREEN_EX + self.matrix[i][j], end=' ')
                            elif (w.health > (w.maxHealth / 4)):
                                print(colorama.Fore.YELLOW + self.matrix[i][j], end=' ')
                            elif (w.health > 0):
                                print(colorama.Fore.RED + self.matrix[i][j], end=' ')
                            else :
                                self.matrix[i][j] = '*'
                                print(colorama.Fore.LIGHTBLACK_EX + self.matrix[i][j], end=' ')
                elif (self.matrix[i][j] == 'H'):
                    for h in self.all_hut:
                        if (h.R == i and h.C == j):
                            if (h.health > (h.maxHealth / 2)):
                                print(colorama.Fore.LIGHTGREEN_EX + self.matrix[i][j], end=' ')
                            elif (h.health > (h.maxHealth / 4)):
                                print(colorama.Fore.YELLOW + self.matrix[i][j], end=' ')
                            elif (h.health > 0):
                                print(colorama.Fore.RED + self.matrix[i][j], end=' ')
                            else :
                                self.matrix[i][j] = '*'
                                print(colorama.Fore.LIGHTBLACK_EX + self.matrix[i][j], end=' ')
                elif (self.matrix[i][j] == 'C'):
                    for c in self.all_cannon:
                        if (c.R == i and c.C == j):
                            if (c.health > (c.maxHealth / 2)):
                                print(colorama.Fore.LIGHTGREEN_EX + self.matrix[i][j], end=' ')
                            elif (c.health > (c.maxHealth / 4)):
                                print(colorama.Fore.YELLOW + self.matrix[i][j], end=' ')    
                            elif (c.health > 0):
                                print(colorama.Fore.RED + self.matrix[i][j], end=' ')
                            else :
                                self.matrix[i][j] = '*'
                                print(colorama.Fore.LIGHTBLACK_EX + self.matrix[i][j], end=' ')
                elif (self.matrix[i][j] == 'B'):
                    for b in self.barbarians:
                        if (b.R == i and b.C == j):
                            if (b.health > (b.maxHealth / 2)):
                                print(colorama.Fore.LIGHTGREEN_EX + self.matrix[i][j], end=' ')
                            elif (b.health > (b.maxHealth / 4)):
                                print(colorama.Fore.YELLOW + self.matrix[i][j], end=' ')
                            elif (b.health > 0):
                                print(colorama.Fore.RED + self.matrix[i][j], end=' ')
                            else :
                                self.matrix[i][j] = '*'
                                print(colorama.Fore.LIGHTBLACK_EX + self.matrix[i][j], end=' ')
                            break

            print()
        print()
        
        # Print Health of Town Hall
        print(colorama.Fore.YELLOW + 'Health of Town Hall: ' + colorama.Fore.LIGHTMAGENTA_EX + str(self.th.health) + '/' + str(self.th.maxHealth))
        # Print Health Bar of Town Hall
        if (self.th.health > 0):
            print(colorama.Fore.YELLOW + 'Health Bar of Town Hall: ' + colorama.Fore.LIGHTMAGENTA_EX + '*' * int(self.th.health / self.th.maxHealth * 10))
        else:
            print(colorama.Fore.RED + '        Town Hall is destroyed!!!')

        print()

        # Print Health of Barbarian King
        print(colorama.Fore.YELLOW + 'Health of Barbarian King: ' + colorama.Fore.LIGHTMAGENTA_EX + str(self.BarbarianKing.health) + '/' + str(self.BarbarianKing.maxHealth))
        # Print Health Bar of Barbarian King
        if (self.BarbarianKing.health > 0):
            print(colorama.Fore.YELLOW + 'Health Bar of Barbarian King: ' + colorama.Fore.LIGHTMAGENTA_EX + '*' * int(self.BarbarianKing.health / self.BarbarianKing.maxHealth * 10))
        else:
            print(colorama.Fore.RED + '        King is dead!!!')
        print(colorama.Fore.RESET)
