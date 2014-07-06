#argv takes input from command line
from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

#AHHH
print "\n\n"

fruit = raw_input("What's your favorite fruit?")
print "Y u like %s" % fruit