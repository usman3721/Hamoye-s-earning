# PART 1:Nested Control Structures
# 1.
# import random libary
import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)

# Initializing a variable to track whether the user has guessed correctly
guessed_correctly = False

while not guessed_correctly:
    # Prompt the user to guess the number
    user_guess = int(input("Guess the number between 1 and 10: "))
    
    # Compare the user's guess with the random number
    if user_guess == random_number:
        print("Congratulations! You guessed the correct number.")
        guessed_correctly = True
    elif user_guess < random_number:
        print("Too low!")
    else:
        print("Too high! ")
        
        
# 2.

# DEfining the number of lines/rows
rows = 5

for i in range(1, rows + 1): 
    num = i
    # Looping
    for j in range(i):
        print(num, end="")
        num += 1
    num -= 2
    for j in range(i - 1):
        print(num, end="")
        num -= 1
    print()



# # PART 2: Conditional Expressions
# # 1.

# Get user input for two integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Use a conditional expression to determine the maximum

if num1 > num2:
    print("The maximum value is:", num1)
else:
    print("The maximum value is:", num2)


# 2.

# Get user input for the percentage score
percentage = float(input("Enter the percentage score: "))

# calculates the grade for a student using if &else statemenr(conditional statement)
if percentage >= 90:
    print("Grade:A") 
elif percentage >= 80:
    print("Grade:B") 
elif percentage >= 70:
    print("Grade:C")
elif percentage >= 60:
    print("Grade:D")
else:
    print("Grade:F") 





# Part 3: Loop Patterns

# Get user input for the size of the diamond
size = int(input("Enter an odd number for the size of the diamond: "))



if size % 2 == 0:
    print("Size must be an odd number for a diamond to be formed.")
    print()

# Creating a for loop for the increment downward 
for i in range(1, size + 1, 2):
    spaces = (size - i) // 2
    print(" " * spaces + "*" * i)

# Creating another for loop for decrement after the increment loop has finished ikteration
for i in range(size - 2, 0, -2):
    spaces = (size - i) // 2
    print(" " * spaces + "*" * i)










