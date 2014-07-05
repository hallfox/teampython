#hey computers understand symbols kinda

#integer
cars = 100
#float, note the decimal point
space_in_a_car = 4.0
#integer
drivers = 30
#integer
passengers = 90
#integer => integer - integer = integer
cars_not_driven = cars - drivers
#integer
cars_driven = drivers
#float => integer * float = float
carpool_capacity = cars_driven * space_in_a_car
#float => integer / integer = float?
#remember in Python 3 / is always true division which
#outputs a floating point
#in the python 2 example this number is actually an integer
#this is because / in Python 2 has // functionality if the
#two numbers being operated on are integer types
#thus, this variable is equal to 3.0, not 3 like in the book
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
