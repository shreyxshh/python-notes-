#SETS:-
"""its a data type used to store unique value in it."""

#SETS PROPERTIES
""""
1. they are inordered (no indexing)
2. theyre semi mutable (can add but cant chnage and remove)
3. unique elements only (no duplicates)
4. heterogenous elements (can contains different data types)
"""

#initialization 
s = set()
s = {1,2,3,4,5}
print(s)
print(type(s))

#methods in sets 
""""
1. add()
2. update()
3. remove()
4. discard()
5. pop()
6. clear()
"""

#for single value addition
s.add(6)
print(s)

#for adding multiple values 
s.update([7,8,9])
print(s)

#to remove some value(value should always exist)
s.remove(8)
print(s)

# if we use discard on el which is not present it wont give any error
s.discard(10)
print(s)

#this removes smallest el from the set
s.pop()
print(s)

#this removes all values and returns a empty set
s.clear()
print(s)

#SET OPERATION
"""
1. intersection 
2. union
3. difference
4. symmetric difference
"""

s1 = {1,2,3,4}
s2 = {2,3,4,5}

#intersection = returns the value which are common in both sets
print(s1.intersection(s2))

#union = returns the unique values in set
print(s1.union(s2))

#difference = el in first set but not in second set
print(s2.difference(s1))

#sym diff = values which are not present in either sets
print(s1.symmetric_difference(s2))

#frozenset - this function doesnt let any changes in sets
s3 = {5,3,6,2,3}
frozenset(s3)
s3.add(43)
#this make the set static in nature
#default its dynamic 


