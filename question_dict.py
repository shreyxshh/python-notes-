d1 = {
    1 : 10, 
    2 : 20,
    3 : 30
}
d2 = {
    3 : 40,
    5 : 50,
    6 : 60
}

#question1 
"""inserting el of d2 in d1"""
# for i in d2:
#     d1[i] = d2[i]
# print(d1)

#question2
"""if same keys are present then add the values"""
for i in d2:
    if i in d1.keys():
        d1[i] = d1[i] + d2[i]
    else:
        d1[i] = d2[i]
#whenever "in" is used in code then a loop is running    
print(d1)

#question3
"""frequency counter"""

l = [1,1,1,1,1,1, 2,2,2,2,2, 3,3,3,3,3]
d = {}

for i in l:
    if i in d.keys():
        #if exist then increase the frequency
        d[i] += 1
    else:
        #if el doesnt exist then create the (key : value)
        d[i] = 1
print(d)