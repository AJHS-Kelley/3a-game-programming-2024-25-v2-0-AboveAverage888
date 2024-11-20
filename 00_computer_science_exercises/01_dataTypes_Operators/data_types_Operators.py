# Data Types and Operators, Jackques Williams, v0.0

# Fundamental Data Types
# String - str - Sequence of letters, number, spaces, or other characteristics.
# String in Python are inside  ' ' or " "
#Idc if you use ' ' or " " just be consistent

# Boolean- bool- True or False values

# Float - float - any number value with a decimal including 0, +/-

# Integers - int - any whole number including 0, +/-

# Data Types are stored in VARIABLES.
# A Variable is basically a bucket with a name to put data into.
# VARIABLES NAME SHOULD TELL YOU WHAT DATA IS BEING STORED IN IT.
# VARIABLES CAN'T START WITH A NUMBER
# camelCaseVariablesNames
# snake_case_variables_names

# DECLARING VARIABLES AND ASSIGNING VALUES

high_score = 884654 # int data type
highScore = 294514 # int data types

carSpeed = 18.64 # float data type, miles per hour
car_speed = -9.5664848 # float data type, miles per hour

hasAxe = True # boolean data type
isPurple = False # boolean data type

playerName = "Jackques Williams" # string data type
enemyType = "wind" # string data type

# Assign NEW VALUES
playerName = "Gambit"
carSpeed = "9.50"

# DATA TYPES CAN CHANGE, BE CAREFUL
hasAxe = 4.5

# Print Data Types
newInt = 3
newFloat = 5.0
newString = "Peanut Butter"
newBool = False

print(type(newInt))
print(type(newString))
print(type(newFloat))
print(type(newBool))

# print Variables to Console / Screen
print(playerName)
print(isPurple)
print(highScore)
print(carSpeed)

# print variables and expression to console / screen
print(highScore + 9000)
print(45 * 2)
print(highScore)


# PRINTING VARIABLES INSIDE OF STRINGS
print(f"Hello {playerName}. Your high score is {highScore}. \n")

# ARITHMETIC OPERATORS
myInt = 5
myFloat = 4.68
myNum = 0

# addition
myInt = 4 + 6
myFloat = 4.6 + 6.8

myInt = myInt + 5

myNum = myInt + myFloat 
# when you add an int  and a float together, the answer becomes a float

# subtraction
myNum = myInt - myFloat
myInt = myFloat - 32

# multiplication
myNum = myInt * myFloat

# Division
myNumber = myInt / myFloat # first is numerator, second is denominator

# MODULUS (MODULO) % --Returns REMAINDER after dividing
# MOST COMMON USE FOR MODULUS IS DETERMINING EVEN / ODD NUMBERS
numStudents = 8
numSlicesPizza = 32

leftOvers = numSlicesPizza % numStudents
print(leftOvers)

# EXPONETS **
numSquared = 6 ** 2 # 6 is the base, 2 is the exponent

# FLOOR-DIVISION // Divides, throws out any decimal.
myNum = myInt // myFloat

# Addition-Assignment Operator - Mostly used for counters
myNum = 4
myNum = myNum + 2 #Old-School Method
myNum += 1 # New hotness 
myNum *= 1
myNum /= 1

# COMPARISON OPERATORS


# IS-EQUAL-TO == Are the two values equapl to each other?
# Returns True or False based on evaluation
x = 12.0
# print(x ==5)

# NOT-EQUAL-T!= Are the two values not equal?
# Returns True or False based on evaluation
print(x !=12)

# # GREATER THAN/ GREATER-THAN-OR-EQUAL- TO
# print(5 > 3) # Greater Than
# print( 12 >= 2) # Greater than or equal to

# # LESS THAN / LESS-THAN-OR-EQUAL-TO
# print(5 < 3) # LESS than
# print( 12 <=  2) # Less than or equal to

# LOGICAL OPERATORS
# and -- ALL CONDITIONS MUST BE TRUE FOR ENTIRE STATMENT TO BE TRUE
age = 16
height = 87.9
eyeColor = "Dark Brown"
# In order to ride the Teacups, you must be at least 18 years old and at least 60' tall
# print(age >= 18 and height >= 60)
# print(age >= 18 and height >= 60 and eyeColor == "Green")
# ALWAYS CHECK FOT THE LEAST-LIKELY TO BE FALSE CONDITION FIRST!!!
# print(defeatedBoss == True and level > 5 and hasBlueKey == True)


# or --  AT LEAST ONE CONDITION MUST BE TRUE FOR ENTIRE STATMENT TO BE TRUE
# print(age >= 18 or height >= 60)
# print(age >= 18 or height >= 60 or eyeColor == "Green")
# ALWAYS CHECK FOR THE MOST-LIKELY TO BE TRUE FIRST!!!
# print(defeatedBoss == True or level > 5 or hasBlueKey == True)

# not -- RETURNS THE OPPOSITE VALUES OF THE STATMENT.
a = 9
print(a == 9)
print(not (not (a == 9)))

# COMBINING LOGICAL OPERATORS
# print(a == 9 and hasKey == True or isCloud == True)
# TRUE and 

# IDENTITY OPERATORS
g = 1.0
h = 1.0
i = g
print( g is h)
print(i is h)
print(i is not 1.0 )
print(i is not g)

# MEMBERSHIP OPERATORS
fruits = ["apple, banana, tomato"]
print("banana" in fruits)
print("potato" in fruits)





