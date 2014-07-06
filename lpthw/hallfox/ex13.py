#importing from the module
#note I could also add the word 'as' to change the name of the
#module, like this
from sys import argv as peanuts

#unpacking here, need EXACTLY the same arguments put in
script, first, second, third = peanuts

#little extra credit (3)
color = input("What is your favorite color? ")

#printing to show it works
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

print("Your favorite color is:", color)
