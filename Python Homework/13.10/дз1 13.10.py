tax = int(23)
line = input()
cop = len(line) * tax
rub = int(cop / 100)
cop = cop - rub*100
print(rub ,"р.", cop, "коп.")