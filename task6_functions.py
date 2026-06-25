# Task 6: Functions

# Basic function
def greet(name):
    return f"Hello, {name}! Welcome to Python."

# Function with default parameter
def calculate_area(length, width=10):
    return length * width

# Function with multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)

# Recursive function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Lambda function
square = lambda x: x ** 2

# Main
print(greet("Donte"))
print("Area (5x10):", calculate_area(5))
print("Area (5x3):", calculate_area(5, 3))

numbers = [4, 17, 2, 99, 33, 8]
low, high = min_max(numbers)
print(f"Min: {low}, Max: {high}")

print("Factorial of 6:", factorial(6))
print("Square of 9:", square(9))
