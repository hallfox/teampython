# creates cheese and crackers function using cheese count and
# boxes of crackers variables 
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
#now we need to get the variables
# here the variables are set directly in the function to 20 and 30
# meaning cheese count = 20 and boxes of crackers = 30
print "We can just give the function numbers directly: "
cheese_and_crackers(20, 30)

#here we set different variables and call the variables in the function
print "OR, we can use variables from our script"
amount_of_cheese = 10
amount_of_crackers = 50

#called cheese n crackers function with the above variables
#which in turn become = to the variables in the function definition
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#calculates the variables directly in the function before calling
print "We can even do math inside too: "
cheese_and_crackers(10 + 20, 5 + 6)

#gets the 2 variables(set to number obviously)
#and adds them to the variables and then runs the function
#I wonder what would happened if you used a string on accident
print "And we can combine the two, variable and math: "
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
