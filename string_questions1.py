# question1
s = "ShreyasH"
print(s)
print(f"length of string is -> {s.len()}")#string length
print(f"string in uppper case is -> {s.upper()}")#string uppercase
print(f"string in lower case is ->{s.lower()}")#string lower case

#string reversing 
#in slicing stop value always goes upto length-1 
print(s[::-1])#this is used to reverse the string in short form

# question2
s = "SHREYash"
lower = ""
upper = ""
# '.is' is a identity operator used to check to operand identity when used 
for i in s:
    #lower case
    if i.islower():
        lower = lower+i
    # upper case
    elif i.isupper():
        upper = upper+i
    
print(lower+upper)
        
# question3
s = "P@#yn@^at&i5ve"
digit = 0
alpha = 0
spec = 0
for i in s:
    if i.isalpha():
        alpha += 1
    elif i.isdigit():
        digit += 1
    else:
        spec += 1

print(f"the count of digits, alphabets and special char are in string are {digit}, {alpha} and {spec}")

# question4
s1 = "Rawat"
s2 = "rawat"
if len(s1) != len(s1):
    print("not equal")
else:
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            print("string are not same")
            break
    #printing are same at last cause itll make the number of operation lesser 
    else:
        print("string are same")

#question5
str1 = "ubfuqewbfuqewbf"
count = 0 
for i in str1:
    if i in "aeiouAEIOU":#using this string to check if vowels exist in the string
        count += 1

print(f"the count of vowels in string is {count}")

# question6
def countVowel():
    str1 = "ubfuqewbfuqewbf"
    count = 0 
    for i in str1:
        if i in "aeiouAEIOU":#using this string to check if vowels exist in the string
            count += 1

    return f"the count of vowels are : {count}"
print(countVowel())

# question7

# using loops 
str1 = "shreyash"
rev = ""#for storing the reverse string 
for i in str1[::-1]:
    rev = rev+i

print(rev)
# question8 
# using two pointer
s = "781187"
i, j = 0, len(s)-1
while i<=j :
    if s[i] == s[j]:
        i+=1
        j-=1
    else:
        print("not a palindrome")
print("is a palindrome")

# question8 
s = "madam"
rev = s[::-1]
if s == rev:
    print("is palindrome")
else:
    print("not a palindrome")

def checkPalindrome(str):
    rev = str[::-1]
    if str == rev:
        print("palindrome")
    else:
        print("not a palindrome")

s = input("enter a string : ")
checkPalindrome(s)

def countVowelsAndConsonents(str1):
    vowels = 0
    const = 0
    for i in str1:
        if i in "aeiouAEIOU":
            vowels+=1
        else:
            const+=1

    return f"the count of vowels and consonents in string are {vowels} and {const}!"

print(countVowelsAndConsonents("uibewfbqweiew"))

def count_vowels_and_consonants(s):
    vowels = set("aeiouAEIOU")
    vowel_count = sum(1 for ch in s if ch.isalpha() and ch in vowels)
    consonant_count = sum(1 for ch in s if ch.isalpha() and ch not in vowels)
    return f"The count of vowels and consonants in string are {vowel_count} and {consonant_count}!"

print(count_vowels_and_consonants("uibewfbqweiew"))
