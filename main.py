x = 5
y = 10
sum = x + y
print(sum)
p = sum(x,y) # sum not defined
print(p)
def sum(x,y):
    z = x + y
    return z 

'''
CODE EXECUTION:
1) creates a variable x with the value 5
2) creates a variable y with the value 10
3) creates a variable sum with the value of x + y
4) displays the value of the variable sum
5) creates a variable p with the value of (runs the function sum)

THIS IS ABSOLUTELY WRONG

'''

def sum(x,y):
    z = x + y
    return z
p = sum(x,y)
print(p)

#code execution flow is: 23,26,23,24,25,26,27