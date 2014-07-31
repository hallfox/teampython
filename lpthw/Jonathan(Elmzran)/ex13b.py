from sys import argv

script, name, age, location, food, color, race = argv

print "This script is", script
print "Your name is", name
print "Your age is", age
print "Your location is", location
print "Your favorite food is", food
print "Your favorite color is", color
print "Your race is", race

confirmation = raw_input("Is this information correct? ")

print "You said %s" % confirmation