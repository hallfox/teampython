#announce then return result
def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b

def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b

def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b

def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
#remember this will be a float in 3 but an int in 2
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

#puzzzzlessss
print("Here is a puzzle.")

#that hurts
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
wat = (age + (height - (weight * (iq / 2))))

print("That becomes: ", what, "Can you do it by hand?")
print("Wat:", wat)

#some more credit
def mod(a, b):
    print("MODDING {} % {}".format(a, b))
    return a % b

why = 33 + 5500 / (445 * 3 - 89 % 2)
wai = add(33, divide(5500, subtract(multiply(445, 3), mod(89, 2))))

print("Did I get it?")
print("Why? %d" % why)
print("Wai: %d" % wai)
