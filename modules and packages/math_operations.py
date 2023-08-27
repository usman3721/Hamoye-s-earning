# defining a add function to add its parameters
def add(x, y):
    return x + y

# defining a subtract function to subtract its parameters
def subtract(x, y):
    return x - y

# defining a multiply function to multiply its parameters
def multiply(x, y):
    return x * y

# defining a divide function to divide its parameters
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"