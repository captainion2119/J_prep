# Corrected Ans 1 (accurate code, incorrect logic)
# s_1 = int((input("Enter the marks of subject 1: ")))
# s_2 = int((input("Enter the marks of subject 2: ")))
# s_3 = int((input("Enter the marks of subject 3: ")))  #Directly took value as integer as value is not in any other form in the code
# avg = (s_1+ s_2 +s_3)/3
# if (avg >= 90):                                       # '>=' Missed, logical error!
#     print("grade A")
# elif (avg < 90 and avg >= 80):
#     print("grade B")
# elif (avg < 80 and avg >= 70):
#     print("grade C")
# else:
#     print("grade D")

# Corrected Ans 3 (accurate code, correct logic)
# yr = int(input("enter the year : "))                  #Directly took value as integer as value is not in any other form in the code
# if (yr%400 == 0) and (yr%100 == 0):
#     print("this is a leap year")
# elif (yr%4 ==0) and (yr%100!= 0):
#     print("this is a leap year")
# else:
#     print("this is not a leap year")

# Corrected Ans 4 (accurate code, minor logical error)
# n = int(input("Enter the value of n: "))
# fac = 1
# if n == 0:
#     print("factorial of 0 in 1")
# elif n<0:
#     print("factorial does not exist")
# else:
#     for i in range(1,n+1):                            #need to put 'n+1' instead of 'n' as the for loop only runs till the value before the stop parameter
#         fac *= i                                      #changed 'fac = fac * i' to 'fac *= i'
#     print("factorial is ",int(fac))

# Incorrect Ans 5 (inaccurate code)
# inp = int(input("enter the input : "))
# inpo = inp
# for i in range(10,1000):
#     inp = inp/i
#     i = i*10
# if (str(inp) == str(inpo)):
#     print("the input is palindrome")
# else:
#     print("the input is not a palindrome")

# Corrected Ans 5:
# inp = input("Enter the input: ")
# is_palindrome = True
# for i in range(len(inp) // 2):
#     if inp[i] != inp[len(inp) - i - 1]:
#         is_palindrome = False
#         break
# if is_palindrome:
#     print("The input is a palindrome")
# else:
#     print("The input is not a palindrome")

# Corrected Ans 3
n = int(input("Enter a number: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    fib_seq = [0, 1]
    while fib_seq[-1] + fib_seq[-2] <= n:
        next_num = fib_seq[-1] + fib_seq[-2]            # [0,1] = 0 + 1 = 1, [1,1] = 1 + 1 = 2
        print(next_num, end=" ")                        # 1 , 2
        fib_seq[0], fib_seq[1] = fib_seq[1], next_num   # [0,1] = [1,1], [1,1] = [1,2]
    print()