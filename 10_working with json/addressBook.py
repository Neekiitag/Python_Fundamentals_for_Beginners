book = {}
book["tom"] = {
    'name' : 'tom',
    'address' : '123 Stuart Ave, Norwalk, CT',
    'phone' : '7894561230'
}

book["bob"] = {
    'name' : 'bob',
    'address' : '100 Calumet St, Boston, MA',
    'phone' : '7015975320'
}

import json
s = json.dumps(book)
print(s)
with open("C://Course Work//Projects & Self Study//Code-Basics_Python//pythonProject//10_working with json//book.txt","w") as f:
    f.write(s)