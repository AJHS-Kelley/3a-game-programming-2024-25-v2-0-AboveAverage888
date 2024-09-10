# Loops, Jackques Williams, v0.0   
import random #Import the random module for us to use
# TwO TYPES OF LOOPS
# for <-- Used when you know how many loops you'll need
# while <-- Used when you don't know how many loops you'll need

# for loop is like Gold Fish, you search each card for what the player asked.
# while loop is like musical chairs, you move around until the music stops.

# EACH TRIP THROUGH THE ENITRE LOOP IS CALLED AN iteration
# "iterate through the list" mean use a for loop

# for lop example -- Iterating a list
fruits = ["apple", "banana", "blueberry", "strawberry"]
for eachfruit in fruits:
    print(eachfruit) 

# continue Keydword -- Skips the current iteration and then finishes the loop
#fruits = ["apple", "banana", "blueberry", "strawberry"]
#for eachFruit in fruits:
#    print(eachfruit)
#    if eachFruit == "banana":
#        continue
#print(eachFruit)
# break Keydword -- Immediately exit the loop
#fruits = ["apple", "banana", "blueberry", "strawberry"]
#for eachFruit in fruits:
#    print(eachfruit)
#    if eachFruit == "banana":
#        break
#print(eachFruit)

# for loops using range(). range(x) is exclusive, it starts at 0 and ends at x -1
# for i in range(10, 100): #
#   print(i)
    
#   #Might not always want to start at zero
#for i in range(10,100)
#    print(i)
    

# Not want to count by 1
for i in range(10, 100, 5): # 10 = start, 100 - 1 = stop, 5 - # to count by
    print(i)

# Sometimes you're not done writing the loops
for x in range(10):
    pass # tells Python this loop isn't finished, don't freak out

# while loop -- Musical Chairs
playerScore = 0
counter = 0
while playerScore < 100: # Run as loong as this us True
    print (f"starting: {playerScore}")
    playerScore += random.randint(1,3)
    print(f"After: {playerScore}")
counter += 1
print(counter)


















