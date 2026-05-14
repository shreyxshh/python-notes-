#File handling:-

# #to open a file from being on its path 
# """to open a file"""
# file = open('string_question.py')

# """it reads the file"""
# print(file.read())

# """we have to close the file manually"""
# file.close

# #to open a file which is not in path
# file1 = open(r"C:\Users\SHREYASH\vs codes files\cpp\dsa.exe")

#using r in open to opne that it in raw mode 


"""
there are 4 modes of file handling
1. w - write mode : if file already exist it will overwrite the file texts 
        else it will create the file for the name 
2. a - append mode : add the content at the end of the file
3. r - read mode: this reads the content inside the file 
4. x create mode:
"""

#1. write mode
file = open('gangadhar.txt', 'w')
file.write('this is gangadhar fiie.')
file.close()

#2. append mode
file = open('gangadhar.txt', 'a')
file.write('this is added using (append) mode.')
file.close()

#. read mode
file = open('gangadhar.txt', 'r')
print(file.read())
file.close()

"""we can also use a for loop in this file"""
file = open('gangadhar.txt', 'r')
for i in file:
    print(i)
file.close()

#4. create mode

#using "with" statement : this auto closes the file 

with open('gangadhar.txt', 'r') as file:
    print(file.read())

with open('gangadhar.txt', 'w') as file:
    file.write('content overwritten')
    print("done")

#PATHS
#this get the path we are in and searches if the file exists there or not 
#since we're on the correct path we can just enter the file name to be found
from pathlib import path
p = path('gangadhar.txt')
if p.exists():
    print("exist")
else:
    print("doesnt exist")