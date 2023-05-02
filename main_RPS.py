import random
import os
import time

import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.25)

def movement(p1,p2):
    if (p1 == 'R'):
        if(p2 == 'R'):
            return 'Draw'
        if(p2 == 'P'):
            print('P2 wins')
            return 'P2 wins'
        if(p2 == 'S'):
            print('P1 wins')
            return 'P1 wins'
    if (p1 == 'P'):
        if(p2 == 'R'):
            print('P1 wins')
            return 'P1 wins'
        if(p2 == 'P'):
            return 'Draw'
        if(p2 == 'S'):
            print('P2 wins')
            return 'P2 wins'
    if (p1 == 'S'):
        if(p2 == 'R'):
            print('P2 wins')
            return 'P2 wins'
        if(p2 == 'P'):
            print('P1 wins') #posso excuir os prints, irrelevantes
            return 'P1 wins'
        if(p2 == 'S'):
            return 'Draw'
    
p1_score = 0
p2_score = 0

while(True):
    os.system('cls')
    print(f'Scores:\n Player 1 = {p1_score}\t\t\t\t Player 2 = {p2_score}\n')
    mov = ['R','P','S']
    p1 = input("type 'R', 'P', or 'S' to make a move.")
    if(p1 != 'R' or p1 !='S' or p1 != 'P'):
        print("opção invalida, digite apenas R, P ou S")
        time.sleep(2)
        continue
    p2 = mov[random.randint(0,2)]

    print(" Your move = ",p1)
    print("Enemy move = ", p2)


    result = movement(p1,p2)
    if (result == 'P1 wins'):
        p1_score = p1_score + 1
    if(result == 'P2 wins'):
        p2_score = p2_score + 1
    elif(result == 'Draw'):
        print("Empate...")

    time.sleep(2)
    if(p1_score == 3):
        os.system('cls')
        delay_print("You Win")
        break
    elif(p2_score == 3):
        os.system('cls')
        delay_print("You Lose")
        break
