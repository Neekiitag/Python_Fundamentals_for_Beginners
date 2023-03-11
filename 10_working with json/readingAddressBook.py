f = open("C://Course Work//Projects & Self Study//Code-Basics_Python//pythonProject//10_working with json//book.txt","r")
s = f.read()
# print(s)

import json

book = json.loads(s)
print(book)
print(type(book))
print(book["bob"])
print(book["bob"]["phone"])


#printing all the records from the disctionary - book
for person in book:
    print(book[person])