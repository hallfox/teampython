print(True and True) #True
print(False and True) #False
print(1 == 1 and 2 == 1) #False
print("test" == "test") #True
print(1 == 1 or 2 != 1) #True
print(True and 1 == 1) #True
print(False and 0 != 0) #False
print(True or 1 == 1) #True
print("test" == "testing") #False
print(1 != 0 and 2 == 1) #False
print("test" != "testing") #True
print("test" == 1) #False
print(not (True and False)) #True
print(not (1 == 1 and 0 != 1)) #False
print(not (10 == 1 or 1000 == 1000)) #False
print(not (1 != 10 or 3 == 4)) #False
print(not ("testing" == "testing" and "Zed" == "Cool Guy")) #True
print(1 == 1 and not ("testing" == 1 or 1 == 0)) #True
print("chunky" == "bacon" and not (3 == 4 or 3 == 3)) #False
print(3 == 3 and not ("testing" == "testing" or "Python" == "Fun")) #False

"""
Notice a pattern? 
If there's an and statement and the first part is False, then the statement always evaluates to False, else the second part is the value of the statement.
If there's an or statement and the first part is True, then the statement always evaluates to True, else the second part is the value of the statement.
This is called 'short-circuiting.'
"""
