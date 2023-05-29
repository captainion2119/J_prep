'''
Predict the outputs & if errors found, fix them:

1)
count = 0
while count < 10:
    print("hello")
        count += 1

2)
x = 10
y = 0
while y < x:
    print(x,y)
    x = x - 1
    y = y + 1

3)
keepgoing = True
x = 100
while keepgoing:
    print(x)
    x = x - 10
    if x < 50:
        keepgoing = False

4)
x = 45
while x < 50:
    print(x)

5)
for x in [1,2,3,4,5]:
    print(x)

6)
for p in range(1,10):
    print(p)

7)
for z in range(-500,500,100):
    print(z)

8)
x = 10
y = 5
for i in range(x - y * 2):
    print("%",i)

9)
c = 0
for x in range(10):
    for y in range(5):
        c += 1
print(c)

10)
x = [1,2,3]
counter = 0
while counter < len(x):
    print(x[counter]*'%')
    for y in x:
        print(y * '* ')
    counter += 1

11)
for x in 'lamp':
    print(str.upper(x))

12)
x = 'one'
y = 'two'
counter = 0
while counter < len(x):
    print(x[counter],y[counter])
    counter += 1

13)
x = "apple, pear, peach"
y = x.split(",")
for z in y:
    print(z)

14)
x = "apple, pear, peach, grapefruit"
y = x.split(",")
for z in y:
    if z < 'm':
        print(str.lower(z))
    else:
        print(str.upper(z))

15)
name = "Gregory"
print("Greetings!!!")
    print("Hello",name)
    print("How do you do?")

'''

'''
a) Write a program that asks the user to input number of seconds and then expresses it in terms of how many minutes and seconds it contains.

b) Write a program that repeatedly asks from users some number until string 'done' is typed. The program should print the sum of all numbers entered.

c) Write a program to print a square multiplication table as shown below:

1   2   3   4   5   6   7   8   9
2   4   6   8   10  12  14  16  18
3   6   9   12  15  18  21  24  27
4   8   12  16  20  24  28  32  36
5   10  15  20  25  30  35  40  45
6   12  18  24  30  36  42  48  54
7   14  21  28  35  42  49  56  63
8   16  24  32  40  48  56  64  72
9   18  27  36  45  54  63  72  81

'''

# Answers here:

# 1.
# hello
# hello
# hello
# hello
# ...
# hello
# WRONG CORRECT = 10

# 2. (10,0) (9,1) (8,2) (7,3) (6,4)
# CORRECT

# 3. 100,90,80,70,60,50
# CORRECT

# 4. 45..... infinite
# CORRECT

# 5. 1
#    2
#    3
#    4
#    5
# CORRECT

# 6. 1
#    2 
#    .
#    .
#    .
#    10
# WRONG CORRECT = TILL 9

# 7. -500
#    -400
#    -300
#     .
#     .
#     500
# WRONG CORRECT = TILL 400

# 8. blank 
# CORRECT

# 9. 0
#    1
#    2
#    3
#    4
# WRONG CORRECT = 50

# 10.%
#    *
#    **
#    ***
#    %% 
#    *
#    **
#    ***
#    %%%  
#    *
#    **
#    ***
# WRONG CORRECTED

# 11. 
# L
# A
# M
# P
# WRONG CORRECTED

#12.
# o t
# n w
# e o
# WRONG CORRECTED

# 13. apple
#     pear
#     peach
# "apple, pear, peach"
# apple
#  pear
#  peach
# PASS

# 14. x = ['apple', 'pear', 'peach', 'grapefruit']
#     y = x.split(",")
#     for z in y:
#        if z<2:
#   		print(str.lower(z))
# 	 else:
# 		print(str.upper(z))

# apple
#  pear
#  peach
#  grapefruit
# PASS

# 15. 
# name = "Gregory"
#     print("Greetings!!!")
# 	print("Hello " + str(name))
# 	print("How do you do?")
	
#     OUTPUT:
#       Greetings!!!
#       Hello Gregory
#       how do you do?
# CORRECT

# 16. seconds = int(input(seconds))
#     min = seconds//60 // floor division
#     sec = seconds%60                            
#   print(" min",min +" sec",sec)
# WRONG CORRECTED

