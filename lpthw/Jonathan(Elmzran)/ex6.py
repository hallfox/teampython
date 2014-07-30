# sets x equal to a string with a string formatter
x = 'There are %d types of people.' % 10
# sets binary to a string
binary = "binary"
# sets do_not to a string that is a conjunction of itself
do_not = "don't"
# sets y to a string that is formatted with the binary and do_not strings
y = "Those who know %s and those who %s." % (binary, do_not)

#prints both x and y
print x
print y

#prints strings using x and y as string formatters
print "I said: %r." % x
print "I also said: '%s'." % y

#sets hilarious to false
hilarious = False
#sets joke_evaluation to a string with a formatter
joke_evaluation = "Isn't that joke so funny?! %r"

#uses the formatter in joke_evaluation with the var hilarious
print joke_evaluation % hilarious

#sets strings to w and e
w = "This is the left side of..."
e = "a string with a right side."

# combines w and e strings and prints them together
print w + e