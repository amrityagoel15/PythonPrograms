# Single-line comment: This prints Hello World
print("Hello, World!")  # Inline comment after code

# -----------------------------
# Multi-line comments using #
# Each line starts with #
# -----------------------------
x = 10
y = 20
# Adding two numbers
sum_xy = x + y
print("Sum =", sum_xy)

"""
Multi-line comment using triple quotes
This can also act as a docstring if placed inside a function, class, or module.
Here we are just using it as a block comment.
"""
product = x * y
print("Product =", product)

# Function with a docstring
def greet(name):
    """This function greets the person passed as a parameter."""
    return f"Hello, {name}!"

print(greet("Mehak"))
print("This program is written and excecuted by MEHAK BHUTANI with ERP 0231BCA063")
