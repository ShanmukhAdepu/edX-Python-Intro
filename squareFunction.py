"""
Write a Python function, square, that takes in one number and returns the square of that number.

This function takes in one number and returns one number.
"""
def square(x):
    
    return x**2
    
user_input = input("Please give me a number to square: ")




print("The square of " + str(user_input) + " is " + str(square(user_input)))