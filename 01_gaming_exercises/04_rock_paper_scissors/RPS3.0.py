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
    isCorrect = input("is that correct? Type yes or no and press enter.\n") .lower()
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

def pickWinner(playerChoice: str, cpuChoice: str) -> str: #playerChoice and cpuChoice are both ARGUMENTS, they wil be string values.
    """ This function uses the player choice and CPU choice to determine a winner"""
    if playerChoice == "rock" and cpuChoice == "paper":
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("CPU win a point. \n")
        return "CPU Wins"
        # CPU WINS
    elif playerChoice == "rock" and cpuChoice == "scissors" :
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("Player win a point. \n")
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
        return "Player Wins"
    elif playerChoice == "scissors" and cpuChoice == "rock" : 
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("CPU win a point. \n")
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
        return "Player Wins"
    elif playerChoice == "paper" and cpuChoice == "scissors" :
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("CPU win a point. \n")
        return "CPU Wins"
    else:
        print("Unable to determine a winner. Please restart. \n")
        exit()
    # return statements IMMEDIATELY exit a function.

def score(winner: str) -> int:
    """ This function uses the winner to update the score for CPU, NUM, DRAWS, and player score."""
    if winner == "Player Wins":
        score = 1
    elif winner == "CPU Wins":
        score = 1
    else: # This is a DRAW.
        score = 0
    return score

# DELETE ALL OF THE OLD CODE UNER THE SCORE FUNCTION.
# ADD THIS NEW CODE BELOW.
def matchWinner(playerScore: int, cpuScore: int) -> bool:
    """ This function dtermines if a player has won the game or not by scoring 5 points."""
    if playerScore >= 5:
        print("Congratulations! You are the winner.\n")
        return True
    elif cpuScore >= 5:
        print("Sadly, you have been defeated by the CPU.\n")
        return True
    else: # No winner yet
        return False

def playGame(playerScore: int,cpuScore: int) -> None:
    """ This function will use all the other functions to play Rock, Paper, Scissors."""
    while True:
        cpuPick = cpuChoice()
        playerPick = playerChoice()
        roundWinner = pickWinner(playerPick, cpuPick)
        if roundWinner == "Player Wins":
            playerScore += score(roundWinner)
        if roundWinner == "CPU Wins":
            cpuScore += score(roundWinner)

        print(f"Player Score: {playerScore}\n")
        print(f"CPU Score: {cpuScore}\n")

        if matchWinner(playerScore, cpuScore) == True:
            break

playGame(playerScore, cpuScore)