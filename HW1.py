# HW1.py
# Author: Tyler J. Criswell         


# Question 1:
# Print Hello World like we did in class
print("Hello World")


# Question 2:
# Print the following:


# Your name
print("Tyler Criswell")


# Your age
print("22")


# Your favorite color
print("Blue")


# Your favorite animal
print("Capybara")


# Question 3:
# Create a variable called "myName" and set it equal to your name
myName = "Tyler Criswell"   


# Create a variable called "myAge" and set it equal to your age
myAge = "22" 


# Create a variable called "myColor" and set it equal to your favorite color
myColor = "Blue"


# Create a variable called "myAnimal" and set it equal to your favorite animal
myAnimal = "Capybara"


# Print the following:
# Hello, my name is <myName>
print("Hello, my name is", myName)


# I am <myAge> years old
print("I am", myAge, "years old")


# My favorite color is <myColor>
print("My favorite color is", myColor)


# My favorite animal is <myAnimal>
print("My favorite animal is a", myAnimal)


# Question 4:
# Calculate the following and print the result:

# 2 + 2
print(2 + 2)


# 3 * 4
print(3 * 4)


# 5 - 6
print(5 - 6)


# 8 / 2
print(8 / 2)


# Question 5:
# Create a variable called "num1" and set it equal to 2
num1 = 2 


# Create a variable called "num2" and set it equal to 3
num2 = 3 


# Create a variable called "num3" and set it equal to 4
num3 = 4 


# Create a variable called "num4" and set it equal to 5
num4 = 5 


# Calculate the following and print the result:
# num1 + num2
print(num1 + num2)


# num3 * num4
print(num3 * num4)


# num4 - num1
print(num4 - num1)


# num2 / num1
print(num2 / num1)


# Question 6: Write a program that asks the user for their name and then prints the following:
name = input("Hello, Please enter your name: ")


print("Hello,", name, ". Please enter three numbers.")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))


# 1. The sum of the three numbers is <sum>
sum = num1 + num2 + num3
print("The sum of the three numbers is", sum)


# 2. The product of the three numbers is <product>
product = num1 * num2 * num3
print("The product of the three numbers is", product)


# 3. round the three numbers to the nearest integer and print the sum of the three rounded numbers divided by 3
rounded_sum = round(num1) + round(num2) + round(num3)
rounded_average = rounded_sum / 3  
print("The sum of the three rounded numbers divided by 3 is", rounded_average)


# 4. The average of the three numbers is <average>
average = (num1 + num2 + num3) / 3 
print("The average of the three numbers is", average) 


# Question 7: Ask the user for an input of a symbol (in the example its *)
# Print a diamond of the symbol that looks like the following. Include the spaces and the | character.
# Hint: the print("symbol", end="") with \t and \n characters will be useful here.

#    *     |
#   ***    |
#  *****   |
# *******  |
#  *****   |
#   ***    |
#    *     |

symbol = input("Please enter a symbol: ")
print("   ", symbol, "    |")
print("  ", symbol * 3, "   |")
print(" ", symbol * 5, "  |")
print(symbol * 9, "|")
print(" ", symbol * 5, "  |")
print("  ", symbol * 3, "   |")
print("   ", symbol, "    |")