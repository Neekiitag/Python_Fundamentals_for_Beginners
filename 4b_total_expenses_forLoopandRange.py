expenses = [3000.32,2936,3511,3620,2600,2987]
total = 0
for i in range(len(expenses)):
    print("Month",(i+1),"expenses are: ",expenses[i])
    total = total + expenses[i]
print("My total expenses half yearly are: ", total)


