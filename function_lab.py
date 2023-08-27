# Part 1: Function Definition and Invocation:

# defining the function
def Calculate_average(num1,num2):
    average=(float(num1)+float(num2))/2
    return average

# Prompting the user for parameter
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Storing the resukt in a Variable
result = Calculate_average(num1, num2)
# printing out the result
print("The average is:", result)


# Part 2: Return Values and Variable Assignment: 

def Max_num(num1,num2,num3):
    max_num=max(num1,num2,num3)
    return max_num

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the second number: ")

max=Max_num(num1,num2,num3)
print("The maximum number:", max)


# Part 3: Multiple Functions: 

# defining Calculate factorila function
def calculate_factorial(num):
    # conditiinal statement
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, num + 1):
            factorial *= i
        return factorial

# prompting the user
number = int(input("Enter a number: "))
# storing the resukt in a variable
fac= calculate_factorial(number)
# printing thr result
print("Factorial of", number, "is:", fac)


# defining Calculate power function
def calculate_power(base,exponent):
   power=base**exponent
   return power

# prompting the user
base= int(input("Enter the base number: "))
exponent= int(input("Enter the exponent: "))

# storing the resukt in a variable
pow= calculate_power(base=base,exponent=exponent)

# printing thr result
print("power is:", pow)



# Part 4: Recursion:
# Defining a function the calcualte fibonacci nth term
def calculate_fibonacci(n):
    # conditiional statement
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)

# prompting user
prompt= int(input("Enter a positive integer: "))
# Stoing the answee in a variable
fibonacci = calculate_fibonacci(prompt)
# printing the nth term of a fibonacci
print("The", prompt, "th Fibonacci number is:", fibonacci)



# Part 5:

# importing math module
import math
def is_prime(num):
    if num <= 1:
        return False
    # Loop to check if num is divisible by any number from 2 up to its square root
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Loop to check prime numbers in the range 1 to 100
for number in range(1, 101):
    if is_prime(number):
        print(number, "is prime")


