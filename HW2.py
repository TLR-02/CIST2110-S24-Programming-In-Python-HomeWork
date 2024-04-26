# HW2.py

# Author:Tyler J. Criswell     


# Question 1:

# Write some code that prompts the user for their age. Depending on the input:

# If the age is less than 13, print "You are a child."

# If the age is between 13 and 19, print "You are a teenager."

# If the age is 20 or older, print "You are an adult."

input_age = int(input("Enter your age: "))

if input_age < 13:

        print("You are a child.")

elif input_age >= 13 and input_age <= 19:

        print("You are a teenager.")

else:

    print("You are an adult.")
    

# Question 2:

# Write some code to display the following pattern using a for or while loop:

# 1

# 12

# 123

# 1234

# 12345

for i in range(1, 6):

    for j in range(1, i + 1):

        print(j, end="")

        print(

            end=""

        )

    print()
    

# Question 3:

# Write some code that prompts the user to input 10 numbers. After all the numbers are inputted, the program should display:

# The highest number.

# The lowest number.

# The average of all the numbers.

# Hint 1: You will need to use a for loop and a counter variable to keep track of the total sum of the numbers.

# Hint 2: You will need to use an if statement to keep track of the highest and lowest numbers.

print("Enter 10 numbers: ")

numbers = []

highest = float('-inf')

lowest = float('inf')

total = 0

for i in range(10):
 
    number = int(input())
      
    numbers.append(number)
    
    total += number  
    
    if number > highest:
        
        highest = number
        
    if number < lowest:
        
        lowest = number

average = total / len(numbers)

print("Highest number:", highest)

print("Lowest number:", lowest)

print("Average:", average)

    
# Question 4:

# Vowel Counter - Write some code that prompts the user to enter a string. The program should then display the number of vowels in the string. IE. If the user enters "Hello World", the program should display 3.

# the vowels are a, e, i, o, u

# Hint: convert the string to lowercase and use a for loop with a counter variable and an if statement

print("Enter a string: ")

string = input().lower()

vowels = 0

for i in string:

    if i in "aeiou":

        vowels += 1

        print(vowels)