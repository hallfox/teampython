print "What year is it?"
currentYear = int(raw_input())

print "What year were you born?"
yearBorn = int(raw_input())

def calcAge(currentYear, yearBorn):
	age = currentYear - yearBorn
	print "You are %d years old." %age