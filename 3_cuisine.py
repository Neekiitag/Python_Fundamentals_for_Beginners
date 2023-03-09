# write a program that asks user to enter the dish name and it should print which cuisine is that dish ?

indian = ["CholeyBhature","Dosa","PuranPoli","PaniPuri"]
italian = ["Pizza","Pasta","Spaghetti"]
mexican = ["Quesadilla", "Burrito", "Fajitas", "Tacos", "GuacAndChips"]

dish = input("Please enter the dish name: ")

if dish in indian:
    print("This is a Indian Cuisine")
elif dish in italian:
    print("This is a Italian Cuisine")
elif dish in mexican:
    print("This is a Mexican Cuisine")
else:
    print("Based on my knowledge, I am not sure which cuisine is", dish)