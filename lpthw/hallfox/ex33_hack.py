#the function from the exercise, modified 
def loop_list(n, inc=1):
    numbers = []
    
    for i in range(0, n, inc): 
        print("At the top i is %d" % i)
        numbers.append(i)
        print("Numbers now:", numbers)
 
    print("At the bottom i is %d" % i)
    print() #this seems more readable
    
    print("The numbers: ")
    
    for num in numbers:
        print(num)
 
#a control loop
n = int(input("Enter the size of the list you want to make: "))
inc = int(input("Enter the increment: "))
loop_list(n, inc)  
