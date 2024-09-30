# Rock, Paper, Scrissors by Jackques Williams v0.1

# Module Imports
import random, time

# DATA STRUCTURES -- player
playerScore = 0
playerChoice = None
numDraws = 0

# Data Operators -- CPU
cpuScore = 0
cpuChoice = None

# MAIN GAME LOOP
loopCount = 0
loopsReq = int(input("How many  loops do you want?\n Enter an interger, no commas, and press ENTER"))
# req is the universal abbreviation in computer programming for REQUEST. reqs = REQUEST
rpsTimeStart = time.time() # returns the number of seconds since Jan .01 1970 @ 12:00AM
while loopCount < loopsReq: 
    # let CPU select choice at random
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
    # print(f"CPU Choice: {cpuChoice}")

    # let PLAYER select choice at random
    playerChoice = random.randint(0, 2) # randomly selct 0, 1 , or 2.       
    if playerChoice == 0:
        playerChoice = "rock"
    elif playerChoice == 1:
         playerChoice = "paper"
    elif playerChoice == 2 :
         playerChoice = "scissors"
    else :
        print("Unable to determine CPU choice. \n Please restart")
        exit()

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
    loopCount += 1



print(f"Your final score: {playerScore}\n CPU Final Score: {cpuScore}\n Draws {numDraws}\n")
if playerScore > cpuScore:
    print(f"Congratulations. a winner is you\n")
elif cpuScore > playerScore:
    print(f"The CPU wins. You fail to exist from now on.\n")
else:
    print("Unable to determine a winner.\n Please restart\n")
    exit()  

rpsTimeStop = time.time()
rpsTime = rpsTimeStop - rpsTimeStart
print(f"Number of Loops: {loopCount}\n")
print(f"Execution Time {rpsTime: .2F} seconds. \n") # :.2F formats to 2 decimal places





