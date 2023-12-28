st = "This is Python!!"

#for x in st:
#    print(x)
    
    
#programmingLanguage = ["C", "C++", "Java", "Python", "PHP", "Ruby", "Javascript"]

# example of break statement
'''for x in programmingLanguage:
    print(x)
    if x == "Java":
        break'''
        
# example of continue statement
'''for x in programmingLanguage:
    if x == "Java":
        continue
    print(x)
'''



# Printing 1 to 10 using for loop

#for x in range(10):
#    print(x+1)
    
# range function

#range(start, stop, step)
#range(1, 10, 2) >> 1,9,2 


# Printing 10 to 1 using for loop

#for x in range(1, 12, 2):
#    print(x)

#for x in range(10,0,-1):
#    print(x)


#for x in reversed(range(10)):
#    print(x+1)
    
#for x in reversed(range(1,11)):
#    print(x)
    
# print odd numbers from 1 to 100
#for x in range(1, 101, 2):
#    print(x)


# Check if a provided number is odd or even
# + = addition, - = subtarction, * = multiplication, / = division, % = modulus (remainder)
#x=1000065
#y=x%2
#print(y)

'''if x%2 == 0:
    print(x, "is even number")
else:
    print(x, "is odd number")'''
    
fruits = ["apple", "banana", "orange"]
for x in fruits:
    print (x)
    if x == "banana":
        break