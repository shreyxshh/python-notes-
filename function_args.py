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
a

def add(*a):
    print(a)
add(1,2,3,4,5,6)

'''
args is a tuple type of data type which stores a large number data in single variable 
'''