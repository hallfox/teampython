name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'


#Surprisingly, this method actually works in Python 3, even
#though I thought it didn't. The more common way i see it is
#using the string.format method.
print("Let's talk about %s." % name)
print("He's %d inches tall." % height)
print("He's %d pounds heavy." % weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are usually %s depending on the tea." % teeth)
#this % isn't modulo, but rather a method of string formatting
#in C, there's a function called printf and it works in much
#the same way that this function does
#the %d, %s are format specifiers that specify what kind of
#data will be in that space
#there are a bunch
# %d = Decimals (base 10 numbers)
# %f = Floats (floating point)
# %s = Strings (strings)
#these are the most common, but I've also seen others used like
# %x = heXadecimal (base 16 numbers)


#string.format method
print("Let's talk about {}.".format(name))
print("He's {} inches tall.".format(height))
print("He's {} pounds heavy.".format(weight))
print("Actually that's not too heavy.")
#cool, right? Now watch this.
print("He's got {0} eyes and {1} hair.".format(eyes, hair))
print("His teeth are usually {0} depending on the tea.".format(teeth))
#the numbers will make more sense when you get to lists, but
#basically I'm telling the string to substitute in the nth
#argument to the format function (there is such a thing as a
#0th argument in most languages)
#don't worry too much about it now, but remember to come back
#after the lesson on lists

#this line is suuuper tricky
print("If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight))
