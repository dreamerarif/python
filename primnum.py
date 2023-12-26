'''#Formula 1
x = 3
flag = False   #define a flag variable

if x == 1:
    print (x, "is not a prime number")
elif x > 1:
    for i in range(2, x):
        if (x % i) == 0:
            flag = True  #if found, flag is true
            break   #loop break
    if flag:
        print ( x, "is not a prime number") #if flag is true
    else:
        print (x, "is a prime number") #if flag is false
'''       

#Formula 2 
'''x = 3

if x > 1:
    for i in range(2, int(x/2)+1):
        if (x % i) == 0:
            print (x, "is a prime number")
            break
    else:
        print ( x, "is a prime number")
else:
    print (x, "is not a prime number")'''


#Formula 3
x = -1

if x == 1:
    print (x, "is not a prime number")
elif x > 1:
    for i in range(2, x):
        if (x % i) == 0:
            print(x, "is not a prime number")
            break
    else:
        print(x, "is a prime number")
else:
    print("Invalid Number")
 
# Git Conflict Check
#This is primnumber finder
#Problem
#Conflict resolved