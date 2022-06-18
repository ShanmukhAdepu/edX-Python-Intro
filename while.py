"""
1. Convert the following into code that uses a while loop

print 2
prints 4
prints 6
prints 8
prints 10
prints Goodbye!
"""

print("This is exercise 1: ")
n = 2
while n <= 10:
    print(n)
    n=n+2
print("Goodbye!")
print(" ")

"""
2. Convert the following into code that uses a while loop

print Hello!
prints 10
prints 8
prints 6
prints 4
prints 2
"""

print("This is exercise 2: ")
print("Hello!")
n = 10
while n > 0:
    print(n)
    n=n-2
print(" ")

"""
3. Write a while loop that sums the values 1 through end, inclusive. 
end is a variable that we define for you. 
So, for example, if we define end to be 6, your code should print out the result: 21
Which is 1+2+3+4+5+6
"""

print("This is exercise 3: ")
end = 6
start = 0
ans = 0
while start <= end:
    ans = ans + start
    start = start + 1
print(ans)
print(" ")