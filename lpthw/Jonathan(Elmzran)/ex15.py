# imports arguments given when script is run
from sys import argv

# assigns arguments given to two separate variables, one is script name,
# and the other is the second file name
script = argv

print "Enter the filename below:"
filename = raw_input("> ")

txt = open(filename)
print txt.read()
txt.close()