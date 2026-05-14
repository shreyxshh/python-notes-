# # basics in notes

# # return vs print
# # return is used to return some value from a function related to function values 
# def hello(): #function defination
#     return "how are you"

# a = hello() #function calling 
# print(a)


# def agecheck(n):
#     if n >= 18:
#         return True
#     else :
#         return False
    
# age = int(input("enter ur age : "))

# if agecheck(age):
#     print("you can vote")
# else:
#     print("u cant vote")

# def hello1():
#     hello2()
#     print("hello 1")

# def hello2():
#     hello3()

# def hello3():
#     hello4()
#     print("hello 3")

# def hello4():
#     print("hello 4")

# #flow of printing 
# #hello 4 -> hello 3 -> hello 2 -> hello 1
# hello1()


# # recursion and recursive calls

# # 1.printing number till 100
# def printNumber(n):
#     if n == 101:
#         return "done"
#     print(n)
#     printNumber(n+1)# we can increase the step which is taken in priting statement

# printNumber(1)

# def printnumberREV(n):
#     if n == 101:
#         return "done"
#     printnumberREV(n+1)
#     print(n)

# printnumberREV(1)


# def strongestNumber(n):
#     copy = n
#     sum = 0
#     fact = 1
#     while n > 0:
#         last = n % 10
#         for i in range(1, last+1):
#             fact = fact * i
#             sum = sum + fact 
#         n = n // 10    

def factorialN(n):
    if n == 1 or 0:
        return 1
    fact = 1
    for i in range(n , 0, -1):
        fact *= i

    return fact

print(factorialN(5))