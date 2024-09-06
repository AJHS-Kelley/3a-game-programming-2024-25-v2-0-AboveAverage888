# Loops, Jackques Williams, v0.0   

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
fruits = ["apple", "banana", "blueberry", "strawberry"]
for eachFruit in fruits:
    print(eachfruit)
    if eachFruit == "banana":
        continue
print(eachFruit)
# break Keydword -- Immediately exit the loop
fruits = ["apple", "banana", "blueberry", "strawberry"]
for eachFruit in fruits:
    print(eachfruit)
    if eachFruit == "banana":
        break
print(eachFruit)

