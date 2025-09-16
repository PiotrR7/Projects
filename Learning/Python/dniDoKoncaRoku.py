dzien=int(input('podaj dzisiejszy dzien: '))
miesiac=int(input('podaj obecny miesiac: '))

miesiace=[1,2,3,4,5,6,7,8,9,10,11,12]
dniwmiesiacu=[31,28,30,31,30,31,30,31,30,31,30,31]
minieteMiesiace=[]

for x in miesiace:
    miesiace=dniwmiesiacu

for y in range(1,miesiac):
    y=minieteMiesiace.append(y)

for a in range(0,len(minieteMiesiace)):
    minieteMiesiace[a]=dniwmiesiacu[a]

print(minieteMiesiace)

suma=sum(minieteMiesiace[:])
suma+=dzien
print(suma)

print("do końca roku zostało",365-suma)