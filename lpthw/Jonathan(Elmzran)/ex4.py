# Set various variables
# number of cars
cars = 100
# number of passengers that can fit in each car
space_in_a_car = 4
# number of drivers available
drivers = 30
# number of passengers needing transporting
passengers = 90
# number of cars that will not be driven today
cars_not_driven = cars - drivers
# the number of cars that will be driven today
cars_driven = drivers
# the max amount of passengers we could potentially transport today
carpool_capacity = cars_driven * space_in_a_car
# how many passengers we should put in each car with a driver
average_passengers_per_car = passengers / cars_driven

# Print the variables that were set above according to each statement
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."