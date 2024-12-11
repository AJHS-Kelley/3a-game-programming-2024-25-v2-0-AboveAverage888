# Flow Control Structures, Jackques Williams, v0.0
# Making Computer Programs Make Decisions

temperature = 88
color = "Black"
height = 8
likesPineappleOnPizza = True 

# SINGLE DECISION POINT - if statement
# if CONDITIONAL_EXPESSION: <-- This will use a COMPARISON OPERATOR 99% of the time
#       runThisCode IF the CONDITIONAL_EXPRESSION is True

if temperature > 100:
   print("It is hot as the sun outside.\n")

if height < 10:
    print("you not good.\n")

# CHEAT CODE FOR IF STATEMENTS THAT USE BOOLEANS.
if likesPineappleOnPizza: 
    print("Nasty")

# What if we want something different to happen
if color == "Black" : # COMMON ERROR FOR STUDENTS IS USING instead of ==.
    print("Your shirt is the correct  unitform color\n")
else:
     print("Your shirt is not the correct  unitform color\n")

if temperature == 188.92:
    print("It is hot as heck\n")
else:
    print("It is too cold\n")

# AMUSEMENT PARK HEIGHT CHECKER EXAMPLE
# Must be > min. height and < max. height to ride

if height <= 6:
    print("You're too tall enough to ride the Sling Shot!\n")
elif height <= 3:
    print("You're too tall to ride the Sling Shot\n")
else: # "dang it dude, something wrong!"
    print("Error,height not detected. DON'T RIDE.\n")

# When writing if-elif-else block checks for the HIGHEST VALUE first when using > or >=
# When writing if-elif-else block checks for the LOWEST VALUE first when using < or <=

# Create an if-elif-else block that check for temperature
# If the temperature is at least 100, print that its too hot outside.
# If the temperature is at least 50 degress but less than 100, print that recess is allowed 
# If the temperature is less than 50 degress but greater than 0, print that recess is in the gym    
# If no temperature is detected, print an error message
    
if temperature >= 100:
    print("It is too hot outside\n")
elif temperature >= 50:
    print("Recess is allowed\n")
elif temperature <= 0:
    print("Recess is allowed in the gym\n")
else:
    print("Error temperature is not found\n")







