x = "There are %d types of people." % 10 #oh no
binary = "binary" #i know where this is going
do_not = "don't" #programmer pun in 3
y = "Those who know %s and those who %s." % (binary, do_not) #2

print(x) #1
print(y) #aaaaand there is

print("I said: %r." % x)
print("I also said: '%s'." % y)

hilarious = False #well at least he's being honest
joke_evaluation = "Isn't that joke so funny?! %r" #brutally honest

print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

#string concatenation (fancy wording for sticking something
#to the end of something else) can be done with +
print(w + e)
