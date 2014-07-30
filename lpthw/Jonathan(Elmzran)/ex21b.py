def sentence_combiner(word1, word2, word3, word4, word5):
	space = " "
	return word1 + space + word2 + space + word3 + space + word4 + space + word5 + "."

prompt = "> "
print "Let's make a 5 word sentence."
word1 = raw_input("First word:\n" + prompt)
word2 = raw_input("Second word:\n" + prompt)
word3 = raw_input("Third word:\n" + prompt)
word4 = raw_input("Fourth word:\n" + prompt)
word5 = raw_input("Fifth word:\n" + prompt)

mysentence = sentence_combiner(word1, word2, word3, word4, word5)
print mysentence

print "Now let's do math stuff."

def addition(a, b):
	print "Adding %f + %f" % (a, b)
	return a + b

def subtraction(a, b):
	print "Subtracting %f - %f" % (a, b)
	return a - b

def multiplication(a, b):
	print "Multiplying %f * %f" % (a, b)
	return a * b

def division(a, b):
	print "Dividing %f / %f" % (a, b)
	return a / b

print "Let's make some huge crazy equation thing to solve (88 + (56 / 42)) + ((7 * 76) + (560 - 42))\nSome variables will be used as well."

the_meaning = 42.0
favorite_number = 7.0
answer = addition(addition(88, division(56, the_meaning)), addition(multiplication(favorite_number, 76), subtraction(560, the_meaning)))

print "The answer is %f." % answer