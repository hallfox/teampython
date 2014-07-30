def loop_list(n, inc=1):
    numbers = []
    
    for i in range(0, n, inc): #there's a bug in this line, can you find it?
        print("At the top i is %d" % i)
        numbers.append(i)
        print("Numbers now:", numbers)

    print("At the bottom i is %d" % i)
    print() #this seems more readable
    
    print("The numbers: ")
    
    for num in numbers:
        print(num)

loop_list(10) #what do you think inc is equal to in this case?
loop_list(7, 3)
