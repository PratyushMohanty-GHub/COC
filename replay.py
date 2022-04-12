from cmath import sqrt
import os
import colorama
from numpy import matrix
import math as mat
from game import *
from objects.Troops import *
from src.input import input_to, Get
import json
import time
# Entry Point of the Game
getch = Get()
myGame = Game()
myGame.printMatrix()

def defense():
    for c in myGame.all_cannon:
        if c.health > 0:
            for i in range(25):
                for j in range(50):
                    if ((i-c.R)**2 + (j-c.C)**2) <= c.range**2:
                        if myGame.matrix[i][j] == 'K':
                            myGame.BarbarianKing.health -= c.damage
                            return 1
                        if myGame.matrix[i][j] == 'B':
                            for b in myGame.barbarians:
                                if b.C == j and b.R == i:
                                    b.health = b.health - c.damage
                                    return 1


def barbarian_move():
    for b in myGame.barbarians:
        if b.health > 0:
            shortest_dist = 100
            shortest_C = 0
            shortest_R = 0
            for i in range(25):
                for j in range(50):
                    if myGame.matrix[i][j] == 'C' or myGame.matrix[i][j] == 'T' or myGame.matrix[i][j] == 'H':
                        if (i-b.R)**2 + (j-b.C)**2 <= shortest_dist**2:
                            if (i-b.R)**2 + (j-b.C)**2 <= (shortest_dist*shortest_dist):
                                shortest_dist = mat.sqrt(
                                    (i-b.R)**2 + (j-b.C)**2)
                                shortest_R = i
                                shortest_C = j

            move = 0
            if b.R != shortest_R:
                if b.R > shortest_R and b.R > 0 and (myGame.matrix[b.R-1][b.C] == '*' or myGame.matrix[b.R-1][b.C] == 'B'):
                    myGame.matrix[b.R][b.C] = '*'
                    b.R = b.R - 1
                    myGame.matrix[b.R][b.C] = 'B'
                    move = 1
                else:
                    if b.R < 25 and (myGame.matrix[b.R+1][b.C] == '*' or myGame.matrix[b.R+1][b.C] == 'B'):
                        myGame.matrix[b.R][b.C] = '*'
                        b.R = b.R + 1
                        myGame.matrix[b.R][b.C] = 'B'
                        move = 1

            else:
                if b.C != shortest_C and b.C > shortest_C and b.C > 0 and (myGame.matrix[b.R][b.C-1] == '*' or myGame.matrix[b.R][b.C-1] == 'B'):
                    myGame.matrix[b.R][b.C] = '*'
                    b.C = b.C - 1
                    myGame.matrix[b.R][b.C] = 'B'
                    move = 1
                else:
                    if b.C < 50 and (myGame.matrix[b.R][b.C+1] == '*' or myGame.matrix[b.R][b.C+1] == 'B'):
                        myGame.matrix[b.R][b.C] = '*'
                        b.C = b.C + 1
                        myGame.matrix[b.R][b.C] = 'B'
                        move = 1
            attack_r = b.R
            attack_c = b.C

            if b.R != shortest_R and move == 0:
                if b.R > shortest_R:
                    attack_r = b.R - 1
                else:
                    attack_r = b.R + 1
            else:
                if b.C > shortest_C:
                    attack_c = b.C - 1
                else:
                    attack_c = b.C + 1

            if myGame.matrix[attack_r][attack_c] == 'W':
                for w in myGame.all_wall:
                    if w.R == attack_r and w.C == attack_c:
                        w.health = w.health - b.damage
            if myGame.matrix[attack_r][attack_c] == 'T':
                myGame.th.health = myGame.th.health - b.damage
            if myGame.matrix[attack_r][attack_c] == 'H':
                for h in myGame.all_hut:
                    if h.R == attack_r and h.C == attack_c:
                        h.health = h.health - b.damage
            if myGame.matrix[attack_r][attack_c] == 'C':
                for c in myGame.all_cannon:
                    if c.R == attack_r and c.C == attack_c:
                        c.health = c.health - b.damage


