x = input("Enter number 1: ")
y = input("Enter number 2: ")

try:
    z = x / int(y)
except Exception as e:
    print("Exception has occurred: ", e)
    z = None

print("Divison of numbers is: ",z)

