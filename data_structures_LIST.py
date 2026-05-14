#LIST 
"""used to store large amount of values in same container"""

#to create a list we use sqaure bracket"[]""
l = [1,2,3,4,5]

"""special characterstics of lists:- """

# 1. heterogeneous nature
"""it can multiple type of data in a single type of list"""
l1 = [False, "shreyash", 12, 12.532, print()]

# 2. always in order
"""the list always in a specific order which is increasing order by default, each element in the has a
    designated position in the list which allow easy traversal and operations"""
"""its indexed toooo"""

# 3. mutatability 
"""list canbe changed in anytime in the program whcih means any value in the llist canbe deleted, changed ,
        exchanged etc which allows multiple usecase in programming"""

# 4. duplicates in a list 
"""list can store duplicate value in a list"""

#BASICS OPERATIONS ON LIST

"""reading a list"""
l2 = [1,2,3,4,5]
print(l2)
print(l2[3], l2[-2])

"""updating a list"""
l3 = [1,2,3,4,5]
print(l3)
l3[4] = 7
print(l3)

"""deleting elements from a list"""
l4 = [1,2,3,4,5]
print(l4)
del l4[2] #'del' used to delete anyything store in RAM 
print(l4)

"""looping on list"""
l5 = [1,2,3,4,5]

#based on values 
for i in l5:
    print(i)
"""here all the values will be accessed one by one"""

#based on index
for i in range(len(l5)):
    print(l5[i])
'''here values and indices canbe accessed,it also gives more control over your list'''

#METHODS FOR LIST:-
l6 = [1,2,3,4,5]

# #1. creation of new element in list
""".append(value) used to add new value at the last of the list
    bcz default value to add is (-1)"""
l6.append(6)
l6.append([7,8,9])

# 2. to insert a value in between the list 
""".insert(index of place to be inserted, value to insert)"""
l6.insert(2, 34789)
print(l6)

#3. to empty the whole list
""".clear() to empty the whole list"""
l6.clear()

#4. to remove from specific index from the list
""".pop(index to be remove), by default its value is set to (-1)
        it also return the same item which is removed from list 
            this canbe sometimes usedful"""
l6.pop(3)

#5. to remove a specific value
'''.remove(value to to removed), it also return the value which is removed'''
l6.remove(5)

#LIST SORTING :-

l7 = [1,2,67,34,89,2345,4,57,8]
#bubble sort in python
"""in this we intent to put the largest number in the list at the end
        comparing two elements with wach other aand swapping larger with smaller"""


"""bubble sort in python"""

#intuition behind the algo is to just swap the larger el with smaller el at the end of the list
for j in range(len(l7)-1):
#outer loop is just running the n-1 times 
    for i in range(len(l7)-1):    
        #inner loop in actually doing the comparisons and sorting the list
        if l7[i] > l7[i+1]:
            l7[i], l7[i+1] = l7[i+1], l7[i]
            
print(l7)