max_barb = 20
def create_barbarian(pos):
    if len(myGame.barbarians) < max_barb:
        if pos == '1':
            myGame.barbarians.append(barbarian(0, 0, 100, 100, 1, 1))
            myGame.matrix[0][0] = 'B'
        elif pos == '2':
            myGame.barbarians.append(barbarian(0, 49, 100, 100, 1, 1))
            myGame.matrix[0][49] = 'B'
        else:
            myGame.barbarians.append(barbarian(24, 0, 100, 100, 1, 1))
            myGame.matrix[24][0] = 'B'


def end_cond():
    no_barb = 1
    no_bldg = 1
    if len(myGame.barbarians) < max_barb:
        no_barb = 0
    for c in myGame.all_cannon:
        if c.health > 0:
            no_bldg = 0
    for h in myGame.all_hut:
        if h.health > 0:
            no_bldg = 0
    if myGame.th.health > 0:
        no_bldg = 0
    if (no_bldg == 1):
        myGame.no_of_stars = 3
        myGame.printMatrix()
        
        print("Troops have won")
        file_name = input("Enter the name of file: ")
        with open('replays/'+file_name+'.json', 'w') as output_file:
            json.dump(inputs, output_file)
        exit()
    elif (no_barb == 1 and myGame.BarbarianKing.health <= 0):
        print("Troops have lost")
        file_name = input("Enter the name of file: ")
        with open('replays/'+file_name+'.json', 'w') as output_file:
            json.dump(inputs, output_file)
        exit()
    else:
        return 1

def check_damage():
    myGame.no_of_building_left = 0
    for i in range(25):
        for j in range(50):
            if (myGame.matrix[i][j] == 'H'):
                myGame.no_of_building_left = myGame.no_of_building_left + 1
            if (myGame.matrix[i][j] == 'C'):
                myGame.no_of_building_left = myGame.no_of_building_left + 1
    if (myGame.th.health > 0):
        myGame.no_of_building_left = myGame.no_of_building_left + 1

    if (myGame.no_of_building_left == 0):
        myGame.no_of_stars = 3
    elif (myGame.no_of_building_left < 4 and myGame.th.health <= 10):
        myGame.no_of_stars = 2
    elif (myGame.no_of_building_left < 4 or myGame.th.health <= 10):
        myGame.no_of_stars = 1
    else:
        myGame.no_of_stars = 0
    
inputs  = input("Enter game name: ")
with open('replays/'+inputs + '.json') as json_file:
    inputs_arr = json.load(json_file)

