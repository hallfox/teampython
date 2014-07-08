cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#Prints the text, then variable 100, then text
print "There are", cars, "cars available"

#Prints the text, then variable 30, then text
print "There are only", drivers "drivers available' 

#Prints the text, then variable (100-30)=70, then text
print "There will be" cars_not_driven "empty cars today"

#Prints the text, then variable (30x4.0)=120, then text
print "We can transport", carpool_capacity, "people today"

#Prints the text, then variable 90, then text
print "We have", passengers, "to carpool today."

#Prints the text, then variable(90/30)=3 , then text
print "We need to put about", average_passengers_per_car, "in each car."