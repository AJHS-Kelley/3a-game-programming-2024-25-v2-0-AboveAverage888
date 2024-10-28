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
    else:
        print("Salut tout le, Monde\n")

helloWorldMulti()






