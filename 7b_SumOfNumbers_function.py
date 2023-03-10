"""Two types of arguments used in a function:
1. Named Arguments
2. Positional Arguments"""

def sum(a,b):
    total = a+b
    return total

"""Positional Arguments"""
x = sum(5,6)
print("Sum is :", x)

"""Named Arguments"""
y = sum(b=14, a=2)
print("Sum is :", y)