'''
during initialization of any function if we dont know the no of parameters to be passed 
solution -> use args

notation to create a args - (*variable_name)
example:-
args -> *shreyash
args canbe used to take various inputs at a time and pass large no of parameters to function directly 
args variable name canbe anything.
'''

def a(*a):
    print(type(a))
a(1,2,3,4)

def add(*a):
    print(a)
add(1,2,3,4,5,6)

'''
args is a tuple type of datatype which stores a large number data in single variable 
args takes value in the form of tuples 
if args is tuple its canbe looped
'''

def args_looping(*chacha):
    for i in chacha:
        print(i)

args_looping(1,2,3,4,5)

#keyword arguments 
def polio(name, age, pin, contact):
    print(name, age, pin, contact)
polio(name = "shreyash", age = 13, pin = 1323, contact = 3452345)

"""
if user give a extra paramters to be added and the function doesnt have 
the input capacity we can use (kwargs)
this excepts arguements in the form of dictionary and initialize the missing variable if its passed 
"""

'''
notation to write kwargs -> (**variable_name)
parameters = keys , arguments = values 
we can also loop in kwargs 
'''

"""if we are sure about the arguements passing we can used (kwargs) 
else we can go with (args)
"""
def polio1(**var):
    print(type(var))
    print(var)
    for i in var:
        print(f"parameters -> {i}, arguements -> {a[i]}")
polio1(name = "shreyash", age = 20, school = "xaviers")

#lambda fucntion -> one liner fucntion 
# 1. normal method
def showVar(a,b):
    print(a,b)
showVar(1,2)

# 2. lambsa method
'''lambda changes the variable into a function using 
if both the parameters get a value then only the lambda function works 
otherwise no output
'''
showAdd = lambda a,b: a+b
print(showAdd(12,65))