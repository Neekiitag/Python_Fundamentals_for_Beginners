x = input("Enter number 1: ")
y = input("Enter number 2: ")
"""
try:
    z = x / int(y)
except Exception as e:
    print("Exception type: ", type(e).__name__)
    z = None

print("Divison of numbers is: ", z)
"""

try:
    z = x / int(y)
except TypeError as e:
    print("TypeError Exception")
    z = None

print("Divison of numbers is: ", z)
