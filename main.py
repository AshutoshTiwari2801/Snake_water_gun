################################## Snake, water game #################################
# Its played between the two player and also known as Rock Paper Scissor game
# player1 : computer
# player2 : You
# ####################################################################################
# Author : Ashutosh Kumar Tiwari
# Created on : 13/03/2021
# ####################################################################################
''' In the code : 's' is for Snake
                  'w' is for Water
                  'g' is for Gun
'''
# importing the random module
import random
# player1 = computer and player2 = user or you
# defined a function which tells the player 2 which is you whether you win or loose
def GameWin(player1, player2):
    # checking for all conditions
    # if computer chooses the option as 'snake' as 's' stands for snake
    if player1 =='s':
        if player2=='s':
            print("Its a tie, try again")
            return None
        elif player2=='w':
            print("You loose")
            return False
        elif player2=='g':
            print("You win")
            return True
    # if computer chooses the option as 'water' as 'w' stands for water
    elif player1=='w':
        if player2=='s':
            print("You win")
            return True
        elif player2=='w':
            print("its a tie")
            return None
        elif player2=='g':
            print("you loose, gun drowned")
            return False
    # if computer chooses the option as 'gun' as 'g' stands for gun
    elif player1=='g':
        if player2=='s':
            print("You loose")
            return False
        elif player2=='w':
            print("you win, gun drowned")
            return True
        elif player2=='g':
            print("its a tie")
            return None
print("computer turn to choose Snake(s),water(w) or gun(g)")
randNo= random.randint(1,3)
if randNo==1:
    player1='s'
elif randNo==2:
    player1='w'
elif randNo==3:
    player1='g'
player2 = input("Choose Snake(s) or water(w) or gun(g)")
a = GameWin(player1, player2)
print(a)
print(f"computer played as {player1}".format(player1))
print(f"you played as {player2}".format(player2))
