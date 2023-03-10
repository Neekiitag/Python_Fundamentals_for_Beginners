def calculate_total(exp):
    total = 0
    for item in exp:
        total = total + item
    return total

nik_exp = [1200,1000,1500,856,1490,1059]
nik_total_exp = calculate_total(nik_exp)
print("The half yearly expenses of Nik are: ", nik_total_exp)

jack_exp = [3000,3250,2960,3590,3420,2990]
jack_total_exp = calculate_total(jack_exp)
print("The half yearly expenses of Jack are: ", jack_total_exp)


