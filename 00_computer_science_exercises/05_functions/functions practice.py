# Functions Practice, Jackques Williams, v0.0  

import random

language = input 
def helloWorldMulti(): # FUNCTION SIGNATURE
    """This function will output Hello, World! in a language the user choose.""" #DOCSTRING \
    # print a list of language to the scren, at least three but no more than five.
    # allow the user to select (input) a chice for the language.
    # print "Hello, World!" to the screen in that language.
    print("""
        Welcome to the Hello, World! Languages Available
        [E]nglish
        [S]panish
        [F]rench
         """ )
    language = input("what language would you like\n Type the first letter of the language you want\n").upper()

    if language == "E":
        print("Hello, World\n")
    elif language == "S":
        print("Hola, Mundo\n")
    elif language == "F":
        print("Salut tout le, Monde\n")
    else:
        print("you stupid, try again")

#helloWorldMulti() # FUNCTION CALL

# Function to determinje even / odd numbers
argument1 = random.randint (-1000, 1000)

def isEven(argument1: int) -> bool: # Requires one ARGUMENT (argument1) and RETURNS a Boolean value
    """ Determines if an interger value is even or odd"""
    if argument1 % 2 == 0:
        return True
    else: 
        return False

print(isEven(argument1))

# Functions with Multiple Arguments
def  canRideRollerCoaster(age: int, height: int) -> bool:
    if age > 10 and height > 4:
        print("You can ride\n")
        return True
    else:
        print("You cannot ride\n")
        return False
    
canRideRollerCoaster(4,10) # Arguments must be passed in the same order as the function signature indicates.