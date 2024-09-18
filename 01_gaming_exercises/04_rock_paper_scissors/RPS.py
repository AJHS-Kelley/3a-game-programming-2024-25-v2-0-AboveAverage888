# Rock, Paper, Scrissors by Jackques Williams v0.1

# Module Imports
import random

# DATA STRUCTURES -- player
playerScore = 8
playerName = "Test Player"
playerChoice = None

# Data Operators -- CPU
cpuScore = 0
cpuChoice = None

# PLAYER NAME INPUT
playerName = input("Please type your name and press enter\n")
print(f"Hello {playerName}!\n")
isCorrect = input("is that correct? Type yes or no and press enter.\n")
if isCorrect == "yes":
    print(f"Ok {playerChoice}, let's play Rock, Paper, Scissors!\n")
else:
    playerName = input("Please type you name and press enter.\n")





# The rules 
print("""
Welcome to the Rock, Paper, Scissors robot!!      
Lets play Rock, Paper, Scissors      
      
You will play against the CPU. The first player to score 5 points wins.     
You  will either select Rock, Paper, or Scissors.      
The CPU will select ROCK, PAPER, or SCISSORS at random    
         
1) Rock beats Scissors     
2) Scissors beats Paper    
3) Paper beats Rock      
        """)

# MULTI-LINE STRINGS CAN BE USED AS BIG COMMENTS
""" You can put comments in these strings aswell"""





# MAIN GAME LOOP
while playerScore < 5 and cpuScore < 5:
    print(f"{playerName} you have {playerScore} points.\n The CPU has {cpuScore} poihnts \n")
    playerChoice = input ("Please enter rock, paper, or scissors  and press enter \n").lower()
    if playerChoice != "rock" or playerChoice != "paper" or playerChoice != "scissors":
        playerChoice = input ("Please enter rock, paper, or scissors  and press enter \n").lower()
        if playerChoice != "rock" or playerChoice != "paper" or playerChoice != "scissors":
            print("You are not following my rules. Please try again\n")
            exit()
            print(f"You have chosen{playerChoice}\n")
        else:
            print(f"You have chosen {playerChoice} \n")
    # let player select rock, paper, or scissor
    # let cpu select choice at random
    # compare player choice to cpu choice
    # print the results to the screen
    # award point to winner and output results


