def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
	
def subtract(a, b ):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	
	
print "Let's do some math with just function!"

age = add(30, 5)#35
height = subtract(78, 4)#74
weight = multiply(90, 2)#180
iq = divide(100, 2)#50

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


#A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."
# what = add(35, subtract(74, multiply(180, divide(50, 2)))) 
#													25                                                         
what = add(age, subtract(height, multiply(weight, divide(iq, 2)))) + 4391

print "That becomes: ", what, "Can you do it by hand?"

#How can I use raw_input() to enter my own values?
#Remember int(raw_input())? The problem with that is then you can't enter 
#floating point, so also try using float(raw_input()) instead.