# ANSWER:
#17. final = 0
# inp = input("Enter a number or 'done': ")
# while inp != "done":
#     final += int(inp)
#     inp = input("Enter a number or 'done': ")
# print(final)
# WRONG CORRECTED

#18. for row in range(1,10):
#     for col in range(1,10):
#         prod = row * col
#         if prod < 10:
#             print(" ",prod,'',end="\t")
#         else:
#             print(prod,'',end="\t")
#     print()
# PASS CORRECTED


# =================================================================================================================================================================================================

'''

1) Find the errors and predict the output of the following:
s1 = 'must'
s2 = 'try'
n1 = 10
n2 = 3
print(s1 + s2)
print(s2 * n2)
print(s1 + n1)
print(s2 * s1)

2) Predict the output of the following:
x = "abcdef"
i = "a"
while i in x:
    print(i,end=" ")

3) For the following code:
string = input("Enter a string: ")
count = 3
while True:
    if string[0] == 'a':
        string = string[2:]
    elif string[-1] == 'b':
        string = string[:2]
    else:
        count += 1
        break
print(string)
print(count)

What will be the output for the following inputs:
i) aabbcc
ii) aaccbb
iii) abcc

4) For the following code:
Inp = input("Please enter a string: ")
while len(Inp) <= 4:
    if Inp[-1] == 'z':
        Inp = Inp[0:3] + 'c'
    elif 'a' in Inp:
        Inp = Inp[0] + 'bb'
    elif not int(Inp[0]):
        Inp = '1' + Inp[1:] + 'z'
    else:
        Inp = Inp + '*'

What will be the output for the following inputs:
i) 1bzz
ii) '1a'
iii) 'abc'
iv) '0xy'
v) 'xyz'

5) Write a program that takes a string with multiple words and then capitalizes the first letter of each word and forms a new string out of it.

6) Write a program that reads a string and checks whether it is a palindrome string or not.

7) What is the answer to the following expressions:
if, L = ["These",["are","a"],["few","words"],"that","we","will","use"]

i) L[3:4]+L[1:2]
ii) "few" in L[2:3]
iii) "few" in L[2]
iv) L[2][1:]
v) L[1]+L[2]

8) Predict the output:
aLst = [1,2,3,4,5,6,7,8,9]
print(aLst[::3])

9) Predict the output:
Lst = [1,2,3,4,5,6,7,8,9]
Lst[::2]=10,20,30,40,50,60
print(Lst)

10) Predict the output:
values = []
for i in range(1,4):
    values.append(i)
    print(values)

11) Predict the output:
rec = {"Name":"Python","Age":"20"}
r = rec.copy()
print(id(r) == id(rec))

12) Predict the output:
dc1 = {}
dc1[1] = 1
dc1['1'] = 2
dc1[1.0] = 4
sum = 0
for k in dc1:
    sum += dc1[k]
print(sum)

13) Predict the output:
fruit = {}
f1 = ['Apple','Banana','apple','Banana']
for index in fruit:
    if index in fruit:
        fruit[index] += 1
    else:
        fruit[index] = 1
    print(fruit)
print(len(fruit))

14) Find the error:
aLst = {'a':1,'b':2,'c':3}
print(aLst['a','b'])

15) Find the error and give reason:
box = {}
jars = {}
crates = {}
box['biscuit'] = 1
box['cake'] = 3
jars['jam'] = 4
crates['box'] = box
crates['jars'] = jars
print(crates[box])

16) Consider a dictionary "points" with single-letter keys, each followed by a 2-element tuple representing the coordinates of a point in an x-y coordinate plane.

points = {'a':(4,3),'b':(1,2),'c':(5,1)}

Write a program to calculate the maximum value from within all of the value's tuples at the same index.
eg: for 0th index the values 4,1,5 will be taken, i.e 0 index values from all the tuples and the maximum will be calculated.
    hence output will be: 
                            Maximum value at index(points,0) = 5

17) Find errors and give reasons:

i)
t = (1,"a",9.2)
t[0] = 6

ii)
t = [1,"a",9.2]
t[0] = 6

iii)
t = [1,"a",9.2]
t[4] = 6

iv)
t = 'Hello'
T[0] = 'H'

v)
for Name in [Jaanu,Rio,Rahul]
    IF Name[0] = 'S':
        print(Name)
'''

