#this is where things get weird
#remember that to end a print with a space you have to specify
#the ending character
print("How old are you?", end=" ")
#note that raw_input() is not used
#in python 2, input is a function, but it only accepted valid
#python code
#in python 3, raw_input() was deprecated and input's
#functionality was replaced with raw_input()'s ie input() now
#does what raw_input() did
age = input()
print("How tall are you?", end=" ")
height = input()
print("How much do you weigh?", end=" ")
weight = input()

print("So, you're %r old, %r tall and %r heavy." % (
    age, height, weight))

#as a note, you could rewrite this problem like this
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print("So you're {} old, {}, tall and {} heavy.".format(
    age, height, weight))

#notice that passing a string to the input function will print
#the string out as a prompt without a newline so we don't have
#to specify the ending string
