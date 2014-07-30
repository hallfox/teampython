#we start combining skills together
from sys import argv

script, filename = argv

#getting the command line arguments
print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

#gathering input
input("?")

print("Opening the file...")
#this opens the file in write mode
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
#this wipes the existing file
target.truncate()

print("Now I'm going to ask you for three lines.")

#get input
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

#and we write the lines in
#extra credit method
target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print("And finally, we close it.")
target.close()

#extra credit
print("We're going to display the file now.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Printing file...")
print()
print(target.read())
print("Printing complete.")
print("Have a nice day.")
