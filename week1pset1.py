"""
Problem 1
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print:
Number of vowels: 5
"""
print(" ")
print("This is problem 1: ")
s = "acdbobobegghakl"
count = 0
for i in s:
    if i == 'a':
        count = count + 1
    if i == 'e':
        count = count + 1
    if i == 'i':
        count = count + 1
    if i == 'o':
        count = count + 1
    if i == 'u':
        count = count + 1
print("Number of vowels: " + str(count))
print(" ")

"""
Problem 2
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print:
Number of times bob occurs is: 2
"""

print("this is problem 2:")
s = "azcbobobegghakl"
count = 0
for i in range(len(s)): 
    if s[i:i+3] == "bob": #s[start of split: end of split]
        count += 1
print("Number of times bob occurs is: " + str(count))
print(" ")

"""
Problem 3
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print:
Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc
"""
print("This is problem 3:")
s = "azcbobobegghakl"
longest = s[0] #tracks longest alphabetical order
current = s[0] #tracks current alphabetical order
for c in s[1:]: #goes through every letter starting at the second letter of s till the end
    if c >= current[-1]: #checks to see if the letter is after the previous letter
        current += c #if it is then it adds that letter to the substring
        if len(longest) < len(current): #if the current substring is longer then its the new longest
            longest = current
    else: #if the letter is not after the previous letter than it becomes the new starting letter of the substring current
        
        current = c
print("Longest substring in alphabetical order is: " + str(longest))
print(" ")


