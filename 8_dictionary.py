"""Telephone Dictionary, order of key-value pairs doesn't matter"""

d = {"Tom" : 7894561230, "Jerry" : 3216549870 , "Popoye" : 1597534682}               #defining the dictionary
print(d)                                                                             #Displaying the elements of the dictionary
print(d["Jerry"])                                                                    #Displaying one element from the dictionary
d["Bob"] = 648219735                                                                 #Adding an element to the dictionary
print(d)                                                                             #Displaying the elements of the dictionary

d["Sam"] = 648987935
d["Joe"] = 648219322
print(d)

del d["Popoye"]
print(d)

for key in d:
    print("Key is:", key, "& Value is:", d[key])

for k,v in d.items():
    print("key:", k, "Value:", v)

d.clear()
print("Values in Dictionary are vanished.", d)