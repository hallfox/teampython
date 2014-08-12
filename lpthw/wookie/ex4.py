#sets variable cars to 100
cars = 100
#sets number of spaces in a car
space_in_a_car = 4.0
#sets num of drivers
drivers = 30
#sets num of passengers
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
#returns float number because uses space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#prints variables and variables that contain math operations w set variables
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

#study drill
#1 not necessary, but if float is used in an operation it returns a float
#2 number that can contain fractions
#3 did most of them
#4 = asigns value  == tests if things have same value
#5 _ = underscore   DUH!
#6 Used python powershell to set variables and do math operations