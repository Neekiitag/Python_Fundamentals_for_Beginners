"""Variables inside the defined function are called local variables,
variables calculated outside function are called global variables"""

total = 0

def sum(a,b):
    print("This is a:", a)
    print("This is b:", b)

    total = a+b
    print("Sum calculated inside function is:", a)
    """Here, total is a local variable, can be accessed only inside the function"""
    return total

n = sum(15, 25)
print("Sum calculated outside the function is: ", total)
"""Here, total is a global variable, initialised outside the function and can be accessed anywhere"""
