people = 20
cats = 30
dogs = 15

"""
if-statements: evaluates a bit of code if certain conditions are met; otherwise
it skips over the code
"""

if people < cats:
    print("Too many cats! The world is doomed!") #BLASHPHEMY
if people > cats:
    print("Not many cats! The world is saved!") #NNEED MORRE CATZ
if people < dogs:
    print("The world is drooled on!")
if people > dogs:
    print("The world is dry!") #???

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")
if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")
