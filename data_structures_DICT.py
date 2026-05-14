#  DICTIONARY :-
"""dictionary is a data structure which stores (key : value) pairs"""
d = {
    "one" : 1,
    "two" : 2,
    "three" : 3
    #key : value
}
"""dict doesnt have indexing, to access the el in dict we use (key)
        dict can store all type of data structure in itself"""

print(d["one"]) # 1
print(d["two"]) # 2

"""operations in dictionary"""
#1. looping in dictionary
for i in d:
    print(i) 
# this will access all the keys
    print(d[i])
# this will access all the values

#2. creating new el in dictionary 
d["four"] = 4
print(d)

#3. delete the el from the dict
del d["four"]
print(d)

#4. updation in dict 
d["one"] = 7
print(d)

"""methods in dictionary"""
