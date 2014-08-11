states = {
    "Oregon": "OR",
    "Florida": "FL",
    "California": "CA",
    "New York": "NY",
    "Michigan": "MI"
}

cities = {
    "CA" : "San Francisco",
    "MI" : "Detroit",
    "FL" : "Jacksonville"
}

cities['NY'] = "New York"
cities["OR"] = "Portland"

sep = '-'*10

print(sep)
print("NY State has: ", cities["NY"])
print("OR State has: ", cities["OR"])

print(sep)
print("Michigan's abbreviation is: ", states["Michigan"])
print("Florida's abbreviation is: ", states["Florida"])

print(sep)
print("Michigan has: ", cities[states["Michigan"]])
print("Florida has: ", cities[states["Florida"]])

print(sep)
for state, abbrev in states.items():
    print("%s is abbreviated %s" % (state, abbrev))

print(sep)
for state, abbrev in states.items():
    print("%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev]))

print(sep)
state = states.get("Texas")

if not state:
    print("Sorry, no Texas.")

city = cities.get("TX", "Does Not Exist")
print("The city for the state 'TX' is: %s" % city)
