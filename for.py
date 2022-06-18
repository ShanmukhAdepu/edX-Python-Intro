"""
1. Convert the following into code that uses a for loop

print 2
prints 4
prints 6
prints 8
prints 10
prints Goodbye!
"""
print(" ")
print("This is exercise 1: ")
for n in range(2, 12, 2): #range(start, stop, increment value)
    print(n)
print("Goodbye!")
print(" ")

"""
2. Convert the following into code that uses a for loop

print Hello!
prints 10
prints 8
prints 6
prints 4
prints 2
"""

print("This is exercise 2: ")
print("Hello!")
for n in range(10, 0, -2):
    print (n)
print(" ")

"""
3. Write a for loop that sums the values 1 through end, inclusive. 
end is a variable that we define for you. 
So, for example, if we define end to be 6, your code should print out the result: 21
Which is 1+2+3+4+5+6
"""

print("This is exercise 3: ")
end = 6
ans = 0
for n in range(0, end+1, 1):
    ans = ans + n
print(ans)
print(" ")