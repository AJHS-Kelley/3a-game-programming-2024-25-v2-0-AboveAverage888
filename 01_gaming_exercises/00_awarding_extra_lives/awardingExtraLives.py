# Awarding Extra Lives, Jackques Williams, v0.0


lives = 3
score =int(input("Enter your score then press ENTER\n"))
name = "Ques"

print(f"Hello {name}! You scored {score} points\n")



# CHARACTER REFERENCE
# CURLY BRACES {}
# BRACKETS []
# ANGLE BRACKETS <>
# PARENTHESES ()
# Allow the user to input the score AS AN INTERGER
# If score is 10000 or less 
    # Lose a life
# If score is > 10000 but less than 10001
    # Give 1 extra life
# If score is > 1000000
    # Give 2 extra lives 

# Output the socre and the number of lives to the screen

if score >= 100000:
    print("You gain, 2x lives\n")
    # You will gain the lives
elif score >= 10000:
    print("You will gain a extra life\n")
    # You will gain a life
else:
    print("You lose a life\n")
    # You will lose the life

# Output the socre and the number of lives to the screen








