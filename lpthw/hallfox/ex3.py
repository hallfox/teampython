#printing
print("I will now count my chickens:")

#commas add a space in between each argument
#here we print 30 integer division 6, which is 5, plus 25, which is 30
#the '//' is the Python3 way of doing integer division, which is a way
#to do normal division but cut off any decimal points
print("Hens", 25 + 30 // 6)
#the only new thing here is the % symbol (pronounced 'modulus'), this
#does integer division but takes the remainder as the result
#ie when we say 3 % 4, we get the remainder of 3 // 4 (3 // 4 == 0, because 
#3 / 4 == 0.75, but then we drop the decimal), and that number is 3
#therefore, we multiply 3 by 25 to get 75 and subtract that from 100 to get 25
print("Roosters", 100 - 25 * 3 % 4)

print("Now I will count the eggs:")

#this just shows you don't need to print a string, python will convert it
#for you
print(3 + 2 + 1 - 5 + 4 % 2 - 1 // 4 + 6)
#here's a floating point version, this should give an absurd measurement
#of eggs
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5 - 7?")

#< is the 'less than' comparator and it produces a boolean value (True or False)
#in this case we ask it to print 5 < -2, which is a false statement, thus it
#is false
print(3 + 2 < 5 - 7)

#it's on the tin
print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

#explaining what I just explained
print("Oh, that's why it's False.")

print("How about some more.")

#yup
print("Is it greater?", 5 > -2)

#i think we get it: <, >, <=, >=, ==, and != are all comparison operators
#== checks if two values are the same while != does the opposite
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= 2)

