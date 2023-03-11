"""
List: All value shave similar meaning. they are homogeneous in nature
    eg: Expense list, salaries, List of people
Tuples: All values have different meaning. they are heterogeneous. They are immutable
    eg: x co-ordinate and y co-ordinate, address
"""


thistuple = ("apple", "banana", "cherry", "kiwi", "orange")
print(thistuple)

thislist = ["apple", "banana", "cherry"]
print(thislist)

#changing tuple values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Creating a new tuple with the value "orange", and adding that to tuple:
xtuple = ("apple", "banana", "cherry")
a = ("orange",)
xtuple += a

print(xtuple)

#Convert the tuple into a list, remove "apple", and convert it back into a tuple:
ytuple = ("apple", "banana", "cherry")
print("Tuple before removing any item: ", ytuple)
b = list(ytuple)
b.remove("apple")
ytuple = tuple(b)
print ("This is the updated tuple:", ytuple)

#The del keyword can delete the tuple completely:
ztuple = ("apple", "banana", "cherry")
print("Tuple to be deleted: ", ztuple)
del ztuple
print("Tuple is deleted")

#this will raise an error because the tuple no longer exists


