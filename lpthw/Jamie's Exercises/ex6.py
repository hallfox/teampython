#Prints 10 in %d - if called prints text with %d = 10.
#1- Sting inside String(nested)
x = "There are %d types of people." % 10

#var = text output
binary = "binary"

#var = text output
do_not = "don't"

#var = text with %'s = binary and do_not.
#2 - String inside String(nested)
y = "those who know %s and those who %s." % (binary, do_not)

#prints var x + y
print x
print y

#prints text - %r= var(x)
print "I said %r." % x
#prints text - %s = var(y)
print "I also said: '%s'." % y

#Declare var(hilarious) = value (false)
hilarious = False

#declare var(joke_evaluation) = text
#3- String inside String(nested)
joke_evaluation = "Isn't that joke so funny?! %r"

#prints var(joke_evaluation) -%r = hilarious
print joke_evaluation % hilarious

#declare var(w) = text
w = "this is the left side of..."
#declare var(e) = text
e = "a string with a right side."

#prints var (w + e)
#w + e = "text.."+"text..." - making one sentence.
print w + e