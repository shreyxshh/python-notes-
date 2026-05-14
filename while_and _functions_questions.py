# #question1
# #first method
# num = int(input("enter a number : "))

# dig = 0
# while n > 0:
    
#     dig += 1
#     n = n // 10

# print("the count of dig in the number is :", dig)

# # #alternative method
# n = input("enter a number : ")
# print(len(n))

# def countDig(n):

#     dig = 0
#     while n > 0:
    
#         dig += 1
#         n = n // 10
# #this is used to make the divided number in whole number form (n/10) will make the n in floating form

#     return ("the count of dig in the number is :", dig)

# num1 = int(input("enter a number : "))
# print(countDig(num1))
# """if "return" is used then the function acts as a smol variable 
#         and output is to printed it has to be printed explicitly""" 

# #question2
# """print the sum of digits in a number"""
# n = int(input("enter a number : "))
# sum = 0
# while n > 0:
#     dig = n % 10
#     sum += dig
#     n = n // 10

# print(f"the sum of number is {sum}")



# """this is known as function notation and its used to specify the 
#         type of parameters which is to inputed in the fucntion """
# def numberSum(n: int):

#     sum = 0
#     while n > 0:
#         dig = n % 10
#         sum += dig
#         n = n // 10

#     return(f"the sum of number is {sum}")

#question3
"""check if number is armstrong or not"""

def check_armstrong(num: int):
    copy = num 
    sum = 0
    while num > 0:
        dig = n % 10
        power = dig ** 3
        sum += power 
    if copy == sum:
        return f"the {copy} is an armstrong number!"
    else:
        return f"the {copy} is not an armstrong number"

n = int(input("enter a number : "))
print(check_armstrong(n))

def factorialN(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def check_strong_number(num):
    copy = num
    strong = 0
    while num > 0:
        dig = num % 10
        fact = factorialN(dig)
        strong += fact
        num = num // 10

    if strong == copy:
        return (f"{copy} is a strong number!")
    else:
        return (f"{copy} is not a strong number!")

print(check_strong_number(145))
