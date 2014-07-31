people = 40
cars = 40
buses = 40

# This statement checks for cars.
# If we have more cars than people, then we should take those cars.
if cars > people:
	print "We should take the cars."
# If we have more people than cars, then those cars may be too crowded.
elif cars < people:
	print "We should not take the cars."
# If we have has many cars as people, then we cannot decide.
else:
	print "We can't decide."

if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."

if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."