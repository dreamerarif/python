'''
1
12
123
1234
12345
'''
# Pyrami8d with python
line=5

for i in range(line): # Outer loop - Line
    for j in range(i+1): # Inner Loop - Line content
        print(j+1, end='')
    print('\n', end='')
    
print("")
'''
12345
1234
123
12
1
'''
    
for i in range(line): # Outer loop - Line
    for j in range(line-i): # Inner Loop - Line content
        print('*', end='')
    print('\n', end='')
    
    
#  *
# ***
#***** 