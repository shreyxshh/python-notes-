# #LIST QUESTIONS

# #question1
# a = int(input("enter number of element wanted : "))
# l1 = []
# for i in range(0, a):
#     z = int((input("enter number : ")))
#     l1.append(z)    

# print(l1)
# #alternative method
# l2 = eval(input("enter ur string : "))
# print(l2)

# #question2
# l3 = [1,2,3,4,5]

# # #method 1: slicing
# # print(l3[::-1])

# # # #mwthod 2 : using for loop
# rev = []
# """using negative stepping"""
# for i in range(len(l3)-1, -1, -1):#stepping is negative in this loop 
#     rev.append(l3[i])
# print(rev)

# #method 3 : using two pointer 
# i , j = 0 , len(l3)-1
# while i<j:
# # """to swap two values in python we can use (a,b = b,a)"""
#     l3[i], l3[j] = l3[j], l3[i]
#     i += 1
#     j -= 1
    
# print(l3)

# #method 4 : using for loop 
# z = len(l3)-1
# for i in range(len(l3)//2):
#     l3[i], l3[z] = l3[z], l3[i]
#     z -= 1
# """looping the list till mid of it and using another pointer to 
#     iterate the list from the back and swapping the values 
#         using ("a,b = b,a")"""

# #question3
# l4 = [-1, 4, -4, 5, 2, -89]
# print("printing all postive values")
# for i in l4:
#     if i >= 0:
#         print(i)

# print("printing all the negative values")
# for i in l4:
#     if i < 0:
#         print(i)

# #question4
# """sorting without using .sort(), using bubble sort"""
# l7 = [1,2,67,34,89,2345,4,57,8]
# for j in range(len(l7)-1):
#     for i in range(len(l7)-1):
#         if l7[i] > l7[i+1]:
#             l7[i], l7[i+1] = l7[i+1], l7[i]
            
# print(l7)

# #question5
# l8 = [1,7,63,46,348,83,92,53,73]
# large, idx = 0, 0
# for i in range(len(l8)):
#     if large < l8[i]:
#         large = l8[i]
#         idx = i

# print(f"the largest element in the list is {large} and its index is {idx}")

#question6
"""in previous question find the first and second largest number"""

#using if else:
# l8 = [1,7,63,46,348,83,92,53,73]
# largest, secLar = l8[0], l8[0]
# idx1, idx2 = 0, 0
# for i in range(len(l8)):
#     '''finding the largest in list'''
#     if largest < l8[i]:
#         largest = l8[i] 
#         idx1 = i
#     elif l8[i] > secLar and l8[i] != largest:
#         secLar = l8[i]
#         idx2 = i


# print(f"the largest element in list is {largest} with index {idx1}!")
# print(f"second largest element in list is {secLar} with index {idx2}!")

#using .pop function to delete the largest value

#using swappings
'''for indices run the loop on index'''
# max = l8[0]
# sec_max = l8[0]
# for i in l8:
    
#     if i > max:
#         sec_max = max
#         max = i

#     elif i > sec_max and sec_max != max:
#         sec_max = i

# print(max)
# print(sec_max)

#question7
# l = [1,46,63,348,83,7, 92,53,73]    
# smallest = float('inf')
# secSlt = float('inf')
# idx1 , idx2 = 0 , 0
# for i in range(0, len(l)):
#     if l[i] < smallest:
#         smallest = l[i]
#         idx1 = i
#     elif l[i] < secSlt and l[i] != smallest:
#         secSlt = l[i]
#         idx2 = i

# print(smallest, secSlt)
# print(idx1, idx2)

"""for finding largest -> use """

#question8 
"""checking if list is sorted or not"""

# l9 = [1,2,3,4,5,8,7]
# for i in range(0, len(l9)-1):
#     if l9[i] > l9[i+1]:
#         print("the list not sorted")
#         break
# else:#this is used at outer indent cause it will be executed multiple times if written in
#         print("the list is sorted")



#question9 
"""list palindrome"""

# a = [2,3,15,3,2]
# i = 0
# j = len(a)-1
# while i<j:
#     if a[i] != a[j]:
#         print("not a palindrome") 
#         break
    
#     i += 1
#     j -= 1    
# else:
#     print("palindrome ")

# #alternative method -> using for loop 

# for i in range(len(a)//2):
#     if a[i] != a[len(a)-1-i]:
#         print("not a palindrome")
# else:
#     print("palindrome")

# a = 0
# b = []
# n = int(input("enter the number of elements : "))
# for i in range(n):
#     el = int(input("enter number : "))
#     b.append(el)
#     a += el

# print(a)
# print(b)

# lst = list(map(int, input("enter number : ").split()))
# print(lst)

"""
.map(data_type, input)
.split() -> seperates all the values and digits
list() -> converts the value in list

sabse pehle inputs accpets -> har input split hoga -> inputs will be type casted in the form of int -> we store
all the int values inside a list
"""

# #question10 
"""rotate list by 'k' """
# l = [1,2,3,4,5,6,7,8,9] # k = 2
# k = 12
# """for large value of k"""
# k = k % len(l) 
# for i in range(k):
#     last = l[-1]
#     for j in range(len(l)-1,0 ,-1):
#         l[j] = l[j-1]
        
#     l[0] = last
# print(l)
#alterenative method

# i = 0
# j = len(l)-1
# last = l[-1]
# while i < k:
#     l[j] = l[j-1]
# l[0] = last 

# print(l)

#question11 
"""put all the zeroes at the end"""

#using two pointers
# r = [0,1,0,3,6]
# i, j = 0, len(r)-1 
# count = 0 
# while i<j:
#     if r[i] == 0:
#         r[i], r[j] = r[j], r[i]
#         #swapped the last el to zero el
#         i += 1
#         j -= 1
#         count += 1
#     else:
#         i += 1
# print(r, count)
"""only moving the i pointer as it will cover the whole list and j will point at the last
    whenever i == 0 then swapping is done and j is decresed"""
#counts the number of zeroes in list 


#alternative method - this is also two pointer but different (using for loop)
# j = 0
# for i in range(len(r)):
#     if r[i] != 0:
#         r[i], r[j] = r[j] , r[i]
#         j += 1
# print(r)
