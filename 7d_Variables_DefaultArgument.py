def sum(a,b=0):
    print("This is a:", a)
    print("This is b:", b)

    total = a+b
    print("Sum calculated inside function is:", total)
    return total

n = sum(15)
print("Sum calculated outside the function is: ", n)

"""In main function, 
we have set argument b to zero, hence the function is still working even after we have not provided value for b.
These are called default arguments"""