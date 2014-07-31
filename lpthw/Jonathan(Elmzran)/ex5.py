name = 'Zed A. Shaw'
age = 35 #not a lie
height_in = 74.0 # inches
weight_lb = 180.0 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

height_cm = height_in * 2.54
weight_kg = weight_lb * 0.453592

print "Let's talk about %s." % name
print "He's %f centimeters tall." % height_cm
print "He's %f kilograms heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height_cm, weight_kg, age + height_cm + weight_kg)