for inputCmd in inputs_arr:
    # Set actions for 'A', 'S', 'W', 'D'
    defense()
    end_cond()
    barbarian_move()
    if inputCmd == 'a' or inputCmd == 'A':
        # If left Position is safe
        myGame.BarbarianKing.facing = 'a'
        if (myGame.BarbarianKing.C - 1 >= 0 and myGame.matrix[myGame.BarbarianKing.R][myGame.BarbarianKing.C - 1] == '*'):
            myGame.matrix[myGame.BarbarianKing.R][myGame.BarbarianKing.C] = '*'
            myGame.BarbarianKing.C = myGame.BarbarianKing.C - 1
            myGame.matrix[myGame.BarbarianKing.R][myGame.BarbarianKing.C] = 'K'
    elif inputCmd == 's' or inputCmd == 'S':
        # If down position is safe
        myGame.BarbarianKing.facing = 's'
        if (myGame.BarbarianKing.R + 1 < 25 and myGame.matrix[myGame.BarbarianKing.R + 1][myGame.BarbarianKing.C] == '*'):
            myGame.matrix[myGame.BarbarianKing.R][myGame.BarbarianKing.C] = '*'
            myGame.BarbarianKing.R = myGame.BarbarianKing.R + 1
            myGame.matrix[myGame.BarbarianKing.R][myGame.BarbarianKing.C] = 'K'
    elif inputCmd == 'w' or inputCmd == 'W':
        # If up position is safe
        myGame.BarbarianKing.facing = 'w'
        if (myGame.BarbarianKing.R - 1 >= 0 and myGame.matrix[myGame.BarbarianKing.R - 1][myGame.BarbarianKing.C] == '*'):
            myGame.matrix[myGame.BarbarianKing.R][myGame.BarbarianKing.C] = '*'
            myGame.BarbarianKing.R = myGame.BarbarianKing.R - 1
            myGame.matrix[myGame.BarbarianKing.R][myGame.BarbarianKing.C] = 'K'
    elif inputCmd == 'd' or inputCmd == 'D':
        # If right position is safe
        myGame.BarbarianKing.facing = 'd'
        if (myGame.BarbarianKing.C + 1 < 50 and myGame.matrix[myGame.BarbarianKing.R][myGame.BarbarianKing.C + 1] == '*'):
            myGame.matrix[myGame.BarbarianKing.R][myGame.BarbarianKing.C] = '*'
            myGame.BarbarianKing.C = myGame.BarbarianKing.C + 1
            myGame.matrix[myGame.BarbarianKing.R][myGame.BarbarianKing.C] = 'K'
    elif inputCmd == ' ':
        if myGame.BarbarianKing.facing == 'a':
            if myGame.BarbarianKing.health > 0:
                new_col = myGame.BarbarianKing.C - 1
                if myGame.matrix[myGame.BarbarianKing.R][new_col] == 'W' or myGame.matrix[myGame.BarbarianKing.R][new_col] == 'H' or myGame.matrix[myGame.BarbarianKing.R][new_col] == 'T' or myGame.matrix[myGame.BarbarianKing.R][new_col] == 'C':
                    if myGame.matrix[myGame.BarbarianKing.R][new_col] == 'W':
                        for w in myGame.all_wall:
                            if w.R == myGame.BarbarianKing.R and w.C == new_col:
                                w.health = w.health - myGame.BarbarianKing.damage
                                if w.health <= 0:
                                    myGame.all_wall.remove(w)
                                    myGame.matrix[w.R][w.C] = '*'
                                else:
                                    myGame.matrix[w.R][w.C] = 'W'
                    elif myGame.matrix[myGame.BarbarianKing.R][new_col] == 'H':
                        for h in myGame.all_hut:
                            if h.R == myGame.BarbarianKing.R and h.C == new_col:
                                h.health = h.health - myGame.BarbarianKing.damage
                                if h.health <= 0:
                                    myGame.all_hut.remove(h)
                                    myGame.matrix[h.R][h.C] = '*'
                                else:
                                    myGame.matrix[h.R][h.C] = 'H'
                    elif myGame.matrix[myGame.BarbarianKing.R][new_col] == 'C':
                        for c in myGame.all_cannon:
                            if c.R == myGame.BarbarianKing.R and c.C == new_col:
                                c.health = c.health - myGame.BarbarianKing.damage
                                if c.health <= 0:
                                    myGame.all_cannon.remove(c)
                                    myGame.matrix[c.R][c.C] = '*'
                                else:
                                    myGame.matrix[c.R][c.C] = 'C'
                    elif myGame.matrix[myGame.BarbarianKing.R][new_col] == 'T':
                        myGame.th.health = myGame.th.health - myGame.BarbarianKing.damage
        elif myGame.BarbarianKing.facing == 's':
            if myGame.BarbarianKing.health > 0:
                new_row = myGame.BarbarianKing.R + 1
                if myGame.matrix[new_row][myGame.BarbarianKing.C] == 'W' or myGame.matrix[new_row][myGame.BarbarianKing.C] == 'H' or myGame.matrix[new_row][myGame.BarbarianKing.C] == 'T' or myGame.matrix[new_row][myGame.BarbarianKing.C] == 'C':
                    if myGame.matrix[new_row][myGame.BarbarianKing.C] == 'W':
                        for w in myGame.all_wall:
                            if w.R == new_row and w.C == myGame.BarbarianKing.C:
                                w.health = w.health - myGame.BarbarianKing.damage
                                if w.health <= 0:
                                    myGame.all_wall.remove(w)
                                    myGame.matrix[w.R][w.C] = '*'
                                else:
                                    myGame.matrix[w.R][w.C] = 'W'
                    elif myGame.matrix[new_row][myGame.BarbarianKing.C] == 'H':
                        for h in myGame.all_hut:
                            if h.R == new_row and h.C == myGame.BarbarianKing.C:
                                h.health = h.health - myGame.BarbarianKing.damage
                                if h.health <= 0:
                                    myGame.all_hut.remove(h)
                                    myGame.matrix[h.R][h.C] = '*'
                                else:
                                    myGame.matrix[h.R][h.C] = 'H'
                    elif myGame.matrix[new_row][myGame.BarbarianKing.C] == 'C':
                        for c in myGame.all_cannon:
                            if c.R == new_row and c.C == myGame.BarbarianKing.C:
                                c.health = c.health - myGame.BarbarianKing.damage
                                if c.health <= 0:
                                    myGame.all_cannon.remove(c)
                                    myGame.matrix[c.R][c.C] = '*'
                                else:
                                    myGame.matrix[c.R][c.C] = 'C'
                    elif myGame.matrix[new_row][myGame.BarbarianKing.C] == 'T':
                        myGame.th.health = myGame.th.health - myGame.BarbarianKing.damage
        elif myGame.BarbarianKing.facing == 'w':
            if myGame.BarbarianKing.health > 0:
                new_row = myGame.BarbarianKing.R - 1
                if myGame.matrix[new_row][myGame.BarbarianKing.C] == 'W' or myGame.matrix[new_row][myGame.BarbarianKing.C] == 'H' or myGame.matrix[new_row][myGame.BarbarianKing.C] == 'T' or myGame.matrix[new_row][myGame.BarbarianKing.C] == 'C':
                    if myGame.matrix[new_row][myGame.BarbarianKing.C] == 'W':
                        for w in myGame.all_wall:
                            if w.R == new_row and w.C == myGame.BarbarianKing.C:
                                w.health = w.health - myGame.BarbarianKing.damage
                                if w.health <= 0:
                                    myGame.all_wall.remove(w)
                                    myGame.matrix[w.R][w.C] = '*'
                                else:
                                    myGame.matrix[w.R][w.C] = 'W'
                    elif myGame.matrix[new_row][myGame.BarbarianKing.C] == 'H':
                        for h in myGame.all_hut:
                            if h.R == new_row and h.C == myGame.BarbarianKing.C:
                                h.health = h.health - myGame.BarbarianKing.damage
                                if h.health <= 0:
                                    myGame.all_hut.remove(h)
                                    myGame.matrix[h.R][h.C] = '*'
                                else:
                                    myGame.matrix[h.R][h.C] = 'H'
                    elif myGame.matrix[new_row][myGame.BarbarianKing.C] == 'C':
                        for c in myGame.all_cannon:
                            if c.R == new_row and c.C == myGame.BarbarianKing.C:
                                c.health = c.health - myGame.BarbarianKing.damage
                                if c.health <= 0:
                                    myGame.all_cannon.remove(c)
                                    myGame.matrix[c.R][c.C] = '*'
                                else:
                                    myGame.matrix[c.R][c.C] = 'C'
                    elif myGame.matrix[new_row][myGame.BarbarianKing.C] == 'T':
                        myGame.th.health = myGame.th.health - myGame.BarbarianKing.damage
        elif myGame.BarbarianKing.facing == 'd':
            if myGame.BarbarianKing.health > 0:
                new_col = myGame.BarbarianKing.C + 1
                if myGame.matrix[myGame.BarbarianKing.R][new_col] == 'W' or myGame.matrix[myGame.BarbarianKing.R][new_col] == 'H' or myGame.matrix[myGame.BarbarianKing.R][new_col] == 'T' or myGame.matrix[myGame.BarbarianKing.R][new_col] == 'C':
                    if myGame.matrix[myGame.BarbarianKing.R][new_col] == 'W':
                        for w in myGame.all_wall:
                            if w.R == myGame.BarbarianKing.R and w.C == new_col:
                                w.health = w.health - myGame.BarbarianKing.damage
                                if w.health <= 0:
                                    myGame.all_wall.remove(w)
                                    myGame.matrix[w.R][w.C] = '*'
                                else:
                                    myGame.matrix[w.R][w.C] = 'W'
                    elif myGame.matrix[myGame.BarbarianKing.R][new_col] == 'H':
                        for h in myGame.all_hut:
                            if h.R == myGame.BarbarianKing.R and h.C == new_col:
                                h.health = h.health - myGame.BarbarianKing.damage
                                if h.health <= 0:
                                    myGame.all_hut.remove(h)
                                    myGame.matrix[h.R][h.C] = '*'
                                else:
                                    myGame.matrix[h.R][h.C] = 'H'
                    elif myGame.matrix[myGame.BarbarianKing.R][new_col] == 'C':
                        for c in myGame.all_cannon:
                            if c.R == myGame.BarbarianKing.R and c.C == new_col:
                                c.health = c.health - myGame.BarbarianKing.damage
                                if c.health <= 0:
                                    myGame.all_cannon.remove(c)
                                    myGame.matrix[c.R][c.C] = '*'
                                else:
                                    myGame.matrix[c.R][c.C] = 'C'
                    elif myGame.matrix[myGame.BarbarianKing.R][new_col] == 'T':
                        myGame.th.health = myGame.th.health - myGame.BarbarianKing.damage
    elif inputCmd == '1' or inputCmd == '2' or inputCmd == '3':
        create_barbarian(inputCmd)
    elif inputCmd == 'H' or inputCmd == 'h':
        for b in myGame.barbarians:
            b.h_spell()
        myGame.BarbarianKing.h_spell()
    elif inputCmd == 'R' or inputCmd == 'r':
        for b in myGame.barbarians:
            b.r_spell()
        myGame.BarbarianKing.r_spell()
    elif inputCmd == 'L' or inputCmd == 'l':
        # On which bulding the lightning strike is cast
        print('Which building would you like to strike?')
        print('1. Hut')
        print('2. Cannon')
        print('3. Town Hall')
        print('4. Exit')
        print('Enter your choice: ')
        inputCmd = input()
        if inputCmd == '1':
            for h in myGame.all_hut:
                h.l_spell()
        elif inputCmd == '2':
            for c in myGame.all_cannon:
                c.l_spell()
        elif inputCmd == '3':
            myGame.th.l_spell()
    elif inputCmd == 'e' or inputCmd == 'E':
        for i in range(25):
            for j in range(50):
                if ((i - myGame.BarbarianKing.R)**2 + (j-myGame.BarbarianKing.C)**2) < (36):
                    for w in myGame.all_hut:
                        if w.C == j and w.R == i:
                            w.health = w.health - myGame.BarbarianKing.damage
                    for c in myGame.all_cannon:
                        if c.C == j and c.R == i:
                            c.health = c.health - myGame.BarbarianKing.damage
                    if myGame.th.R == i and myGame.th.C == j:
                        myGame.th.health = myGame.th.health - myGame.BarbarianKing.damage
    elif inputCmd == 'q' or inputCmd == 'Q':
        print('                                      ' + 'Thank you for playing!')
        break

    myGame.printMatrix()
