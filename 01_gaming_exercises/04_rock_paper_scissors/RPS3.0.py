# Rock, Paper, Scrissors by Jackques Williams v3.0

# Module Imports
import random

# DATA STRUCTURES -- player
playerScore = 0
playerName = "Test Player"
playerChoice = None

# Data Operators -- CPU
cpuScore = 0
cpuChoice = None

# PLAYER NAME INPUT
def  playerName(): # Function Signature -- name of function, (arguments if any)
    playerName = input("Please type your name and press enter\n")
print(f"Hello {playerName}!\n")
isCorrect = input("is that correct? Type yes or no and press enter.\n")
if isCorrect == "yes":
    print(f"Ok {playerName}, let's play rock, paper, scissors!\n")
else:
    playerName = input("Please type you name and press enter.\n")

# .lower() can turn all input into lowercase
# .upper() can turn all input into lowercase  

# CALLING THE FUNCTION
playerName()



# The rules 
print("""
Welcome to the Rock, Paper, Scissors robot!!      
Lets play rock, paper, scissors      
      
You will play against the CPU. The first player to score 5 points wins.     
You  will either select rock, Paper, or Scissors.      
The CPU will select ROCK, PAPER, or SCISSORS at random    
         
1) Rock beats Scissors     
2) Scissors beats Paper    
3) Paper beats Rock      
        """)

# MULTI-LINE STRINGS CAN BE USED AS BIG COMMENTS
""" You can put comments in these strings aswell"""





# MAIN GAME LOOP
while playerScore < 5 and cpuScore < 5:
    print(f"{playerName} you have {playerScore} points.\n The CPU has {cpuScore} points \n")
    playerChoice = input ("Please enter rock, paper, or scissors  and press enter \n").lower()
    if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
        playerChoice = input ("Please enter rock, paper, or scissors  and press enter \n").lower()
        if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
            print("You are not following my rules. Please try again\n")
            exit()
        print(f"You have chosen{playerChoice}\n")
    else:
            print(f"You have chosen {playerChoice} \n")


    # let player select rock, paper, or scissor
    # let cpu select choice at random
    cpuChoice = random.randint(0, 2) # randomly selct 0, 1 , or 2.       
    if cpuChoice == 0:
        cpuChoice = "rock"
    elif cpuChoice == 1:
         cpuChoice = "paper"
    elif cpuChoice == 2 :
         cpuChoice = "scissors"
    else :
        print("Unable to determine CPU choice. \n Please restart")
        exit()
    print(f"CPU Choice: {cpuChoice}")

        # compare player choice to cpu choice
    if playerChoice == "rock" and cpuChoice == "paper":
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("CPU win a point. \n")
        cpuScore += 1
        # CPU WINS
    elif playerChoice == "rock" and cpuChoice == "scissors" :
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("Player win a point. \n")
        playerScore += 1
        # PLAYER WINS
    elif playerChoice == "rock" and cpuChoice == "rock" :
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("its a draw. \n")
        # DRAW
    elif playerChoice == "scissors" and cpuChoice == "paper" :
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("Player win a point. \n")
        playerScore += 1

    elif playerChoice == "scissors" and cpuChoice == "rock" : 
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("CPU win a point. \n")
        cpuScore += 1

    elif playerChoice == "scissors" and cpuChoice == "scissors" :
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("its a draw. \n")
    elif playerChoice == "paper" and cpuChoice == "paper" :
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("its a draw. \n")
    elif playerChoice == "paper" and cpuChoice == "rock" :
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("Player win a point. \n")
        playerScore += 1
    elif playerChoice == "paper" and cpuChoice == "scissors" :
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("CPU win a point. \n")
        cpuScore += 1
    else:
        print("Unable to determine a winner. Please restart. \n")
    exit()




print(f"Your final score: {playerScore}\n CPU Final Score: {cpuScore}\n")
    # print the results to the screen
    # award point to winner and output results


playerChoice = input ("Please enter rock, paper, or scissors  and press enter\n").lower()