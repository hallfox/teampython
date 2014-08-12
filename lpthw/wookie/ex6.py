#This block sets the variables to a number and 2 strings
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
#Sets a variable to a string which includes 2 variables which
#are also strings
#There are 2 strings in this string \/
y = "Those who know %s and those who %s." % (binary, do_not)

#prints x and then y
print x
print y

#prints variable x
#string in a string
print "I said: %s." % x
#prints variable y
#string in a strong here too
print "I also said: '%s'." % y

#set hilarious to boolean value false
hilarious = True

#sets joke evaluation to a string that includes an unknown
#string variable
joke_evaluation = "Isn't that joke so funny?! %s"

#prints joke_eval with the hilarious variable
#it was funny - I'll change to true
print joke_evaluation % hilarious

#sets 2 variables to 2 strings
w = "This is the left side of..."
e = "a string with a right side."

#adds 2 strings
#this makes a longer string because w and e are both strings
#using the addition symbol creates an even bigger one!
print w + e

### testing
### a string format variable must be in quotes to display
###
print "I am kinda %s" % "bored"