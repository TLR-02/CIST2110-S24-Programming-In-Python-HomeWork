# HW3.py
# Author:Tyler J. Criswell

# This Homework assignment is meant to test your ability to make functions within python as well as importing and using modules. This assignment might require you to do some research on your own. If you get stuck, try googling the problem, especially when it comes to importing and using the different modules.
# Hint you will want to enable word wrap in vscode (View -> Toggle Word Wrap) to make it easier to read the instructions.


# Question 1:
# Write a function that takes in a number and returns that number squared
# IE. If the user inputs 3, the function should return 9

number = int(input("Enter a number: "))

def square_number(number):
    """Squares a given number.
    Args:
        number: The number to be squared.
    Returns:
        The square of the input number.
    """
    return number ** 2


# Question 2:
# Write a function that takes in a string, a letter, and a number and returns the string with the letter replaced at the number index
# IE. If the user inputs "Hello World", "a", and 3, the function should return "Helao World
# Hint: You will want to use the replace() function

def replace_letter():
    """Gets a string, letter, and index from the user, and replaces the letter at the specified index."""
    string = input("Enter a string: ")
    letter = input("Enter a letter: ")
    index = int(input("Enter a number: "))
    return string[:index] + letter + string[index + 1:]

result = replace_letter()

print(result) 


# Question 3:
# Write a function that takes in a number, a lower_bound, and an upper_bound and returns whether the number is within the bounds
# IE. If the user inputs 5, 1, and 10, the function should return True

def within_bounds():
    """Gets a number, lower bound, and upper bound from the user, and checks if the number is within the bounds."""
    number = int(input("Enter a number: "))
    lower_bound = int(input("Enter a lower bound: "))
    upper_bound = int(input("Enter an upper bound: "))    
    is_within_bounds = number >= lower_bound and number <= upper_bound  # Calculate if the number is within the bounds

    if is_within_bounds:
        return "The number is within the bounds."
    else:
        return "The number is outside the bounds."

print(within_bounds())


# Question 4:
# # write a function with parameters for a name, age, and favorite color. Return the following string using the parameters:
# "Hello, my name is <name>. I am <age> years old. My favorite color is <color>.


def personal_info(name, age, color):
        """Creates a formatted string with personal information.
        Args:
            name: The person's name.
            age: The person's age.
            color: The person's favorite color.
        Returns:
            A formatted string containing the person's information.
        """
        return f"Hello, my name is {name}. I am {age} years old. My favorite color is {color}."


# Question 5:
# Write a function that asks the user for their name, age, and favorite color and then calls the function from question 4 using the user's input as the parameters.
# Hint: You will want to save the users input to variables and use them as the parameters for the function from question 4

def user_info():
    """Gets the user's name, age, and favorite color, and calls the personal_info function with the user's input."""
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    color = input("Enter your favorite color: ")
    return personal_info(name, age, color)

result = user_info() 

print(result) 

# Question 6:
# import the random module and use it to generate a random number between 1 and 100

import random

print(random.randint(1, 100))


# Question 7:
# import the math module and use it to find the square root of 16 (hint: use the sqrt() function)

import math

print(math.sqrt(16))


# Question 8:
# import the sys module and use it to print the version of python you are using
# this time import the module using the import "as" keyword
# hint: use the version attribute (sys.version)

import sys as s 

print(s.version)


# Question 9:
# import the os module and use it to print the current working directory. This time import the module using the from keyword
# hint: use the getcwd() function

import os 

print(os.getcwd())

