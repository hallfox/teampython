#Remember Order of operation: B.O.D.M.A.S - 
#Brackets, Orders, Division, Multiplication, Addition, Subtraction
print "I will now count my chickens:"

#Division then Addition = 30/6 = 5 + 25 = 30
print "Hens", 25 + 30 / 6
#Multiplication then modulo(%). (25 x 3)=75(75 % 4)= 3, (100-3)=97
print "Roosters", 100 - 25 * 3 % 4
#2.4 % 0.34 = 7 remainder 0.02 = 2.4 % 0.34 = 0.02
print "Test Modulo Divison 2.4%0.34", 2.4 % 0.34
print "Now I will count the eggs:"
# (4%2)=0, (1/4)=0.25, (3+2+1)=6, (6-5)=1, (1+6+0.25)=7.25- 7.25 = integer = 7
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
#(3+5)=8 < (5-7)= -2 = 8 is more than -2 so false.
print "Is it true that 3 + 5 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "oh, that's why it's False."

print "How about some more?"
#5 Greater than -2 =  True
print "Is it greater?", 5 > -2
#True
print "Is it greater or equal?", 5 >= -2
#False
print "is it less or equal?", 5 <= -2