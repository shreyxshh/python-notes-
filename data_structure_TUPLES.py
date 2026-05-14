#TUPLES
"""
1. Tuples are ordered(indexing are possible)
2. can have duplicates
3. are heterogenous
4. are immutable 
"""
#we can store mutliple values in var but its type will be "tuples" not that of data type stored 

#t = () empty tuple
t = (10,20,30,40,50)
print(t)

#direct loop 
for i in t:
    print(i)

#index loop
for i in range(len(t)):
    print(i, t[i])

#to access both values and indexes at same time
for index, value in enumerate(t):
    print(index, value)

#enumarate will not work in dictionary

#tuple slicing
print(t[1:4])
#t[start: stop : step]

# "in" is calles membership operator which checks for a value in something

"""tuple methods
1. count() -> count the occurance of el
2. index() -> returns the index value of the first occurance
3.  
"""
#tuple unpacking and packing

#this is called unpacking
t1 = (1,2,3,4,5)
a,b,c,d,e = t1
#this store the individual value in tuple into the following variables 
"""during unpacking the amt of var should be same as el in tuples"""
print(a,b,c,d,e)

#this is  called packing 
t2 = 1,2,3,4,5
print(t2)

#star expression(*):-
t3 = (1,2,3,4,5)
a, *b, c = t3
"""first value will get in a and rest value will collectivety go in b
    c will get the last value and rest will save in b"""
print(a,b,c)

#tuple concatination
t4 = (1,2,3)
t5 = (4,5,6)
print(t4+t5)