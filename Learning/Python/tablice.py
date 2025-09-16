#stworzenie tablicy
owoce=[]

#dodanie 5 owoców
for x in range(1,6):
    x=input("podaj owoc")
    owoce.append(x)
print(owoce)

#wyświetlenie 1,3 i -2 elementu
print(owoce[1],owoce[3],owoce[-2])

#usunięcie 2 elementu
owoce.remove(owoce[2])
print(owoce)

#podanie numeru elementu jabłka
if("jabłko" in owoce):
    print(owoce.index("jabłko"))
else:
    print("w tablicy nie ma jabłka")