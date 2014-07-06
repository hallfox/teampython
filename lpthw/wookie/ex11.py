#raw_input takes input and returns strings
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)
	
#test test - same as top
#found online
age = raw_input("How old are you? ")

height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

#testing 2
print "On a scale of 1 to 10, how bored are you?"
print "10 being REALLY bored"
bored = raw_input()
print "That's pretty bored"
print "What's your favorite food?"
food = raw_input()
#study question 4, yes I see that - it put it there automatically