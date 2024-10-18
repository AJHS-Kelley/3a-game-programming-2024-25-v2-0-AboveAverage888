# Rock, Paper, Scrissors by Jackques Williams v3.1

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
def  playerName() -> str: # Function Signature -- name of function, (arguments if any)
    """ Gets the name from the player and returns it."""
    # The line above is a DOCSTRING, it gives a brief exapmle of what the function does.
    playerName = input("Please type your name and press enter\n")
    print(f"Hello {playerName}!\n")
    isCorrect = input("is that correct? Type yes or no and press enter.\n")
    if isCorrect == "yes":
        print(f"Ok {playerName}, let's play rock, paper, scissors!\n")
    else:
        playerName = input("Please type you name and press enter.\n")
    return playerName  

# CALLING THE FUNCTION
playerName = playerName()

# The rules 
def rules() -> None:
    """ This function prints the rules for rock, paper, scissors."""
    print(f"""
    Welcome, {playerName}to the Rock, Paper, Scissors robot!!      
    Lets play rock, paper, scissors!!      
        
    You will play against the CPU. The first player to score 5 points wins.     
    You  will either select rock, Paper, or Scissors.      
    The CPU will select ROCK, PAPER, or SCISSORS at random    
            
    1) Rock beats Scissors     
    2) Scissors beats Paper    
    3) Paper beats Rock      
            """)
    # Does another part of this program need to access this information? 
    # IF YES, YOU MUST HAVE A return STATEMENT
    # IF NO, A return STATEMENT IS NOT REQUIRED

def playerChoice() -> str:
    """Allows the player to choose rock, paper, scissors.11115"""
    playerChoice = input ("Please enter rock, paper, or scissors  and press enter \n").lower()
    if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
        playerChoice = input ("Please enter rock, paper, or scissors  and press enter \n").lower()
        if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
            print("You are not following my rules. Please try again\n")
            exit()
        print(f"You have chosen{playerChoice}\n")
    else:
            print(f"You have chosen {playerChoice} \n")
    return playerChoice

def cpuChoice()-> str:
    """Allows the CPU to choose paper, rock, scissors."""
    cpuChoice = random.randint(0, 2) # randomly selct 0, 1 , or 2.       
    if cpuChoice == 0:
        cpuChoice = "rock"
    elif cpuChoice == 1:
         cpuChoice = "paper"
    elif cpuChoice == 2 :
         cpuChoice = "scissors"
    else :
        print("Unable to determine CPU choice. \n Please restart.\n")
        exit()
    return cpuChoice 

def pickwinner(playerChoice: str, cpuChoice: str) -> str: #playerChoice and cpuChoice are both ARGUMENTS, they wil be string values.
    """ This function uses the player choice and CPU choice to determine a winner"""
    if playerChoice == "rock" and cpuChoice == "paper":
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("CPU win a point. \n")
        cpuScore += 1
        return "CPU Wins"
        # CPU WINS
    elif playerChoice == "rock" and cpuChoice == "scissors" :
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("Player win a point. \n")
        playerScore += 1
        return  "Player Wins"
        # PLAYER WINS
    elif playerChoice == "rock" and cpuChoice == "rock" :
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("its a draw. \n")
        return "Draw"
        # DRAW
    elif playerChoice == "scissors" and cpuChoice == "paper" :
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("Player win a point. \n")
        playerScore += 1
        return "Player Wins"
    elif playerChoice == "scissors" and cpuChoice == "rock" : 
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("CPU win a point. \n")
        cpuScore += 1
        return "CPU Wins"
    elif playerChoice == "scissors" and cpuChoice == "scissors" :
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("its a draw. \n")
        return "Draw"
    elif playerChoice == "paper" and cpuChoice == "paper" :
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("its a draw. \n")
        return "Draw"
    elif playerChoice == "paper" and cpuChoice == "rock" :
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("Player win a point. \n")
        playerScore += 1
        return "Player Wins"
    elif playerChoice == "paper" and cpuChoice == "scissors" :
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("CPU win a point. \n")
        cpuScore += 1
        return "CPU Wins"
    else:
        print("Unable to determine a winner. Please restart. \n")
    exit()
    # return statements IMMEDIATELY exit a function.

def score(winner: str) -> int:
    """ This function uses the winner to update the score for CPU, NUM, DRAWS, and player score."""
    if winner == "Player wins":
        score = 1
    elif winner == "CPU wins":
        score= 1
    else: # This is a DRAW.
        score = 0
    return score



# MAIN GAME LOOP
while playerScore < 5 and cpuScore < 5:
    print(f"{playerName} you have {playerScore} points.\n The CPU has {cpuScore} points \n")
    


    # let player select rock, paper, or scissor
    # let cpu select choice at random
   
    print(f"CPU Choice: {cpuChoice}")

        # compare player choice to cpu choice
   




print(f"Your final score: {playerScore}\n CPU Final Score: {cpuScore}\n")
    # print the results to the screen
    # award point to winner and output results


playerChoice = input ("Please enter rock, paper, or scissors  and press enter\n").lower()