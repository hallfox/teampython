import random

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number

# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
	# append is a function that lists understand
	elements.append(i)

# now we can print them out too
for i in elements:
	print "Element was: %d" % i

print "Now for a reveral of the count."
the_count.reverse()
for number in the_count:
	print "The count is %d" % number

# let's insert a random number in the count
print "Here's a random number insertion."
the_count.insert(random.choice(the_count), random.randrange(0,1000))
for number in the_count:
	print "The count is %d" % number

# now let's insert 25 random numbers, and print them out
print "We will now insert 25 random numbers."
while i < 25:
	the_count.insert(random.choice(the_count), random.randrange(0,1000))
	i += 1
for number in the_count:
	print "The count is %d" % number

# we should sort these numbers
print "Let's sort the numbers, and then print them in order."
the_count.sort()
for number in the_count:
	print "The count is %d" % number