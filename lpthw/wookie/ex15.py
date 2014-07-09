#from sys module import argument variable
#which allows variables from command line
from sys import argv

#name of script, and sets the 1 variable to filename
script, filename = argv

#creates a variable that is set as a function which opens filename
txt = open(filename)

#prints name of filename
print "Here's your file %r:" % filename
#calls txt open function and then read function
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()