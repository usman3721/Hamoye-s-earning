# importing modules
from math_operations import add,subtract,multiply,divide
from my_package import string_operations

# prompting user
# num1 = int(input("Enter the first integer: "))
# num2 = int(input("Enter the second integer: "))

# # creating adddition object
# addition=add(num1,num2)
# print("Addtion =" ,addition)

# # creating subtraction object
# subtraction=subtract(num1,num2)
# print("Subtraction =",subtraction)

# # creating multiplication object
# multiplication=multiply(num1,num2)
# print("Multiplication =",multiplication)

# # creating division object
# division=divide(num1,num2)
# print("Division =",division)


# prompting user for string
string_prompt= input("Enter a string: ")
# calling the reverse from string_operation module
reversed_letter=string_operation.reverse(string_prompt)
# printing out the reversed string
print("Reversed string:", reversed_letter)


# prompting user for string
string_prompt= input("Enter a string: ")
# calling the count_vowel from string_operation module
nun_vowels=string_operation.count_vowel(string_prompt)
# printing out the number of vowels
print("Number of vowels:", num_vowels)

